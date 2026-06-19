import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

res = np.add(a,b)
print("Addition: ", res)

res = np.subtract(b,a)
print("Substraction: ",res)

res = np.multiply(a,b)
print("Multiply: ",res)

res = np.divide(b,a)
print("Division: ",res)

res = np.mod(b,a)
print("Modulo: ", res)

res = np.power(a,b)
print("Power value: ",res)

res = np.dot(a,b)
print("Matrix product: ",res)

res = np.sum(a)
print("Sum: ",res)


arr = np.array([ [14, 17, 12, 33, 44],
               [15,  6, 27,  8, 19],
               [23,  2, 54,  1,  4] ])

print("Sum: ", np.sum(arr))
print("Sum columns: ", np.sum(arr, axis=0))
print("Sum rows: ", np.sum(arr, axis=1))
print("Sum rows, output in cols: ", np.sum(arr, axis=1, keepdims=True))


# mean
arr = [20, 2, 7, 1, 34]
print("Mean: ", np.mean(arr))

arr = [[14, 17, 12],
       [15,  6, 27],
       [23,  2, 54]]
print("Mean: ", np.mean(arr))
print("Mean row value: ", np.mean(arr, axis=1))
print("Mean col value: ", np.mean(arr, axis=0))

arr = [[5, 10, 15],
       [3,  6,  9],
       [8, 16, 24]]


res=np.mean(arr, axis=1)
print(res)

# max
a = np.array([2, 8, 125])
b = np.array([3, 3, 15])
print("Max value in a: ", np.max(a))
print(np.maximum(a,b))

a = np.array([[1, 4, 7], [2, 5, 8], [2,3,5]])
b = np.array([3, 3, 3])
print(np.maximum(a, b))

#min
a = np.array([2, 8, 125])
b = np.array([3, 3, 15])
print(np.minimum(a, b))


a = np.array([[4, 7, 9], [1, 5, 8]])
b = np.array([3, 6, 10])
print(np.minimum(a, b))

# Statistical functions
w = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])
print("Min: ", np.min(w))
print("Max: ", np.max(w))
print("Range: ", np.max(w) - np.min(w))
print("Range: ", np.ptp(w))
print("70th percentile: ", np.percentile(w,70))
print("Mean: ", np.mean(w))
print("Median:", np.median(w))
print("Std:", np.std(w))
print("variance: ", np.var(w))
print("Avg:", np.average(w))

# Multiplication
x = [[1, 2], [2, 3], [4, 5]]
y = [[4, 5, 1], [6, 7, 2]]

z = np.dot(x,y)
print("REsult :", z)

# Matrix functions
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

print("Square root: ", np.sqrt(x))
print("Sum of all element",np.sum(y))
print("Column wise sum: ", np.sum(y, axis=0))
print("Row wise sum: " , np.sum(y, axis=1))
print("Transpose: ", y.T)

# Define vectors
a = np.array([2, 6])
b = np.array([3, 10])

print("Inner product of vectors a and b =")
print(np.inner(a, b))
print(np.multiply(a,b))

# Define matrices
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])

print("Inner product of matrices x and y =")
print(np.inner(x, y))
print(np.multiply(x,y))

# Define vectors
a = np.array([2, 6])
b = np.array([3, 10])

print("Outer product of vectors a and b =")
print(np.outer(a, b))

# Define matrices
x = np.array([[3, 6, 4], [9, 4, 6]])
y = np.array([[1, 15, 7], [3, 10, 8]])

print("Outer product of matrices x and y =")
print(np.outer(x, y))