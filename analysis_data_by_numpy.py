'''
Based on some statical analysis of historical data, we might come up with reasonable values for the weights w1, w2, and w3.
Here's an example set of values:
w1, w2, w3 = 0.3, 0.2, 0.5
Given some climate data for a region, we can now predict the yield of apples. Here's some sample data:
Region      temp    rainfall    humidity
kanto       73          67          43
johto       91          88          64
hoenn       87          134         58
sinnoh      102         43          37
unova       69          96          70
To begin, we can define some variables to record climate data for a region.
'''
w1, w2, w3 = 0.3, 0.2, 0.5
kanto_temp=73
kanto_rainfall=67
kanto_humidity=43
kanto_yield_apples=kanto_temp*w1+kanto_rainfall*w2+kanto_humidity*w3
print(kanto_yield_apples)
# For simplification by function of above method is very long code required for all region
kanto=[73,67,43]
johto=[91,88,64]
hoenn=[87,134,58]
sinnoh=[102,43,37]
unova=[69,96,70]
region=[kanto,johto,hoenn,sinnoh,unova]
weights=[w1,w2,w3]
# for r,w in zip(kanto,weights):
#     print(r,w)
# for r,w in zip(region,weights):
#     print(r,w)
def crop_yield(region,weights):
    result=0
    for r,w in zip(region,weights):
        result=result+r*w
    print(round(result,2))
crop_yield(kanto,weights)
crop_yield(johto,weights)
crop_yield(sinnoh,weights)
# By numpy library analysis of data
import numpy as np
kanto=np.array([73,67,43])
weights=np.array([0.3,0.2,0.5])
# np.dot() -function use for dot product
# .sum() - use add
kanto_yeild_apple1=np.dot(kanto,weights)
print(kanto_yeild_apple1)
print((kanto*weights).sum())
# Python list
arr1=list(range(100000))
arr2=list(range(100000,200000))
# 1D array also called vector in mathematical terms
arr1_np=np.array(arr1)
arr2_np=np.array(arr2)
#print(arr1)
result=0
for x,y in zip(arr1,arr2):
    result=result+x*y
print(result)
print(np.dot(arr1_np,arr2_np))
print(arr1_np @ arr2_np)
# 2D array it is also call matrix
arr_2d=np.array([[73,67,43],[91,88,64],[87,134,58],[102,43,37],[69,96,70]])
print(arr_2d)
print(arr_2d.shape)
print(weights)
# 3D array..
arr_3d=np.array([[[11,12,13],[13,14,15]],[[15,16,17],[17,18,19]]])
print(type(arr_3d))
print(arr_3d.dtype)#Check the data type of an array using .dtype property
print(arr_3d.shape)
print(np.matmul(arr_2d,weights))# np.matmul()- numpy function for 2d matrix multiplicatrion also use @ at place of np.matmul()
print(arr_2d @ weights)# Matrix multiplication for 2D
print(arr_3d @ weights)# matrix multiplication for 3D
print(np.matmul(arr_3d,weights))