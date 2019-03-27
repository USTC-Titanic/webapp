from page import PageHandler
class FeatureVisHandler(PageHandler):
	def get(self):
		filename = 'feature_vis/index.html'
		return self.render_file(filename)

	def post(self):
		filename = 'feature_vis/index.html'
		return self.render_file(filename)