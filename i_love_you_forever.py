import matplotlib.pyplot as plt
import numpy as np

# Create the heart shape
t = np.linspace(0, 2 * np.pi, 500)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot the heart
plt.figure(figsize=(6, 6))
plt.fill(x, y, "red")

# Add text inside the heart
plt.text(0, -1, "I LOVE YOU FOR EVER", 
         fontsize=16, fontweight="bold",
         color="white", ha="center", va="center")

# Remove axes
plt.axis("off")
plt.show()
