from page import PageHandler
import requests, json, os
from time import gmtime
from html import escape, unescape

article_list_path = 'static/blog/article_list'

class BlogHandler(PageHandler):
	def get(self):
		if self.get_args('q') == 'json':
			size = len(os.listdir(article_list_path)) + 1
			post_list = []
			for id in range(1, size):
				try:
					with open('static/blog/article_list/article_%d.md' % id) as f:
						title = unescape(f.readline())
						update_date = f.readline()
						post_list.append({'title': title, 'update_date': update_date, 'id': id})
				except Exception as e:
					pass
				# post_list = [
				# 	{'title': 'GitHub API 测试', 'update_date': '2019-04-16', 'id': '1'},
				# 	{'title': '人工智能实验3: 基于TensorFlow的cpatcha注册码识别', 'update_date': '2019-04-16', 'id': '2'},
				# 	{'title': 'Titanic 特征分析1', 'update_date': '2019-04-16', 'id': '3'},
				# 	{'title': 'Titanic 特征分析2', 'update_date': '2019-04-16', 'id': '4'},
				# ]
			return self.render_json( json.dumps(post_list, ensure_ascii=False) )
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

		return self.html % {'content': resp.text}

parser = MarkdownParser()

class ArticleHandler(PageHandler):
	def get(self, id):
		try:
			with open('static/blog/article_list/article_%d.md' % id) as f:
				f.readline()
				f.readline()
				md_content = f.read()
	
			html = parser.get_html(md_content)
			return self.render(html)
		except Exception as e:
			return self.redirect_to_target('/blog')
		
	def post(self):
		return BlogHandler().get()
		
class NewArticleHandler(PageHandler):
	def get(self):
		if self.is_valid_cookies():
			filename = 'blog/new_article/new_article.html'
			return self.render_file(filename)
		else:
			return self.redirect_to_target('/signin')
	
	def post(self):
		# TODO 鉴权，只有管理员可以写日志，其他人只能看
		form = self.get_form()
		title = escape(form.get('title'))
		content = escape(form.get('content'))
		update_date = '%04d-%02d-%02d' % gmtime()[0:3]
		id = len(os.listdir(article_list_path)) + 1
		with open('%s/article_%d.md' % (article_list_path, id), 'w') as f:
			f.write(title + '\n' + update_date + '\n' + content)
		return self.render('ok')