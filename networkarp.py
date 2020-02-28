import subprocess
import os
mac='9c:d2:1e:4e:57:bf'
cmd = subprocess.Popen("arp",shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
output= str(cmd.stdout.read() + cmd.stderr.read(),"utf-8")
users=output.split('\n')
b=list()
for j in range(len(users)):
	a=list()
	for i in users[j].split(' '):
		if len(i)>0:
			a.append(i)
	if len(a)>0:
		for k in a:
			if k==mac:
				b.append(a)
try:
	b=b[0][0]
	print("ip  : %s\nMAC : %s"%(b,mac))
except IndexError:
	print("The device %s was not found on the network"%mac)
