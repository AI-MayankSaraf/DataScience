import numpy as np
print("Numpy vesion is: ", np.__version__)

# NumPy Creating Arrays

# 0-D Arrays
arr0 =  np.array(42)
print("0-D Arrays is: ", arr0)

# 1-D Arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("1-D Arrays is: ")
print(arr1)

# 2-D Arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Arrays is: ")
print(arr2)

# 3-D Arrays
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3-D Arrays is: ")
print(arr3)

print("Dimension for 0-D arrays is: ", arr0.ndim)
print("Dimension for 1-D arrays is: ", arr1.ndim)
print("Dimension for 2-D arrays is: ", arr2.ndim)
print("Dimension for 3-D arrays is: ", arr3.ndim)

print("Type of array is: ", type(arr0))

# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('Number of dimensions :', arr.ndim)

# NumPy Array Indexing
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[2] + arr[3])

# Access 2-D Arrays
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) #6

# Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# NumPy Array Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::])
print(arr[::2])
print()
# Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])

# NumPy Data Types
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# A non integer string like 'a' can not be converted to integer (will raise an error):
# arr = np.array(['a', '2', '3'], dtype='i') 

# Converting Data Type on Existing Arrays
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# NumPy Array Copy vs View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
# Copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# View
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Make Changes in the VIEW
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# Check if Array Owns its Data
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)







