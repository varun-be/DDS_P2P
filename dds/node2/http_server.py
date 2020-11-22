import http.server
import socketserver
SERVERPORT = 10011
import os

web_dir = os.getcwd()
#web_dir = os.path.join(web_dir,"data/")
print(web_dir)
#os.chdir("/home/pc/Documents/Projects/DDS/own/node1/data")

def serve():

	Handler = http.server.SimpleHTTPRequestHandler
	with socketserver.TCPServer(("", SERVERPORT), Handler) as httpd:
    #	print("serving at port", SERVERPORT)
		httpd.serve_forever()
