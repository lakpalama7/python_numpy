import numpy_learning as np

arr = np.array([1,2,3,4,5])
print(arr)

print(np.__version__)

print(type(arr))

arr2 = np.array(('a','b','c'))
print(arr2)

#0-D array
arr3=np.array(42)
print(arr3)
print(arr3.ndim)

#1-D array
arra4=np.array([1,2,3,4,5])
print(arra4)
print(arra4.ndim)

#2-D array
arr5=np.array([[1,2,3,3,4],[5,6,7,8,9]])
print(arr5)
print(arr5.ndim)

#3-D array
arr6=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr6)
print(arr6.ndim)

#n-D array

arr7 = np.array([1,2,3,4,5], ndmin=5)
print(arr7)
print(arr7.ndim)

#5-D array
arr8 = np.array([[[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]],[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]]],[[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]],[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]]]])
print(arr8)
print(arr8.ndim)



#Array indexing

arr = np.array([1,2,3,4])
print(arr[0])
print(arr[3])
print(arr[1] + arr[3])

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2[0,3])
print(arr2[1,1])

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3[1,0,2])
print(arr3[1,1,-3])

#numpy array slicing

arr = np.array([1,2,3,4,5])
print(arr[1:4])
print(arr[3:])
print(arr[:5])
print(arr[:])
print(arr[-3:-1])
print(arr[:-1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
print(arr[::2])


#2-D array slicing
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])
print(arr[0, :2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
print(arr[0:2, 1:4])


#Numpy datatypes

arr = np.array([1,2,3])
print(arr.dtype)

arr = np.array(["apple","banana","cherry"])
print(arr.dtype)

#defned data type
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

#Convert datatypes on existing arrays
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
intarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
print(intarr)
print(intarr.dtype)


arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


#copy and view of array
print("copy and view")

#copy creates new array any changes on it, do not affect on original array
arr = np.array([1,2,3,4,5])
a = arr.copy()
print(arr)
print(a)
arr[0]=100
print(arr)
print(a)
a[2]=300
print(arr)
print(a)

print("view array")
#any changes on view array affect on original array or vice versa
arr = np.array([1,2,3,4,5])
a = arr.view()
print(arr)
print(a)
#change on original array
arr[0]=100
print("original: ", arr)
print("view : ", a)

#change on view array
a[4]=500
print("original : ", arr)
print("view : ", a)

#check array owns data
print("check array owns data")
arr = np.array([1, 2, 3, 4, 5])
x=arr.copy()
y=arr.view()
#base -> return NOne if it owns data else it return original object
print(x.base)
print(y.base)

#numpy array shape
print("numpy array shape")

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)
arr = np.array([1,2,3])
print(arr.shape)

arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print("shape of array: ", arr.shape)

#numpy array reshaping
print("numpy reshaping array from 1D to 2D")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr=arr.reshape(4,3)
print(newarr)
newarr=arr.reshape(3,4)
print(newarr)

print("reshaping array from 1D to 3D")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr=arr.reshape(3,2,2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.shape)
newarr= arr.reshape(2,4)
print(newarr.base) #return original array so it is a view


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

print("multidimension reshare to 1D array")
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)


#Numpy for loop
print("For loop in array: ")
arr=np.array([1,2,3,4,5])

for x in arr:
    print(x)

print("Iterating 2D array")

arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
        print(x)

print("Iterating 3D array:")
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for i in y:
            print(i)
    

print("Iterating array using nditer()")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
     print(x)

print("Iterating array with different data types")

arr=np.array([1,2,3,4])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
     print(x)

print("Iterating with diff step size")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)


print("Enumerated Iteration usind ndenumerate") #index and value

arr = np.array([1,2,3,4])

for i,v in np.ndenumerate(arr):
     print(f"index: {i}, value: {v}")


print("Joining Numpy arrays") # Join two array by axes
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1,arr2))
print(arr)


print("Join two 2-D arrays along rows (axis=1):")
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
arr=np.concatenate((arr1,arr2), axis=1)
print(arr)

print("Joining Arrays Using Stack Functions")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)


print("Stacking Along Rows")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)


print("Stacking Along Columns")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

print("Stacking Along Height (depth)")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)