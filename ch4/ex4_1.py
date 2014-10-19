# IPython log file

get_ipython().magic(u'logstart')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import expovariate
def get_intervals(times):
    intervals = []
    last_time = 0
    for i in times:
        if last_time==0:
            intervals.append(i)
        else:
            intervals.append(i - last_time)
        last_time = i
    return intervals

babyboom = pd.read_csv('/home/dean/Downloads/babyboom.tsv', sep='\t', names=['time','sex','weight','minutes'])
intervals = get_intervals(babyboom['minutes'])
sorted_intervals = np.sort(intervals)
yvals=np.arange(len(sorted_intervals))/float(len(sorted_intervals))
plt.plot(sorted_intervals, yvals)
plt.yscale('log')
plt.show()
ccdf_yvals = [1 - yval for yval in yvals]
plt.plot(sorted_intervals, ccdf_yvals, drawstyle='steps')
plt.yscale('log')
plt.show()
lmbda = 1/32.6
x = [expovariate(lmbda) for _ in range(0, 44)]
sorted_x = np.sort(x)
plt.plot(sorted_x, ccdf_yvals, drawstyle='steps')
plt.yscale('log')
plt.show()
plt.show()
exit()
