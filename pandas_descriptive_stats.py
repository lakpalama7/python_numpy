import numpy as np
import scipy.stats as stats
import statistics

# Measure of central tendency
# mean, mode, median
data = np.arange(0,10)
print(data)

# mean
m = np.mean(data)
print("Mean: ", m)


#Mode
arr = np.array([12,2,3,3,4,5,6,3,4])
mode = stats.mode(arr)
print("Mode: ", mode)

# Median
data = np.arange(5,15)
median= np.median(data)
print("Median: ", median)

# Measure of variability : how data are spreadout from the mean.
# Range, variance, std, iqr

# Range
arr = [1, 2, 3, 4, 5]
min = np.min(arr)
max = np.max(arr)
range = max - min
print(f"max: {max} and min: {min} and Range = {range}")

# Variance: 
arr = [1, 2, 3, 4, 5]
var = statistics.variance(arr)
print("Variance: ", var)

#std : square root of varianace

arr = [1, 2, 3, 4, 5]
print("STD: ", np.std(arr))
print("std: ", statistics.stdev(arr))

