#!/usr/bin/python
import sys
import numpy as np

def distance(point,centroid):
    sum = 0
    for i in range(len(point)):
        sum += (centroid[i] - point[i]) ** 2
    return np.sqrt(sum)

fileName = sys.argv[1]
k = int(sys.argv[2])
fin = open(fileName,'r')
out = fileName.split('.')
outName = out[0] + '-output.txt'
del out

values = []

for line in fin:
    line = line.strip('\n')
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    values.append(line)
    del i
    del line

centroids = [[0] * len(values[0])] * k
print 'stuff'
