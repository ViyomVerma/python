import numpy as np
import matplotlib.pyplot as plt

x = np.array([90, 75, 80, 65])
name = ["Python", "Java", "React", "C"]

# Use a colormap for better color scheme
colors = plt.get_cmap('coolwarm')(np.linspace(0.2, 0.8, len(x)))

# Explode the slices to emphasize all of them a bit
explode = (0.1, 0.05, 0.05, 0.05)

# Create the pie chart with enhanced styling
plt.pie(x, labels=name, colors=colors, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 12},
        wedgeprops={'edgecolor': 'black', 'linewidth': 1.5, 'antialiased': True})

# Add a legend outside the chart
plt.legend(name, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=12)

# Add a title
plt.title("MY BEAUTIFUL PIE CHART", fontsize=18, fontweight='bold')

# Adjust the layout so the legend doesn’t overlap the pie chart
plt.tight_layout()

# Display the chart
plt.show()




'''# Colormap: plt.get_cmap('coolwarm') is used to generate smooth gradient colors
               for the slices, giving the chart a modern, polished look.

# Explosion for All Slices: All slices have a slight explosion effect (explode) to 
                           give a dynamic feel, with Python's slice being emphasized more.

# Smooth Edges: wedgeprops are used to create smooth and sharp edges with an outline.

# Legend Position: The legend is moved outside the pie chart to avoid clutter, making the chart more readable.

# Shadow and Start Angle: The shadow remains for a 3D effect, and the chart starts from the top (90 degrees).

# Tight Layout: plt.tight_layout() ensures everything fits well without overlap.

# This version will result in a more refined and professional pie chart'''