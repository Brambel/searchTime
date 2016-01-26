import matplotlib.pyplot as plt
import random
import time
import math

size = [5,10,50,100,500,1000,5000,10000]
sortable = []
points = []
logs = []
for n in range(size.__len__()):
    t1 = time.time()
    for x in range(size[n]):
        sortable.append(random.seed())
    sortable.sort()
    t2 = time.time()
    logs.append(n*n)
    points.append(t2-t1)


plt.plot(points, 'r', logs, 'b')
plt.ylabel('some num')
plt.show()