import socket
import threading
import time
import os
SERVER_PORT = 8889
from replication import *
import shutil

serv_dict = {}
path_list = {}
port_list = set()

def connectionHandler():
	while True:
		c, addr = s.accept()
		print("Got connection from",addr)	
		thread1 = threading.Thread(target = clientHandler, args=(c,addr))
		thread1.daemon = True
		thread1.start()

def clientHandler(c,addr):
	path = c.recv(1024)
	path = path.decode('utf-8')
	path_list[addr[1]] = path
	p_list = path_list
	port_list.add(addr[1])
	#c.send(b"Thank you")


def replicationHandler():
	while True:
		time.sleep(5)
		set1 = set()
		for i in port_list:
			f = open("gg.txt","a+")	
			path = path_list[i]
			g = open(path,"r")
			data = g.read()
			f.close()
			g.close()
			data = data.split("\n")
			temp = []
			for d in data:
				temp.append(d)						
			serv_dict[i] = temp
			s_dict = serv_dict			
			print("serv dict",serv_dict)

def temp():
	while True:
		time.sleep(5)
		#print("in temp")
		rep_ans = replication(serv_dict)
		for i  in rep_ans:
			for key, value in serv_dict.items():
				if i in value:
					continue
				else:
					for k, v in serv_dict.items():
						if i in v:
							link = path_list[k]
							head, tail = os.path.split(link)
							head = os.path.join(head,"data")
							source = os.path.join(head,i)
							h, t = os.path.split(path_list[key])
							dest = os.path.join(h,"data")
							shutil.copy(source,dest)
							#print("source",source)
							#print("dest",dest)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',SERVER_PORT))
print("socket binded to %s" %(SERVER_PORT))
s.listen(5)
print("Socket listening")
thread3 = threading.Thread(target = replicationHandler, args=())
thread3.daemon  = True
thread3.start()
thread7 = threading.Thread(target = temp, args = ())
thread7.daemon = True
thread7.start()
print("Use one of the mirrors to download files",port_list)
connectionHandler()





	

