import socket
import subprocess
import os
import sys
while True:
	try:
		s=socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		port=8888
		s.connect(('127.0.0.1',port))
		print(s)
		while True:
			x=input('$ ')
			if x[:6] == 'filetx':
				s.send(x.encode())
				gh=s.recv(1024)
				try:
					f=open(x[7:],'r')
					for i in f:
						s.send(str.encode(i))
					f.close()
				except:
					print("File not found")
				s.send(str.encode('filetxd'))
			elif x != 'STOP':
				s.send(x.encode())
				print(str(s.recv(1024),"utf-8"))
			else:
				break
	except KeyboardInterrupt:
		break
	except:
		pass
