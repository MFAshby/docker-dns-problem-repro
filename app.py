from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer
from os import fork
from time import sleep
from urllib.request import urlopen
from sys import argv, exc_info

PORT = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

def run_http_server():
    with TCPServer(("", PORT), Handler) as httpd:
        try:
            # print("serving at port", PORT)
            httpd.serve_forever()
        finally: 
            httpd.shutdown()
            httpd.server_close()

def poll_other_servers():
    n_servers = int(argv[1])
    while True:
        for i in range(n_servers):
            try:
                with urlopen("http://app-{i}".format(i=i)) as response:
                   x = response.read()
            except Exception as e:
                print(e)
        sleep(1)

if __name__=="__main__":
    newpid = fork()
    if newpid == 0:
        poll_other_servers()
    else:
        run_http_server()
