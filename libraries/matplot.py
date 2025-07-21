#  practicing matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Create a plot
plt.plot(x, y)
# Add title and labels
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# Show the plot
plt.show()
# Save the plot to a file
plt.savefig('sine_wave_plot.png')


# Multiple plots in one figure
plt.figure(figsize=(12, 8))

# Subplot 1: Line plot with multiple lines
plt.subplot(2, 3, 1)
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)', color='blue')
plt.plot(x, np.cos(x), label='cos(x)', color='red')
plt.title('Trigonometric Functions')
plt.legend()

# Subplot 2: Scatter plot
plt.subplot(2, 3, 2)
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
plt.scatter(x_scatter, y_scatter, alpha=0.6, c='green')
plt.title('Scatter Plot')

# Subplot 3: Bar chart
plt.subplot(2, 3, 3)
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
plt.bar(categories, values, color=['red', 'blue', 'green', 'orange'])
plt.title('Bar Chart')

# Subplot 4: Histogram
plt.subplot(2, 3, 4)
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=100, alpha=0.3, color='purple')
plt.title('Histogram')

# Subplot 5: Pie chart
plt.subplot(2, 3, 5)
sizes = [30, 25, 20, 25]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

# Subplot 6: Heatmap using imshow
plt.subplot(2, 3, 6)
data_2d = np.random.rand(10, 10)
plt.imshow(data_2d, cmap='viridis')
plt.colorbar()
plt.title('Heatmap')

plt.tight_layout()
plt.savefig('matplotlib_examples.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# Advanced styling example
plt.style.use('seaborn-v0_8')  # Use a built-in style

fig, ax = plt.subplots(figsize=(10, 6))

# Create data
x = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot with custom styling
ax.plot(x, y1, linewidth=2, linestyle='-', marker='o', markersize=2, 
        alpha=0.8, label='sin(x)')
ax.plot(x, y2, linewidth=2, linestyle='--', marker='s', markersize=2, 
        alpha=0.8, label='cos(x)')

# Customize axes
ax.set_xlabel('X values', fontsize=12, fontweight='bold')
ax.set_ylabel('Y values', fontsize=12, fontweight='bold')
ax.set_title('Advanced Matplotlib Styling', fontsize=14, fontweight='bold')

# Add grid and legend
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10, loc='upper right')

# Customize spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('advanced_plot.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# Annotations and text
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y)
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(2, 0.8),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=12, color='red')

ax.text(5, -0.5, 'This is a sine wave', fontsize=10, 
        bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.5))

plt.show()
plt.close()