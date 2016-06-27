#!/usr/bin/python
import socket,sys,urllib
import optparse
from bs4 import BeautifulSoup

def spider(url):
	url=str(url)
	request = urllib.urlopen(url)
	bs = BeautifulSoup(request.read(),"lxml")
	link = bs.find_all('a')
	for links in link:
		print links['href']

def head(header):
	url=str(header)
	request = urllib.urlopen(url)
	for item, value in request.headers.items():
		print item + ": " +value
def port(host):
	for port in range(1,35565):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			timeout = s.settimeout(2.0)
			try:
				s.recv(1024)
				print("[+] Port %d: is open " % (port))
			except:
				print("[+] Port %d: is open " % (port))
		except:	pass
	s.close()

def main():
	#parser
	parser = optparse.OptionParser(sys.argv[0]+''+ ' -c url  -p host -d url')
	parser.add_option('-c' , dest='url', type='string', help='spidering')
	parser.add_option('-p', dest='host', type='string', help='port scan')
	parser.add_option('-d', dest='header', type='string', help='header')
	(options, args) = parser.parse_args()
	url = options.url
	host = options.host
	header = options.header
	if url:
		spider(url)
	if host:
		port(host)
	if header:
		head(header)
	else:
		print parser.usage

main()
