from flask import Flask
from index import IndexHandler
from user import SignupHandler, SigninHandler, SignoutHandler, AdminHandler, ProfileHandler
from feature_vis import FeatureVisHandler
from ml_tutorial import MLTutorial
from ml_practice import MLPractice
from ml_predict import MLPredictHandler
from news import NewsHandler
from blog import BlogHandler, ArticleHandler, NewArticleHandler
from database import init_db

app = Flask(__name__)

# $ export FLASK_APP=server
# $ python3 -m flask initdb
@app.cli.command('initdb')
def init():
	init_db()
# or add the next line before app.run
# app.cli.command('initdb')(database.init_db)

@app.after_request
def add_header(response):
	# cache
	content_type = response.content_type
	if 'css;' or 'javascript' or 'image' in content_type:
		print(content_type)
		response.headers['Cache-Control'] = 'public, max-age=43200'

	return response

if __name__ == '__main__':
	app.add_url_rule( '/', view_func=IndexHandler.as_view('index') )
	app.add_url_rule( '/signin', view_func=SigninHandler.as_view('signin') )
	app.add_url_rule( '/signup', view_func=SignupHandler.as_view('signup') )
	app.add_url_rule( '/signout', view_func=SignoutHandler.as_view('signout') )
	app.add_url_rule( '/admin', view_func=AdminHandler.as_view('admin') )
	app.add_url_rule( '/profile', view_func=ProfileHandler.as_view('profile') )
	app.add_url_rule( '/feature_vis', view_func=FeatureVisHandler.as_view('feature_vis') )
	app.add_url_rule( '/tutorial', view_func=MLTutorial.as_view('ml_tutorial') )
	app.add_url_rule( '/practice', view_func=MLPractice.as_view('ml_practice') )
	app.add_url_rule( '/news', view_func=NewsHandler.as_view('news') )
	app.add_url_rule( '/blog', view_func=BlogHandler.as_view('blog') )
	app.add_url_rule( '/blog/<int:id>', view_func=ArticleHandler.as_view('article') )
	app.add_url_rule( '/blog/new', view_func=NewArticleHandler.as_view('new_article') )
	app.add_url_rule( '/predict', view_func=MLPredictHandler.as_view('ml_predict') )
	import sys
	argv = sys.argv
	if len(argv) == 1:
		# server
		context = ('../ssl/server.cer', '../ssl/server.key')
		app.run(port=443, host='0.0.0.0', debug=False, ssl_context=context)
	else:
		# local
		# app.run(port=8000, host='0.0.0.0', debug=True)
		app.run(port=8000, host='127.0.0.1', debug=True)
	