#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import cluster
from random import randint as rand

def distance(point,centroid):
    sum = 0
    for i in range(len(point) - 1):
        sum += (centroid[i] - point[i]) ** 2
    return np.sqrt(sum)

def plotData():
    pValues = np.array(values)
    plt.scatter(pValues[:, 0], pValues[:, 1], c = pValues[:, 2])
    plt.show()

fileName = sys.argv[1]
k = int(sys.argv[2])
fin = open(fileName,'r')
out = fileName.split('.')
outName = out[0] + '-output.txt'
fout = open(outName,'w')
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

centroids = []
# randomly selecting centroids from the data set
for i in range(k):
    element = rand(0, len(values) - 1)
    while values[element] in centroids:
        element = rand(0, len(values) - 1)
    centroids.append(values[element])
    del i
    del element

for i in range(len(values)):
    values[i].append(0)

changed = True

while changed:
    for i in range(len(values)):
        dist = 10000000
        loc = 0
        for j in range(k):
            dist1 = distance(values[i],centroids[j])
            if dist1 < dist:
                dist = dist1
                loc = j
        if values[i][-1] != loc:
            values[i][-1] = loc
            changed = True
        else:
            changed = False
        del j
    del i
    for i in range(k):
        sum = [0] * k
        inThis = 0
        for j in range(len(values)):
            if values[j][-1] == i:
                inThis += 1
                for n in range(k):
                    sum[n] += values[j][n]
        for j in range(len(sum)):
            sum[j] /= inThis
        centroids[i] = sum
    del i

outdata = ''

for i in range(len(values)):
    for j in range(len(values[i])):
        if j == len(values[i]) - 1:
            outdata += str(values[i][j]) + '\n'
        else:
            outdata += str(values[i][j]) + ' '

fout.write(outdata)

plotData()
