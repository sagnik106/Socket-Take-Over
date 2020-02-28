import socket
import subprocess
import os
import sys
while True:
	try:
		s=socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		port=8888
		s.connect(('172.16.165.195',port))
		print(s)
		while True:
			x=input('$ ')
			if x is not 'STOP':
				s.send(x.encode())
				print(str(s.recv(8192),"utf-8"))
			else:
				break
	except KeyboardInterrupt:
		break
	except:
		pass
