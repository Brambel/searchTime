import matplotlib.pyplot as plt
import random
import time
import matplotlib.patches as patch

size = [5,10,50,100,500,1000]
sortable = []
points = []
logs = []
tempTimes = []
for n in range(size.__len__()):
    t1 = time.time()
    for x in range(20):
        for x in range(size[n]):
            sortable.append(random.seed())
        sortable.sort()
        t2 = time.time()
        tempTimes.append(t2-t1)
    logs.append(n*n)
    points.append(sum(tempTimes)/20)
redPatch = patch.Patch(color='red', label='Sort Time')
bluePatch = patch.Patch(color='blue', label='n^2')
plt.legend(handles=[redPatch, bluePatch], loc=2)
plt.plot(points, 'r', logs, 'b')
plt.ylabel('some num')
plt.show()