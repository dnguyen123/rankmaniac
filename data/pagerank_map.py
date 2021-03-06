#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    node = int(line[line.find(':')+1:line.find('\t')])

    rank1_index = line.find(',')
    rank1 = float(line[line.find('\t')+1:rank1_index])

    rank2_index = line.find(',', rank1_index+1)
    rank2 = float(line[rank1_index+1:rank2_index])

    # No outlinks
    if rank2_index == -1:
        sys.stdout.write(str(node)+'\t'+str(rank1)+'\n')
        continue

    sys.stdout.write(str(node)+'\t'+str(0.0)+'\n')

    outlinks = line[rank2_index+1:-1].split(',')
    outlinks = [int(i) for i in outlinks]

    for link in outlinks:
        sys.stdout.write(str(link)+'\t'+str(rank1/len(outlinks))+'\n')

