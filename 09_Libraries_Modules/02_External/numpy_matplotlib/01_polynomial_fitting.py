import numpy as np
import matplotlib.pyplot as plt

# Define data
x = np.array([0, 20, 32, 46, 61, 76, 91, 106, 121, 136, 156])
y = np.array([0, -0.086, -0.427, -0.856, -0.68, -0.419, -0.253, -0.143, -0.069, -0.018, 0.002])
y1 = np.array([0, -0.114, -0.457, -0.91, -0.8, -0.686, -0.4, -0.34, -0.34, -0.229, -0.114])
y2 = np.array([0, -0.025, -0.329, -0.84, -0.734, -0.46, -0.33, -0.28, -0.203, -0.18, -0.076])
y3 = np.array([0, -0.057, -0.386, -0.885, -0.77, -0.50, -0.343, -0.257, -0.214, -0.171, -0.1428])
y4 = np.array([0, -0.045, -0.39, -0.87, -0.745, -0.5, -0.354, -0.26, -0.2, -0.16, -0.136])
y5 = np.array([0, -0.038, -0.387, -0.857, -0.724, -0.51, -0.356, -0.267, -0.21, -0.159, -0.133])

# Degree of polynomial for fitting
degree = 3  # You can change this value based on how well you want to fit the data

# Create a smooth x range for plotting the fit
x_fit = np.linspace(min(x), max(x), 100)

# Create a figure for plotting
plt.figure()
plt.grid(True)

# Function to fit and plot
def plot_fit(x, y, label, color):
    # Fit polynomial
    p = np.polyfit(x, y, degree)
    y_fit = np.polyval(p, x_fit)
    
    # Plot original data and fit
    plt.plot(x, y, 'o', label=f'Original Data ({label})', color=color)
    plt.plot(x_fit, y_fit, '--', label=f'Fit for {label}', color=color)

# Plot all datasets
plot_fit(x, y, 'y', 'blue')
plot_fit(x, y1, 'y1', 'orange')
plot_fit(x, y2, 'y2', 'green')
plot_fit(x, y3, 'y3', 'red')
plot_fit(x, y4, 'y4', 'purple')
plot_fit(x, y5, 'y5', 'cyan')

# Customize plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Combined Plot of Data Series with Curve Fitting')
plt.legend()
plt.show()