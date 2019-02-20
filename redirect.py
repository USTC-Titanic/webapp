from wsgiref.util import request_uri
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
	uri = request_uri(environ)            # 获取 client 请求的地址 URI
	location = uri[:4] + 's' + uri[4:]    # 将 http 替换成 https
	status = '301 Moved Permanently'      # 设置 Status Code
	headers = [ ('Content-length', '0'), ('Location', location) ] # 设置 headers

	start_response(status, headers)
	return b''

httpd = make_server('0.0.0.0', 80, simple_app)
httpd.serve_forever()
