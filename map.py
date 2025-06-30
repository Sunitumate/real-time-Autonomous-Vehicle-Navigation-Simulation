import matplotlib.pyplot as plt
import numpy as np

# Grid size (rows x cols)
rows, cols = 10, 10

# Create a grid initialized with zeros (0 = free space)
grid = np.zeros((rows, cols))

# Mark some obstacles (1 = obstacle)
obstacles = [(2, 3), (3, 3), (4, 3), (5, 5), (6, 7), (7, 7)]
for r, c in obstacles:
    grid[r, c] = 1

def plot_grid(grid):
    plt.imshow(grid, cmap='Greys', origin='upper')
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(True)
    plt.title("2D Grid Map with Obstacles")
    plt.show()

if __name__ == "__main__":
    plot_grid(grid)
