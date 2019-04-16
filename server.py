from flask import Flask
from index import IndexHandler
from user import SignupHandler, SigninHandler, SignoutHandler
from feature_vis import FeatureVisHandler
from ml_tutorial import MLTutorial
from ml_practice import MLPractice
from ml_predict import MLPredictHandler
from news import NewsHandler
from blog import BlogHandler, PostHandler
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
	app.add_url_rule( '/feature_vis', view_func=FeatureVisHandler.as_view('feature_vis') )
	app.add_url_rule( '/tutorial', view_func=MLTutorial.as_view('ml_tutorial') )
	app.add_url_rule( '/practice', view_func=MLPractice.as_view('ml_practice') )
	app.add_url_rule( '/news', view_func=NewsHandler.as_view('news') )
	app.add_url_rule( '/blog', view_func=BlogHandler.as_view('blog') )
	app.add_url_rule( '/blog/<int:id>', view_func=PostHandler.as_view('blogpost') )
	app.add_url_rule( '/predict', view_func=MLPredictHandler.as_view('ml_predict') )
	context = ('../ssl/server.cer', '../ssl/server.key')
	# app.run(port=443, host='0.0.0.0', debug=True, ssl_context=context)
	# app.run(port=8000, host='127.0.0.1', debug=True)
	app.run(port=8080, host='0.0.0.0', debug=True)