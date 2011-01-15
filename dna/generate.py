#!/usr/bin/env python


import sys
import random

def main(dna, scores):

    print dna
    d = [random.choice('GATC') for x in xrange(dna)]
    n = int(dna / 80.0)
    for i in range(n):
        print "".join(d[(i*80):((i+1)*80)])
    rem = dna % 80
    if (rem > 0):
        print "".join(d[(n*80):(n*80)+rem])

    print scores
    for i in range(scores):
        start = int(random.uniform(0,dna-1))
        stop = int(random.uniform(start+1,dna))
        score = int(random.uniform(0,300))
        print "%d %d %d" %(start, stop, score)

if __name__ == "__main__":
    dna = int(sys.argv[1])
    scores = int(sys.argv[2])
    main(dna, scores)
