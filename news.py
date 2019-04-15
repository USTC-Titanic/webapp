from page import PageHandler
from time import time
import requests, json, re, os.path

filename_36kr = 'db/36kr.json'
filename_netease = 'db/netease.json'
url_36kr = 'https://36kr.com/api/newsflash?&per_page=20'
url_netease = 'https://tech.163.com/special/00097UHL/smart_datalist.js?callback=data_callback'

re_netease_newstitle = re.compile(r'"title":"(.*)?"')
re_netease_newsurl = re.compile(r'"docurl":"(.*)?"')
re_netease_newstime = re.compile(r'"time":"(.*)?"')

class Spider(object):
	def get_news(self, src="36kr"):
		if src == "36kr":
			if self.news_expire(filename_36kr) == True:
				return self.update_36kr_news()
			else:
				return self.load_news(filename_36kr)
		elif src == 'netease':
			if self.news_expire(filename_netease) == True:
				return self.update_netease_news()
			else:
				return self.load_news(filename_netease)
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
				news['title'] = item['title']
				news['content'] = item['description']
				news['url'] = item['news_url']
				news['time'] = item['created_at']
				news_list.append(news)
			news_list = json.dumps(news_list, ensure_ascii=False)
			with open(filename_36kr, 'w', encoding="utf-8") as f:
				f.write(news_list)
			return news_list
		except Exception as e:
			pass

	def update_netease_news(self):
		try:
			resp = requests.Session().get(url_netease).text
			title_list = re_netease_newstitle.findall(resp)
			url_list = re_netease_newsurl.findall(resp)
			time_list = re_netease_newstime.findall(resp)
			news_list = []
			for i in range(len(title_list)):
				news = {}
				news['title'] = title_list[i]
				news['content'] = title_list[i]
				news['url'] = url_list[i]
				news['time'] = time_list[i]
				news_list.append(news)
			news_list = json.dumps(news_list, ensure_ascii=False)
			with open(filename_netease, 'w', encoding="utf-8") as f:
				f.write(news_list)
			return news_list
		except Exception as e:
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
		except Exception as e:
			# 如果文件不存在, 则视为过期
			return True

	def load_news(self, filename):
		try:
			with open(filename, 'r') as f:
				news_list = f.read()
			return news_list
		except Exception as e:
			return ""

spider = Spider()

class NewsHandler(PageHandler):
	def get(self):
		filename = 'news/news.html'
		if self.get_args('q') == 'json':
			src = self.get_args('src')
			return self.render( spider.get_news(src) )

		return self.render_file(filename)
