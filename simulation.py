import matplotlib.pyplot as plt
import numpy as np
import time

rows, cols = 10, 10

grid = np.zeros((rows, cols))

obstacles = [(2, 3), (3, 3), (4, 3), (5, 5), (6, 7), (7, 7)]
for r, c in obstacles:
    grid[r, c] = 1

start = (0, 0)
goal = (9, 9)

# For simplicity, reusing the A* function from step 2 here:
from planning import a_star

def plot_vehicle(grid, path, current_index):
    display_grid = np.copy(grid)
    for r, c in path:
        display_grid[r, c] = 0.5  # path
    display_grid[start[0], start[1]] = 0.7  # start
    display_grid[goal[0], goal[1]] = 0.9    # goal

    # Mark current vehicle position
    pos = path[current_index]
    display_grid[pos[0], pos[1]] = 0.3  # vehicle color (different shade)

    plt.clf()
    plt.imshow(display_grid, cmap='Greys', origin='upper')
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(True)
    plt.title("Vehicle Moving Simulation")
    plt.pause(0.5)

if __name__ == "__main__":
    path = a_star(start, goal)
    if not path:
        print("No path found")
    else:
        plt.figure()
        for i in range(len(path)):
            plot_vehicle(grid, path, i)
        plt.show()
