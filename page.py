from flask import make_response, request
from flask.views import MethodView
# from flask.views import View
from datetime import datetime, date

base_path = './static/%s'

class PageHandler(MethodView):
	def render(self, content):
		resp = make_response(content)
		resp.headers['Strict-Transport-Security'] = 'max-age=15768000; includeSubDomains; preload'
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
			form = request.get_json()	# type-dict
		else:
			form = request.form.to_dict()
		return form