# pandas = dataset represent
import numpy as np   #dataset code
import pandas as pd  #dataset represent
import matplotlib.pyplot as plt #graphically data represent

years = np.array([2020,2021,2022,2026])
grade = np.array([94.6,70.3,74.9,81.3])

plt.plot(years,grade,marker= 'o')
plt.title("MY ACDEMIC GRADES")
plt.xlabel("years")
plt.ylabel("grades")
plt.grid()
plt.show()

x=np.array([90,75,80,65])
name=["python","java","react","c"]
plt.pie(x)
plt.legend(name)
plt.title("MY PIE CHART")
plt.show()
