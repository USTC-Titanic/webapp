from page import PageHandler
from time import time
import requests, json, re, os.path

filename_36kr = 'db/36kr.json'
filename_netease = 'db/netease.json'
filename_huxiu = 'db/huxiu.json'
url_36kr = 'https://36kr.com/api/newsflash?&per_page=20'
url_netease = 'https://tech.163.com/special/00097UHL/smart_datalist.js?callback=data_callback'
url_huxiu = 'https://www.huxiu.com/channel/104.html'

re_netease_newstitle = re.compile(r'"title":"(.*)?"')
re_netease_newsurl = re.compile(r'"docurl":"(.*)?"')
re_netease_newstime = re.compile(r'"time":"(.*)?"')

re_huxiu_newstitle = re.compile(r'<a class="transition" title="(.*)?"')
re_huxiu_newscontent = re.compile(r'<div class="mob-sub">(.*)?</div>')
re_huxiu_newsurl = re.compile(r'<a href="(.*)?" class="transition msubstr-row2" target="_blank">')
re_huxiu_newstime = re.compile(r'<span class="time">')

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
		elif src == 'huxiu':
			if self.news_expire(filename_huxiu) == True:
				return self.update_huxiu_news()
			else:
				return self.load_news(filename_huxiu)
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

	def update_huxiu_news(self):
		headers = {
			'cookie': 'screen=%7B%22w%22%3A1280%2C%22h%22%3A800%2C%22d%22%3A2%7D; __secdyid=1698668e15bf4b18595453f12da5d4133ad3da4a5ae59bd9021554868559; huxiu_analyzer_wcy_id=3hb72epa6i9cjutwleg9; gr_user_id=313549f5-bc21-464d-b11a-b2474351a6d1; b6a739d69e7ea5b6_gr_last_sent_cs1=0; grwng_uid=38b22c85-9b86-4994-bce4-e19ba58eb17e; _ga=GA1.2.510960547.1554868562; screen=%7B%22w%22%3A1280%2C%22h%22%3A800%2C%22d%22%3A2%7D; p_h5_u=7243040F-8775-454C-9AE9-E84128C0D72C; selectedStreamLevel=SD; b6a739d69e7ea5b6_gr_session_id=ede0a44a-03a4-435f-a103-d1dfdfb1d722; b6a739d69e7ea5b6_gr_last_sent_sid_with_cs1=ede0a44a-03a4-435f-a103-d1dfdfb1d722; _gid=GA1.2.480895303.1555469158; _gat=1; Hm_lvt_324368ef52596457d064ca5db8c6618e=1554868563,1555469158; b6a739d69e7ea5b6_gr_session_id_ede0a44a-03a4-435f-a103-d1dfdfb1d722=true; b6a739d69e7ea5b6_gr_cs1=0; Hm_lpvt_324368ef52596457d064ca5db8c6618e=1555469165; SERVERID=f60b85c1ffd425d843469f623dc2b612|1555469159|1555469148',
			'dnt': '1',
			'pragma': 'no-cache',
			'referer': 'https://www.huxiu.com/',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
		}

		content = requests.Session().get(url_huxiu, headers=headers).text
		news_list = []
		title_list = re_huxiu_newstitle.findall(content)
		content_list = re_huxiu_newscontent.findall(content)
		newsurl_list = re_huxiu_newsurl.findall(content)
		# newstime_list = re.re_huxiu_newstime.findall(content)
		for i in range(20):
			news = {}
			news['title'] = title_list[i]
			news['content'] = content_list[i]
			news['url'] = 'https://www.huxiu.com/' + newsurl_list[i]
			news['time'] = ''
			news_list.append(news)
		news_list = json.dumps(news_list, ensure_ascii=False)
		with open(filename_huxiu, 'w', encoding='utf-8') as f:
			f.write(news_list)
		return news_list

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
