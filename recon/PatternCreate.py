


class Pat():
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
#        print " -------------"
#        print "file is written in pattern.txt"
#        with open('pattern.txt','w') as f:
#                print >> f, pattern


   def findOffset(pat,size):
        mspattern = createPattern(size)
        if pat in mspattern:
                p = mspattern.index(pat)
                print "pattern offset is %s " %p

