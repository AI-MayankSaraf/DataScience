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







