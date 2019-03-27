from page import PageHandler

class IndexHandler(PageHandler):
	def get(self):
		filename = 'index/index.html'
		return self.render_file(filename)

	def post(self):
		filename = 'index/index.html'
		return self.render_file(filename)