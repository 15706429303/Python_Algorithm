import os
import re
import urllib
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

class TestHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        file = os.path.join(r'd://', 'PowerCmd.rar')
        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header('Welcome','Contect')

        self.send_header("Content-Disposition", "attachment;filename=gradle-4.1-all.zip");
        self.end_headers()
        with open(file,'rb') as aaa:
            self.wfile.write(aaa.read())

def start_server(port):
    http_server = HTTPServer(('',int(port)),TestHTTPHandler)
    http_server.serve_forever()

start_server(8000)