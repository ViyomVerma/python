import numpy as np
import matplotlib.pyplot as plt

x = np.array([90, 75, 80, 65])
name = ["Python", "Java", "React", "C"]

# Define colors for the pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Explode the largest slice (Python in this case) to highlight it
explode = (0.1, 0, 0, 0)  # '0.1' means explode the first slice

# Create the pie chart with more styling
plt.pie(x, labels=name, colors=colors, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=140, textprops={'fontsize': 20})

# Add a legend
plt.legend(name, loc="best")

# Add a title
plt.title("MY ATTRACTIVE PIE CHART", fontsize=16, fontweight='bold')

# Display the chart
plt.show()