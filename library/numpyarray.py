'''It is used to work on large data set 
   reasons:- 
      * Range is too large.
      * High order function.
      * Array reshape.
      * Create N dimensional array'''

# How to use numpy in python:-  goto terminal -> pip install numpy

import numpy as np
#assign array in numpy

myData =np.array([1,2,3,4])
print(myData)
print(type(myData))

myData[0]=9
myData[1]=10
myData[2]=11
myData[3]=12
print(myData)

print("Using for loop")
y=9
for i in range(0,4):
    myData[i]=y   # myData[i]=y+i
    y=y+1
print(myData)

print("printing data from 12 to 9 using while loop")

i=0
a=12
while i<4:
    myData[i]=a
    a=a-1
    i=i+1
print(myData)

#access the data from numpy array
for data in range(0,4):
    print(myData[data])

#accessing the names 
print("accessing the names ")
myfriends=np.array(["viyom","anish","nihal","sakshi","amiti","bishu"])
for name in myfriends:
    print(name)

#reversing the names using while loop
print("reversing the names")
i=5
while i>=0:
    print(myfriends[i])
    i=i-1

#sorting the data
myfriends.sort()
print(myfriends)
