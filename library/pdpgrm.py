import pandas as pd
import numpy as np

x=np.array([1,2,3,4,5])
mydataframe=pd.DataFrame(x)
print(mydataframe)

mydata=pd.DataFrame(data=np.arange(0,100).reshape(10,10))
print(mydata,"\n\n\n")

print("to print the head of the data and print top 5 rows ")
print(mydata.head(7),"\n\n\n")

print("to print the tail of the data and print bottom 5 rows")
print(mydata.tail(),"\n\n\n")

empsalary=pd.DataFrame(data=np.arange(0,100).reshape(10,10))
print(empsalary+1000,"\n\n\n")

print(mydata.describe(),"\n\n\n")
print(mydata.mean(),"\n\n\n")
print(mydata.median(),"\n\n\n")
print(mydata.mode(),"\n\n\n")
print(mydata.loc[[0,3]],"\n\n\n") #print data in no. of rows

print("to print the last row ")
print(mydata.loc[[9,]],"\n\n\n")

print("to print the last two row ")
print(mydata.loc[[8,9]],"\n\n\n")

print(mydata.loc[[]],"\n\n\n")