import hmac
from flask import make_response, request, redirect
from flask.views import MethodView
from datetime import datetime, date

base_path = './static/%s'
admin_username = 'ljj'

class PageHandler(MethodView):
	def render(self, content):
		resp = make_response(content)
		return resp

	def render_json(self, content):
		resp = make_response(content)
		resp.headers['content-type'] = 'application/json'
		return resp

	def render_file(self, filename):
		filepath = base_path % filename
		with open(filepath, 'r') as f:
			content = f.read()
			return self.render(content)

	def get_args(self, key):
		return request.args.get(key)

	def get_date(self, year=0, month=0, day=0):
		if year and month and day:
			return date(year, month, day)
		else:
			return date.today()

	def get_referer(self):
		return request.headers.get('referer')

	def get_cookies(self):
		return request.cookies

	def get_form(self):
		form = {}
		if request.is_json:
			# type-dict
			form = request.get_json()
		else:
			form = request.form.to_dict()
		return form

	def login(self, user):
		resp = make_response('succ')
		resp.set_cookie(key='username', value=user.username, max_age=3600)
		uid_and_digest = make_secure_cookie(user.uid, user.username)
		resp.set_cookie(key='uid', value=uid_and_digest, max_age=3600)
		resp.set_cookie(key='nickname', value=user.nickname, max_age=3600)
		return resp

	def logout(self):
		target = '/'
		resp = redirect(target)
		resp.set_cookie(key='username', value='')
		resp.set_cookie(key='uid', value='')
		resp.set_cookie(key='nickname', value='')
		return self.render(resp)

	def is_valid_cookies(self):
		try:
			cookies = request.cookies
			uid_and_digest = cookies.get('uid')
			username = cookies.get('username')
			return check_secure_cookies(uid_and_digest, username)
		except Exception as e:
			return False

	def is_admin(self):
		username = self.get_username()
		if username == admin_username:
			return True
		return False

	def get_username(self):
		try:
			cookies = request.cookies
			username = cookies.get('username')
			return username
		except Exception as e:
			return ''

	def redirect_to_target(self, target='/'):
		return self.render(redirect(target))

# DK is the generated derived key
# A derived key is a key, which may be calculated (derived) by a well-defined algorithm, usually referred to as a key derivation function, from an input consisting of public as well as secret data (e.g., a master key or primary key).
hkey = 'dk_Huygens'.encode()
def make_secure_cookie(uid, username):
	msg = uid + username
	digest = hmac.new( hkey, msg.encode() ).hexdigest()
	uid_and_digest = '%s|%s' % (uid, digest)
	return uid_and_digest

def check_secure_cookies(uid_and_digest, username):
	if uid_and_digest:
		uid = uid_and_digest.split('|')[0]
		us_uid_and_digest = make_secure_cookie(uid, username)
		return uid_and_digest == us_uid_and_digest
	else:
		return False