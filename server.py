from flask import Flask
from index import IndexHandler
from user import SignupHandler, SigninHandler, SignoutHandler
from database import init_db

app = Flask(__name__)

# $ export FLASK_APP=server
# $ python3 -m flask initdb
@app.cli.command('initdb')
def init():
	init_db()
# or add the next line before app.run
# app.cli.command('initdb')(database.init_db)

if __name__ == '__main__':
	app.add_url_rule( '/', view_func=IndexHandler.as_view('index') )
	app.add_url_rule( '/signin', view_func=SigninHandler.as_view('signin') )
	app.add_url_rule( '/signup', view_func=SignupHandler.as_view('signup') )
	app.add_url_rule( '/signout', view_func=SignoutHandler.as_view('signout') )
	context = ('../ssl/server.cer', '../ssl/server.key')
	# app.run(port=443, host='0.0.0.0', debug=True, ssl_context=context)
	app.run(port=8080, host='0.0.0.0', debug=True)