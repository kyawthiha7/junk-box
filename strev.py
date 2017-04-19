#!/usr/bin/python

import sys

st = sys.argv[1]
revstr = st[::-1]

h = revstr.encode("hex")

o = []
while h:
	o.append(h[:8])
	h = h[8:]
for i in o:
	print i
