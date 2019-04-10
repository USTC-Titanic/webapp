from page import PageHandler
import requests, json
import os.path
from time import time

filename_36kr = 'db/36kr.json'
# url_36kr = 'https://36kr.com/api/newsflash?&per_page=20'
url_36kr = 'https://36kr.com/api/newsflash'

class Spider(object):
	def get_news(self, src="36kr"):
		if src == "36kr":
			if self.news_expire(filename_36kr) == True:
				return self.update_36kr_news()
			else:
				return self.load_news(filename_36kr)
		else:
			return '[{"title":"", "content":"", "time":""}]'

	def update_36kr_news(self):
		try:
			headers = {
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'zh-CN,zh;q=0.9',
				'Host': '36kr.com',
				'Connection': 'keep-alive',
				'Cache-Control': 'no-cache',
				'Pragma': 'no-cache',
				'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
			}
			json_resp = requests.Session().get(url_36kr, headers=headers).json()['data']['items']
			news_list = []
			for item in json_resp:
				news = {}
				# 只保存 title, content, time
				news['title'] = item['title']
				news['content'] = item['description']
				news['time'] = item['created_at']
				news_list.append(news)
			news_list = json.dumps(news_list, ensure_ascii=False)
			with open(filename_36kr, 'w', encoding="utf-8") as f:
				f.write(news_list)
			return news_list
		except Exception as e:
			pass

	def store_jiqizhixin_news(self, json_resp={}):
		'''
		TODO
		如何获得 X-CSRF-Token
		或者, 使用 Selenium + phantomjs
		'''
		headers = {
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Connection': 'keep-alive',
			'Content-Length': '525',
			'Cache-Control': 'no-cache',
			'content-type': 'application/json',
			'Host': 'www.jiqizhixin.com',
			'Origin': 'https://www.jiqizhixin.com',
			'Referer': 'https://www.jiqizhixin.com/dailies',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
		}
		post_data = {
			"operationName":"Dailies",
			"variables":{"cursor":""},
			"query":'\
"query Dailies($cursor: String) {\
  dailies(first: 10, after: $cursor) {\
    edges {\
      node {\
        ...DailyInfo\
        __typename\
      }\
      __typename\
    }\
    pageInfo {\
      ...PageInfo\
      __typename\
    }\
    __typename\
  }\
}\
\
fragment DailyInfo on Daily {\
  id\
  title\
  content\
  likes_count\
  url\
  created_at\
  path\
  __typename\
}\
\
fragment PageInfo on PageInfo {\
  endCursor\
  hasNextPage\
  __typename\
}\
"\
'
		}
		pass

	def news_expire(self, filename):
		'''
		如果超过了 10 分钟, 则判定为过期, 需要更新新闻文件
		'''
		try:
			last_modified = os.path.getmtime(filename)
			now = time()
			expires = now - last_modified > 600
			return expires
		except FileNotFoundError as e:
			# 如果文件不存在, 则视为过期
			return False

	def load_news(self, filename):
		try:
			with open(filename, 'r') as f:
				news_list = f.read()
			return news_list
		except FileNotFoundError as e:
			return ""


spider = Spider()

class NewsHandler(PageHandler):
	def get(self):
		filename = 'news/news.html'
		if self.get_args('q') == 'json':
			src = self.get_args('src')
			return self.render( spider.get_news(src) )

		return self.render_file(filename)
