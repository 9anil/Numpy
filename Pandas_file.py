# Pandas: Loading and reading dataset use for analysing the data,creating the structure of dummy dataset.
import numpy as np
import pandas as pd
data1=pd.DataFrame(np.arange(0,25).reshape(5,5),index=['R0','R1','R2','R3','R4'],columns=['C0','C1','C2','C3','C4'])
print(data1)
data1.to_csv("data1.csv")
data2=pd.DataFrame(np.linspace(2,9,20).reshape(4,5),index=['R0','R1','R2','R3'],columns=['C0','C1','C2','C3','C4'])
print(data2)
data2.to_excel("data2.xlsx")
data3=pd.DataFrame(np.random.rand(5,5),index=['R0','R1','R2','R3','R4'],columns=['C0','C1','C2','C3','C4'])
print(data3)
data3.to_excel("data3.xlsx")
data4=pd.DataFrame(np.random.randint(1,9,25).reshape(5,5),index=['R0','R1','R2','R3','R4'],columns=['C0','C1','C2','C3','C4'])
print(data4)
data4.to_csv("data4.csv")
# iloc()- Use for indexing and slicing in pandas.
print("data4[0][0]=",data4.iloc[0][0],"data4[4][3]=",data4.iloc[4][3],"data4[-3][-3]=",data4.iloc[-3][-3])
print("data4[1:,2:]=",data4.iloc[1:,2:])
data5=pd.read_csv("Book1.csv")
print(data5.head())# head(): select 5rows from top of the table.
print(data5.tail())#tail(): Select 4rows from tail of the table.
print(data5.head(10))# 10rows from the top of the table.
print(data5.info())
print(data5.describe())
