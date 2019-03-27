from page import PageHandler
class MLTutorial(PageHandler):
	def get(self):
		filename = 'ml_tutorial/ml_tutorial.html'
		return self.render_file(filename)

	def post(self):
		filename = 'ml_tutorial/ml_tutorial.html'
		return self.render_file(filename)