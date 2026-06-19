import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


a = np.random.rand(2,2)
print(a)

a = np.random.randint(0,5,size=5) #1d array
print(a)

a = np.random.randint(0,5, size=(2,3)) # 2 d array
print(a)

a = np.random.randint(5,15, size=(2,2,4)) # 3d array
print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)

#Normal (Gaussian) Distribution
#generates one random value using default parameters loc=0 and scale=1.
a = np.random.normal()
print(a)

a = np.random.normal(size=5) # create 1D array of 5 random numbers
print(a)

# generate (2,3) matrix with mean(loc)=10 and std(scale)=2

a = np.random.normal(loc=10, scale=2, size=(2,3))
print(a)

#Visualizing the Normal Distribution
# Generate data
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot histogram
plt.hist(data, bins=30, edgecolor='black', density=True)

# Plot theoretical PDF
x = np.linspace(-4, 4, 200)
pdf = norm.pdf(x, loc=0, scale=1)
plt.plot(x, pdf, label="Theoretical PDF")

plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.legend()
plt.show()