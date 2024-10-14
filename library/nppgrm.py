# x=np..array([1,7,8,11,9,3,2])
# find mean,median,,mode,sort the data
import numpy as np
x=np.array([1,3,5,7,10,45,2,4])
y=np.array([9,8,12,30,50,44,2,1])

print("the mean of the data is =",x.mean())
print("the minimum value is =",x.min())
print("the maximum value is =",x.max())
x.sort()
print(x)

for i in x:   #accessing data from the data
    print(i) 

# Array slicing
print(x[0:8])
print(x[2:8])
print(x[2:])
print(x[:7])
print(x[-5:-1])


#shape,reshape
print(x.shape)

mydata=x.reshape(2,4)
print(mydata)

z=x+y
print(z)