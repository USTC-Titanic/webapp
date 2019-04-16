from page import PageHandler
import requests, json

class BlogHandler(PageHandler):
	def get(self):
		if self.get_args('q') == 'json':
			post_list = [
				{'title': 'GitHub API 测试', 'update_date': '2019-04-16', 'id': '1'},
				{'title': '人工智能实验3: 基于TensorFlow的cpatcha注册码识别', 'update_date': '2019-04-16', 'id': '2'},
				{'title': 'Titanic 特征分析1', 'update_date': '2019-04-16', 'id': '3'},
				{'title': 'Titanic 特征分析2', 'update_date': '2019-04-16', 'id': '4'},
			]
			return self.render( json.dumps(post_list, ensure_ascii=False) )
		else:
			filename = 'blog/blog.html'
			return self.render_file(filename)

class MarkdownParser(object):
	def __init__(self):
		self.post_data = {
			'text': '',
			'mode': 'gfm',
			'context': 'github/gollum'
		}
		self.sess = requests.Session()
		with open('static/blog/post/post_template.html') as f:
			self.html = f.read()

	def get_html(self, md_content):
		self.post_data['text'] = md_content
		url_api_github = 'https://api.github.com/markdown'
		resp = self.sess.post(url_api_github, data=json.dumps(self.post_data))

		return self.html % resp.text

parser = MarkdownParser()

class PostHandler(PageHandler):
	def get(self, id):
		# TODO, 为防止歧义, 以后改名为 ArticleHandler
		with open('static/blog/post/post%d.md' % id) as f:
			md_content = f.read()

		html = parser.get_html(md_content)
		return self.render(html)