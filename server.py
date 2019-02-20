from flask import Flask
from index import IndexHandler

app = Flask(__name__)

if __name__ == '__main__':
	app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
	context = ('../ssl/server.cer', '../ssl/server.key')
	app.run(port=443, host='0.0.0.0', debug=True, ssl_context=context)
	# app.run(port=8080, host='0.0.0.0', debug=True, threaded=True)
