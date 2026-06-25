import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# normal histogram
""" data = np.random.normal(10,3,500)
sns.displot(data, kde=True, bins=10, color='black')
plt.show() """

#Bimodal Histogram
N=400
m1, std1=80,10
m2, std2=20,10

# Generate two normal dis for given mean and std
""" data1 = np.random.normal(m1,std1,N)
data2 = np.random.normal(m2,std2,N)
data = np.concatenate([data1,data2])

sns.displot(data, kde=True, bins=10, color='green')
plt.show() """

# Right skewed histogram

""" data = [0] *10 + [1]*50 + [2]*80 + [3]*60 + [4]*40 +[5]*20+[6]*5
sns.displot(data, bins=7, kde=True, color='blue')
plt.show() """

# Left skewed histogram

""" data = [0]*5+ [1]*20+[2]*40+[3]*60+[4]*100+[5]*80+[6]*95
sns.displot(data, kde=True, bins=7, color='red')
plt.show() """

# Uniform histogram
#generate random data using uniform distribution
""" data = np.random.uniform(low=0,high=1, size=600)
sns.histplot(data, kde=True, bins=10)
plt.show() """

# Normal distribution with Outlier

x = np.random.normal(80,10,600)
data = np.concatenate([x, [200]*30])
sns.displot(data, kde=True, bins=15)
plt.show()

