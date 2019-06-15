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

	def cnt_all(self):
		sql = 'select count(*) cnt from users'
		args = ()
		res = Database().query_db(sql, args)[0]['cnt']
		return res

	def update(self):
		if len(self.password) != 0:
			sql = 'update users set passwd_hash = ?, nickname = ?, email = ? where username = ?'
			passwd_hash = make_pw_hash(self.username, self.password)
			args = (passwd_hash, self.nickname, self.email, self.username)
		else:
			sql = 'update users set nickname = ?, email = ? where username = ?'
			args = (self.nickname, self.email, self.username)
		record_list = Database().query_db(sql, args)
		return record_list

	def update_password(self):
		sql = 'update users set passwd_hash = ? where username = ?'
		passwd_hash = make_pw_hash(self.username, self.password)
		args = (passwd_hash, self.username)
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
		return False
		# return True

	def get(self):
		filename = 'user/admin.html'
		# return self.render_file(filename)
		if self.is_admin():
			if self.get_args('q') == 'json':
				form = {}
				username = self.get_args('username')
				if username:
					form['username'] = username
					record_list = Record(form).retrieve()
					resp = []
					for record in record_list:
						resp.append(dict(record))
					if len(resp) == 0:
						resp = 'error'
					else:
						resp = json.dumps(resp)
				else:
					resp = Record({}).retrieve_all()
				return self.render(resp)
				# resp = '{"cnt": "%d",' % record.cnt_all() + '"userlist": %s}' % record.retrieve_all()
				# resp = Record({}).cnt_all()
				# resp = Record({}).retrieve_all()
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
		# update
		try:
			if self.is_admin():
				form = self.get_form()
				record = Record(form)
				record.update()
				return self.render('ok')
			else:
				return self.render('error')
		except Exception as e:
			return self.render('error')

	def delete(self):
		try:
			if self.is_admin():
				username = self.get_args('username')
				form = {'username': username}
				record = Record(form)
				record.delete()
				return self.render('ok')
			else:
				return self.render('error')
		except Exception as e:
			return self.render('error')

class ProfileHandler(PageHandler):
	def get(self):
		filename = 'user/profile.html'
		return self.render_file(filename)
	
	def put(self):
		us_form = self.get_form()
		us_username = us_form.get('username')
		us_old_password = us_form.get('old_password')
		us_password = us_form.get('password')
		# TODO: regex

		user = {'username': us_username}
		query = Record(user)
		record_list = query.retrieve()
		if len(record_list) > 0:
			record = dict(record_list[0])
			s_passwd_hash = record.get('passwd_hash')
			if check_pw_hash(us_username, us_old_password, s_passwd_hash):
				query.password = us_password
				query.update_password()
				return self.render('ok')
		return self.render('error')

# form = {'username': 'ustcadmin', 'password': 'captainJ', 'nickname': 'admin', 'email': 'admin@ustc.titanic'}
# record = Record(form)
# record.insert()

# form = {'username': 'Alice', 'password': '321456', 'nickname': 'alice', 'email': 'alice@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Bob', 'password': '321456', 'nickname': 'bob', 'email': 'bob@edu.b'}
# record = Record(form)
# record.insert()

# form = {'username': 'Clark', 'password': '321456', 'nickname': 'clark', 'email': 'clark@edu.a'}
# record = Record(form)
# record.insert()

# form = {'username': 'Dirk', 'password': '321456', 'nickname': 'dirk', 'email': 'dirk@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Eva', 'password': '321456', 'nickname': 'eva', 'email': 'eva@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Falcon', 'password': '321456', 'nickname': 'falcon', 'email': 'falcon@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Green', 'password': '321456', 'nickname': 'green', 'email': 'green@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Hilbert', 'password': '321456', 'nickname': 'hilbert', 'email': 'Hilbert@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Isaias', 'password': '321456', 'nickname': 'Isaias', 'email': 'Isaias@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Jack', 'password': '321456', 'nickname': 'Jack', 'email': 'Jack@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Karl', 'password': '321456', 'nickname': 'karl', 'email': 'karl@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Lee', 'password': '321456', 'nickname': 'Lee', 'email': 'lee@edu.c'}
# record = Record(form)
# record.insert()

# form = {'username': 'Melon', 'password': '321456', 'nickname': 'Melon', 'email': 'melon@edu.c'}
# record = Record(form)
# record.insert()