from page import PageHandler
import requests, json
import os.path
from time import time

class Spider(object):
	filename_36kr = 'db/36kr.json'
	url_36kr = 'https://36kr.com/api/newsflash?&per_page=20'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

	def update_news(self):
		last_modified_36kr = os.path.gettime(filename_36kr)
		now = time()
		# 如果超过了 10 分钟, 就更新新闻文件
		expires_36kr = now - last_modified_36kr > 600
		if expires_36kr:
			self.get_news(url_36kr)

	def get_news(self, url=url_36kr, filename='36kr'):
		try:
			sess = requests.Session()
			resp = sess.get(url, headers=headers, )
			text = resp.text
			# TODO 不保存无效信息
			# 只保存 title, description, time, link
			# news_filter
			with open('db/%s.json' % filename, 'w') as f:
				f.write(text)
		except Exception as e:
			pass

	def get_json_news(self, ):
		try:
			with open('db/%s.json' % filename_36kr, 'r') as f:
				content = f.read()
			news = {'36kr': json.loads(content)}
			return news
		except Exception as e:
			raise

	def test1(self):
		self.update_news()

	def test2(self):
		d = self.get_json_news()
		print(d['data']['items'][0]['title'])

spider = Spider()

class NewsHandler(PageHandler):
	filename = 'news/news.html'
	def get(self):
		spider.update_news()
		if self.get_args('q') == 'json':
			return self.render(spider.get_json_news())
		else:
			return self.render_file(filename)

