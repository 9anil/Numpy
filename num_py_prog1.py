# numpy:- Stands for numerical python use for numerical data analysis
import numpy as np
# One dimensional array-
list1=[1,3,45,67,34.78,99.45,77,93,92,12]
list2=[10,31,43,15,22,78,101,302,500,45,0]
list3=["India",23,56,89,0,4,5,67,90]
arr1=np.array(list1)
print("<-----------*Print a one dimensional array*----------------------->")
print(arr1)
arr2=np.array(list2)
print(arr2)
arr3=np.array(list3)
print(arr3)# Print array with string datatype
print(type(arr3))
print("<--------------------------*Two dimensional array*------------------------>")
l1=[30,41,51,63,70,95,12,56,5]
l2=[90,30,40,58,79,12,34,10,7]
l3=[23,45,71,56,89,23,51,77,85]
arr4=np.array((l1,l2,l3))
print(arr4)
print(arr4.shape)#Show the shape of array in for of(x,y): x-is the number of rows and y-is the number of columns
# reshape(): use for reshape the array with some limitation
print(arr4.reshape(9,3))
# Indexing and Slicing in array one and two dimension array..
print("arr1[0]=",arr1[0],"arr1[3]=",arr1[3],"arr1[6]=",arr1[6],"arr1[-2]=",arr1[-2],"arr1[-5]=",arr1[-5])
print("arr2[1:4]=",arr2[1:4])
print("arr2[::-1]=",arr2[::-1])
print("arr2[-1:-4:-1]=",arr2[-1:-4:-1])
print("arr4[0][5]=",arr4[0][5],"arr4[1][7]=",arr4[1][7],"arr4[2][3]=",arr4[2][3])
print("arr4[1:,4:]=",arr4[1:,4:])
print("arr4[0:2,1:5]=",arr4[0:2,1:5])
# arange(): use for generate random number in a given range, arange(x,y,z): x-inclusive,y-exclusive,z-step size
arr5=np.arange(0,10)
print(arr5)
# linspace(): give the desire output in a given range, linspace(x,y,z)- x and y inclusive,z-number of elements equally
arr6=np.linspace(1,20,15)
print(arr6)
# random.rand(): it accepts two parameter row and column,its default range 0 to 1 while 1 is exclusive.
arr7=np.random.rand(3,4)
print(arr7)
#random.randint(): It give the integer value in a give range it allows three parameter (x,y,z) where x-inclusive,y-exclusive and z- is the number of elements
arr8=np.random.randint(2,8,20)
print(arr8)