import os

def inital_dir():
	if os.path.exists('response_code'):
		os.system('rm -r response_code')
	os.system('mkdir response_code')
	os.system('mkdir response_code/http')
	os.system('mkdir response_code/https')
	os.system('mkdir response_code/http/1xx')
	os.system('mkdir response_code/http/2xx')
	os.system('mkdir response_code/http/3xx')
	os.system('mkdir response_code/http/4xx')
	os.system('mkdir response_code/http/5xx')
	os.system('mkdir response_code/http/error')
	os.system('mkdir response_code/https/1xx')
	os.system('mkdir response_code/https/2xx')
	os.system('mkdir response_code/https/3xx')
	os.system('mkdir response_code/https/4xx')
	os.system('mkdir response_code/https/5xx')
	os.system('mkdir response_code/https/error')
