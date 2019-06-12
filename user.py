import re, random, hashlib, json
from string import ascii_letters as letters
from page import PageHandler
from database import Database

# 随机生成长度为 5 的 salt, 由大小写字母构成
def make_salt(length=5):
	# salt = []
	# for i in range(length):
	# 	salt.append(random.choice(letters))
	# return ''.join(salt)
	return ''.join(random.choice(letters) for x in range(length))

admin_username = 'ustcadmin'

def make_pw_hash(username, password, salt=None):
	if not salt:
		salt = make_salt()
	enc = (username + password + salt).encode('utf-8')
	# digest is returned as a string object containing only hexadecimal digits
	passwd_hash = hashlib.sha256(enc).hexdigest()
	return '%s,%s' % (salt, passwd_hash)

def check_pw_hash(username, password, passwd_hash):
	salt = passwd_hash.split(',')[0]
	return passwd_hash == make_pw_hash(username, password, salt)

class User(object):
	def __init__(self, form):
		self.uid = str(form.get('uid'))
		self.username = form.get('username')
		self.password = form.get('password')
		self.nickname = form.get('nickname')
		self.email = form.get('email')

class Record(User):
	def insert(self):
		sql = 'insert into users (username, passwd_hash, nickname, email) values (?, ?, ?, ?)'
		passwd_hash = make_pw_hash(self.username, self.password)
		args = (self.username, passwd_hash, self.nickname, self.email)
		record_list = Database().query_db(sql, args)
		return record_list

	def retrieve(self):
		sql = 'select * from users where username = ?'
		args = (self.username, )
		record_list = Database().query_db(sql, args)
		return record_list

	def retrieve_all(self):
		sql = "select uid, username, nickname, email from users where username <> '%s'" % admin_username
		args = ()
		record_list = Database().query_db(sql, args)
		resp = []
		for record in record_list:
			resp.append(dict(record))
		return json.dumps(resp)

	def update(self):
		sql = 'update users set passwd_hash = ?, nickname = ?, email = ? where username = ?'
		passwd_hash = make_pw_hash(self.username, self.password)
		args = (passwd_hash, self.nickname, self.email, self.username)
		record_list = Database().query_db(sql, args)
		return record_list

	def delete(self):
		sql = 'delete from users where username = ?'
		args = (self.username, )
		record_list = Database().query_db(sql, args)
		return record_list

# 检查用户名、密码、邮箱是否符合规则
re_username = re.compile(r'^[a-zA-Z0-9_-]{3,16}$')
re_password = re.compile(r'^.{6,16}$')
re_nickname = re.compile(r'^.{3,16}$')
re_email = re.compile(r'^[\S]+@[\S]+.[\S]+$')
def check_valid(form):
	if 'username' not in form or 'password' not in form or 'nickname' not in form or 'email' not in form:
		return False
	elif not re_username.match(form['username']):
		return False
	elif not re_password.match(form['password']):
		return False
	elif not re_nickname.match(form['nickname']):
		return False
	elif not re_email.match(form['email']):
		return False
	else:
		return True

# 检查用户名是否可用
def check_usable(form):
	# 如果数据库中已经存在记录, 说明该用户名已经被占用了
	if len(Record(form).retrieve()) > 0:
		return False
	else:
		return True

class SignupHandler(PageHandler):
	def get(self):
		filename = 'user/signup.html'
		if self.is_valid_cookies():
			return self.redirect_to_target('/')
		else:
			return self.render_file(filename)

	def post(self):
		form = self.get_form()
		# 检查用户名, 密码, 昵称, 邮箱是否符合规则
		if check_valid(form) == True:
			# 检查用户名是否可用
			if check_usable(form) == True:
				return self.register(form)
			else:
				return self.render('taken')
		else:
			return self.render('error')

	def register(self, form):
		record = Record(form)
		record.insert()
		record_list = record.retrieve()
		if len(record_list) > 0:
			record = dict(record_list[0])
			user = User(record)
			# 登录并设置 cookie
			return self.login(user)
		else:
			return 'errorio'

class SigninHandler(PageHandler):
	def get(self):
		filename = 'user/signin.html'
		if self.is_valid_cookies():
			return self.redirect_to_target('/')
		else:
			return self.render_file(filename)

	def post(self):
		us_form = self.get_form()
		us_username = us_form.get('username')
		us_password = us_form.get('password')
		record_list = Record(us_form).retrieve()
		if len(record_list) > 0:
			record = dict(record_list[0])
			s_passwd_hash = record.get('passwd_hash')
			if check_pw_hash(us_username, us_password, s_passwd_hash):
				user = User(record)
				# sign in and set cookie
				return self.login(user)
		return self.render('error')

class SignoutHandler(PageHandler):
	def get(self):
		return self.logout()

	def post(self):
		return self.logout()

class AdminHandler(PageHandler):
	def is_admin(self):
		if self.is_valid_cookies():
			username = self.get_username()
			if username == admin_username:
				return True
		# return False
		return True

	def get(self):
		filename = 'user/admin.html'
		# return self.render_file(filename)
		if self.is_admin():
			if self.get_args('q') == 'json':
				resp = Record({}).retrieve_all()
				print(resp)
				return self.render(resp)
			else:
				return self.render_file(filename)
		return self.redirect_to_target('/signin')

	# CRUD
	def post(self):
		filename = 'user/admin.html'
		return self.render_file(filename)
		if self.is_admin():
			'''
			do restful crud
			post    --   create
			get    ---   retrieve, select
			put    ---   update
			delete ---   delete
			param
			?limit=10 --- 指定返回记录的数量
			'''
			return self.render('')
		return self.redirect_to_target('/signin')

	def put(self):
		return self.render('ok')

	def delete(self):
		return self.render('ok')
