from flask import Flask, make_response
from flask.views import MethodView
app = Flask(__name__)

from flask.views import View
class Page(MethodView):
	def render_raw(self, filename):
		filename = './static/%s' % filename
		with open(filename, 'r') as f:
			response = make_response(f.read())
			return response

from random import random
class IndexHandler(Page):
	def get(self):
		filename = 'index/index.html'
		return self.render_raw(filename)
	
	def post(self):
		# TODO: 结合模型输出预测结果
		chance = random()
		print(chance)
		if chance > 0.5:
			return 'Survived'
		else:
			return 'Fallen'

if __name__ == '__main__':
	app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
	app.run(port=80, host='0.0.0.0', debug=True)