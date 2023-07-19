import numpy as np
# Example- arithmatic operations
arr1=np.array([[1,2,3,4],[5,6,7,8]])
arr2=np.array([[2,3,4,5],[6,7,8,9]])
print(arr1+5)
print(arr1+arr2)
print(arr1*arr2)
print(arr2-arr1)
print(np.round(arr2/3,2))
print(arr1%2)
'''Example- Broadcasting- which allow arthmatic opration between two array having a different number of
dimension but compatible shape '''
arr3=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,1,2,3]])
print(arr3.shape)
arr4=np.array([4,5,6,7])
print(arr4.shape)
print(arr3+arr4)
#Example
arr5=np.array([[[1,2],[3,4],[5,6]],
               [[7,8],[9,1],[2,3]]])
print(arr5.shape)
arr6=np.array([5,6])
print(arr6.shape)
print(arr5+arr6)
arr7=np.array([[5,6],[7,8],[9,1]])
print(arr7.shape)
print(arr5+arr7)
# Comparison operations
arr8=np.array([[2,5,4],[3,2,4]])
arr9=np.array([[2,4,6],[3,5,4]])
print(arr8==arr9)
print((arr8==arr9).sum()) # True=1 and False=0 it returns sum of True and False
print(arr8>arr9)
print(arr8<arr9)
# Indexin and slicing...
print(arr1[0][2]) # 2D array
print(arr2[1,3])# 2D array
print(arr1[1:,1:3])
print(arr1[0,0:3])
arr10=np.array([[[11,12,13,14],[13,14,15,19]],
               [[20,30,40,50],[21,22,23,24]],
               [[45,46,47,48],[50,55,56,57]]])
print(arr10.shape)
print(arr10[1,1,2]) # 3D array
print(arr10[1][1][2]) #3D array
print(arr10[1:,1:,2:])
print(arr10[0:2,0,2])
# Other ways of creating array
zero_arr=np.zeros([2,3])# zeros() function gives all array value zero with given dimention
print(zero_arr)
zero_arr_3d=np.zeros((2,2,3))
print(zero_arr_3d)
one_arr=np.ones([3,3]) # All value one in given dimension of array
print((one_arr))
identity_mat=np.eye(3,3) # an identity matrix
print(identity_mat)
full_arr=np.full([3,4],20) # Full from a fixed value
print(full_arr)
arange_arr=np.arange(2,20,2) #range with start end and step
print(arange_arr)
random_arr=np.random.rand(4,3) # value between 0 to 1, in specified dimension
print(random_arr)
print(np.random.rand(2,2,2))
print(np.round(random_arr,1))
rand_int=np.random.randint(1,10,17) # ranger start and end(exclusive) points and number of element
print(rand_int)
linspace_arr=np.linspace(5,4,20) # ranger start and end(both inclusive) points and number of element
print(linspace_arr)