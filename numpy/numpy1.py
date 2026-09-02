import numpy as np

arr  = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(np.ndim(arr))

# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)
# print(np.ndim(arr2))

# arr4 = np.zeroes((1,4))
# print(arr4)

arr5 = np.zeros(3)
print(arr5)

arr3 = np.zeros((3,1))
print(arr3)
print(np.ndim(arr3))

arr6 = np.ones((2,3))
print(arr6)
print(np.ndim(arr6))

arr7 = np.arange(1,1000,3)
print(arr7)