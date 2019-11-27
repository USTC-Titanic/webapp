from page import PageHandler
import requests, json, os, os.path
from time import gmtime
from html import escape, unescape

md_path = 'static/blog/md_list/'
html_path = 'static/blog/html_list/'

class BlogHandler(PageHandler):
	def get(self):
		if self.get_args('q') == 'json':
			post_list = []
			file_list = sorted(os.listdir(html_path))
			for fn in file_list:
				# 文件名格式
				# 1_2019_01_23_title.html
				fn = fn.split('_', 1)
				fid, fn = fn[0], fn[1]
				update_date = fn[:10].replace('_', '-')
				title = fn[11:-5]
				fd = {
					'id': fid,
					'title': title,
					'update_date': update_date
				}
				post_list.append(fd)
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

	def get_html(self, md_content):
		self.post_data['text'] = md_content
		url_api_github = 'https://api.github.com/markdown'
		resp = self.sess.post(url_api_github, data=json.dumps(self.post_data))

		with open('static/blog/post/post_template.html') as f:
			html_template = f.read()
			return html_template % {'content': resp.text}

parser = MarkdownParser()

class ArticleHandler(PageHandler):
	def get(self, fid):
		fid = str(fid)
		for fn in os.listdir(html_path):
			if fn.startswith(fid):
				html_fn = os.path.join(html_path, fn)
				with open(html_fn, 'r') as f:
					html_content = f.read()
					return self.render(html_content)
		# 有 md 无 html
		for fn in os.listdir(md_path):
			if fn.startswith(fid):
				md_fn = os.path.join(md_path, fn)
				with open(md_fn, 'r') as f:
					md_content = f.read()

				fn = fn.replace('.md', '.html')
				html_fn = os.path.join(html_path, fn)
				with open(html_fn, 'w') as f:
					html_content = parser.get_html(md_content)
					f.write(html_content)
					return self.render(html_content)
		# 无 md 无 html
		return self.redirect_to_target('/blog')
		
	def post(self):
		return BlogHandler().get()
		
class NewArticleHandler(PageHandler):
	def get(self):
		if self.is_valid_cookies() and self.is_admin():
			template = 'blog/new_article/new_article.html'
			return self.render_file(template)
		else:
			# 添加提示 【只有管理员可以写日志】
			return self.redirect_to_target('/blog')
	
	def post(self):
		# TODO 鉴权，只有管理员可以写日志，其他人只能看
		if self.is_admin():
			form = self.get_form()
			# escape 转义
			fd = {
				'title': escape(form.get('title')),
				'update_date': '%04d_%02d_%02d' % gmtime()[0:3],
				'fid': len(os.listdir(md_path)) + 1
			}
			# 文件名格式
			# 1_2019_01_23_title.md
			fn = '%(fid)d_%(update_date)s_%(title)s' % fd
			md_fn = os.path.join(md_path, fn + '.md')
			html_fn = os.path.join(html_path, fn + '.html')

			md_content = escape(form.get('content'))
			with open(md_fn, 'w') as f:
				f.write(md_content)

			html_content = parser.get_html(md_content)
			with open(html_fn, 'w') as f:
				f.write(html_content)

			return self.render('ok')

		# 添加提示 【只有管理员可以写日志】
		return self.redirect_to_target('/blog')

