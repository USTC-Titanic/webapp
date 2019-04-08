import sqlite3

DB_USER = 'db/user.db'
SCHEMA = 'db/schema_user.sql'

def init_db():
	try:
		conn = sqlite3.connect(DB_USER)
		cur = conn.cursor()
		with open(SCHEMA, 'r') as f:
			cur.executescript(f.read())
		conn.commit()
	except Exception as e:
		pass
	finally:
		cur.close()
		conn.close()

class Database(object):
	def __init__(self):
		pass

	def query_db( self, query, args=() ):
		record_list = []
		try:
			conn = sqlite3.connect(DB_USER)
			conn.row_factory = sqlite3.Row
			cur = conn.cursor()
			cur.execute(query, args)
			record_list = cur.fetchall()
			conn.commit()
		except Exception as e:
			pass
		finally:
			cur.close()
			conn.close()
		return record_list

if __name__ == '__main__':
	# init_db()
	# sql = 'insert into users (username, passwd_hash, email) values (?, ?, ?)'
	# args = ('abc', 'xyz', '1@c')
	sql = 'select * from users where username = ?'
	args = ('abc', )
	# sql = 'select * from users'
	# args = ()
	db = Database()
	record_list = db.query_db(sql, args)
	# if record_list:
	# 	print(record_list)
	# for record in record_list:
		# print(*record)
