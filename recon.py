 lxml import html

def head(url):
        r = requests.get(url)
        header = r.headers
        for item, value in  header.items():
                print item+ " : " + value

def spider(url):
        r = requests.get(url)
        page = html.fromstring(r.content)
        link = page.xpath('//a/@href')
        for item in link:
                print item

def portscan(host):
        for port in range(1,1025):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                res = s.connect_ex((host,port))
                if (res ==0 ):
                        print "open {0} at {1}".format(port,host)
                s.close

def main():
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument("-H","--header", help= " show http header usage: -H http://example.com", type=str)
        parser.add_argument("-S","--spider",help="spidering usage: -S http://example.com", type=str)
        parser.add_argument("-P","--portscan",help="scanning port usage: -P IP", type=str)
        args = parser.parse_args()

        if len(sys.argv[1:])==0 :
                parser.print_help();

        if args.header:
                head(sys.argv[2]);
        if args.spider:
                spider(sys.argv[2]);
        if args.portscan:
                portscan(sys.argv[2]);

if __name__ == "__main__":
        main();
