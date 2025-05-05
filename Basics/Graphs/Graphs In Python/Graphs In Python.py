# By Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# Date: 18-04-2025

import matplotlib.pyplot as plt

# Data
distances = [0, 0.5, 0.8, 1, 1.1]  # 1.1 used for ">1cm"
values = [0, 61, 68, 70, 76] # Sensor values for each distance

# Plot
plt.figure(figsize=(6,4)) # Set figure size
plt.plot(distances, values, marker='o', linestyle='-') # Line plot with markers
plt.xlabel('Distance (cm)') # X-axis label
plt.ylabel('Sensor Value') # Y-axis label
plt.title('Capacitive Sensor Calibration') # Plot title
plt.grid(True) # Show grid
plt.show() # Show plot