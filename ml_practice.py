from page import PageHandler
class MLPractice(PageHandler):
	def get(self):
		filename = 'ml_practice/ml_practice.html'
		return self.render_file(filename)

	def post(self):
		filename = 'ml_practice/ml_practice.html'
		return self.render_file(filename)