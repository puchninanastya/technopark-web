from cgi import parse_qs

class MySimpleWsgiApp:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
	get_params = parse_qs(self.environ['QUERY_STRING'])
	try:
		request_body_size = int(self.environ.get('CONTENT_LENGTH', 0))
	except:
		request_body_size = 0	
	request_body = self.environ['wsgi.input'].read(request_body_size)	
	post_params = parse_qs(request_body)
	
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)

	output_str  = "Method: " + str(self.environ['REQUEST_METHOD']) + "\n"
	if (request_body_size):
		output_str += "Content-length: " + str(request_body_size) + "\n"
	if (post_params):
		output_str += "Post params:\n" + str(post_params) + "\n"
	if (get_params):
		output_str += "Get params:\n" + str(get_params) + "\n"

	yield output_str

def MySimpleStaticApp(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type', 'text/html')]	
	start_response(status, response_headers)
	output_str = '<p>This is static html !!!</p>'
	yield output_str 
