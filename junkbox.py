from cmd import Cmd
import requests,socket,sys,re
from lxml import html

class MyPrompt(Cmd):
    def do_head( args, url):

	r = requests.get(url)
	header = r.headers
	for item, value in header.items():
		print item+" : "+value

    def do_createPattern(args, size):
	char1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	char2="abcdefghijklmnopqrstuvwxyz"
	char3="0123456789"
			
	pattern = []
	max = int(size)
	while len(pattern) < max:
		for ch1 in char1:
			for ch2 in char2:
				for ch3 in char3:
					if len(pattern) < max:
						pattern.append(ch1)

					if len(pattern) < max:
						pattern.append(ch2)

					if len(pattern) < max:
						pattern.append(ch3)

	pattern = "".join(pattern)   
	print pattern

    def do_findOffset(args, pat,size):
	mspattern = createPattern(size)
	if pat in mspattern:
		p = mspattern.index(pat)
		print "pattern offset is %s " %p

    def do_spider(args, url):
	r = request.get(url)
	page = html.fromstring(r.content)
	link = page.xpath('//a/@href')
	for item in link:
		print item

    def do_portscan(args, host):
       
        for port in range(1,1025):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                res = s.connect_ex((host,port))
                if (res ==0 ):
                        print "open {0} at {1}".format(port,host)
		s.close

    def do_strev(args, st):
	
	rev = st[::-1]
	hx = rev.encode("hex")
	o = []
	while hx:
		o.append(hx[:8])
		hx = hx[8:]
	for i in o:
		print "reverse hex for string "+st+ " is " + i
    def do_search(args, st):
        temp = []
        url = 'http://www.google.com/search'
        payload  = {'q' : st , 'start' : '0'}
        my_head = {'User-agent': 'Mozilla/11.0'}

        r = requests.get(url, params=payload, headers=my_head)

        page = html.fromstring(r.content)
        link = page.xpath('//h3[1]/a/@href')
        for i in link:
                try:
                        temp.append(re.search("url\?q=(.+?)\&sa",i).group(1))
                except:
                        continue
        for l in temp:
                print l

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit

    def help_head(self):
		print "usage : head http://www.example.com"
    def help_spider(self):
		print "usage : spider http://www.example.com"
    def help_portscan(self):
		print "usage : portscan $IP"
    def help_strev(self):
		print "usage : strev $STRINGS"
    def help_createPattern(self):
		print "usage : createPattern SIZE"
    def help_findOffset(self):
		print "usage : findOffset $pat $SIZE"
    def help_search(self):
		print "usage: search $Strings"

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'myjunkbox> '
    prompt.cmdloop('Starting prompt...')
