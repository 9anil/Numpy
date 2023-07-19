import numpy as np
climate_data=np.genfromtxt('climate.txt',delimiter=',', skip_header=1)
print(climate_data)
print(climate_data.shape)
weights=np.array([0.3,0.2,0.5])
print(weights)
yields1=np.dot(climate_data,weights) # .dot() - dot product of array,matrix
print("Yields1=",yields1)
print(yields1.shape)
yields2=np.matmul(climate_data,weights) # .matmul() - for matrix multiplication
print("yields2=",yields2)
yields3=climate_data @ weights # @ - for matrix multiplication
print("yields3=",yields3)
# np.cocatente() - use for concatenate two or more
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9]])
print(np.concatenate((a,b))) # it add a array and b array, b array data added at end of array a as more rows. column same
a1=np.array([[1,2,3],[4,5,6]])
b1=np.array([[7,8,9,10],[1,2,3,4]])
print(np.concatenate((a1,b1),axis=1)) # it add the column b1 array after a1 array,dimension required same
# Now concatenate climate _data and yields
print(climate_data.shape)
print(yields2.shape)
new_yields=yields2.reshape(10000,1)
climate_result=np.concatenate((climate_data,new_yields),axis=1) # axis=0 for rows and axis=1 for column
print(climate_result)
np.savetxt('climate_result.txt',climate_result,fmt='%.2f',delimiter=',',
           header='Temperature, Rainfall, Humidity, Yield_apples',comments=" ")
