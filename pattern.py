#! /usr/bin/env python

import argparse, sys

def createPattern(size):
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
	return pattern

def findOffsetInPattern(pat,args={}):
	
	mspattern = createPattern(sys.argv[3])
	if pat in mspattern:
		p = mspattern.index(pat)
		print "pattern offset is %s" %p

def main():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("-c", "--create" , help=" size of create pattern",type=int)
	parser.add_argument("-q", "--query", nargs=2 , help="""find pattern offset usage: -q pattern  size""",   type=str )
	args = parser.parse_args()
	
	if len(sys.argv[1:])==0 :
		parser.print_help();
	if args.create:
		a = createPattern(sys.argv[2]);
		print a;
	elif args.query:
		findOffsetInPattern(sys.argv[2],sys.argv[3]);

if __name__ =="__main__":
	main();