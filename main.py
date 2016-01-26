import matplotlib.pyplot as plt
import random
import time
import matplotlib.patches as patch
import math

size = [5,10,50,100,500,1000,5000,10000]
sortable = []
points = []
logs = []
tempTimes = []
for n in range(1,size.__len__()+1):
    for x in range(10):
        t1 = time.time()
        for x in range(size[n-1]):
            sortable.append(random.seed())
        sortable.sort()
        t2 = time.time()
        tempTimes.append(t2-t1)
    logs.append(n*math.log(n,2))
    points.append(sum(tempTimes)/20)

redPatch = patch.Patch(color='red', label='Sort Time')
bluePatch = patch.Patch(color='blue', label='n(lg(n))')
plt.legend(handles=[redPatch, bluePatch], loc=2)
plt.plot(points, 'r', logs, 'b')
plt.ylabel('time in seconds')
plt.show()