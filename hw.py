#! /usr/bin/env python
# coding: utf-8

from wsgiref.simple_server import make_server

def hellow_world(environ, start_response):
	response_body = 'тест'
	status = '200 OK'
	response_headers = [('Content-Type', 'text/plain'), ('charset', 'utf-8'),
                  ('Content-Length', str(len(response_body)))]
	start_response(status, response_headers)
	return [response_body]

httpd = make_server(
	'localhost',
	1234,
	hellow_world
	)
httpd.handle_request()