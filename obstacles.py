import matplotlib.pyplot as plt
import numpy as np
import time
import random
from planning import a_star

rows, cols = 10, 10
grid = np.zeros((rows, cols))

# Static obstacles
static_obstacles = [(2, 3), (3, 3), (4, 3), (5, 5)]
for r, c in static_obstacles:
    grid[r, c] = 1

start = (0, 0)
goal = (9, 9)

def plot_vehicle(grid, path, current_index, dyn_obstacle):
    display_grid = np.copy(grid)
    for r, c in path:
        display_grid[r, c] = 0.5
    display_grid[start[0], start[1]] = 0.7
    display_grid[goal[0], goal[1]] = 0.9
    # Vehicle position
    pos = path[current_index]
    display_grid[pos[0], pos[1]] = 0.3
    # Dynamic obstacle position
    display_grid[dyn_obstacle[0], dyn_obstacle[1]] = 1

    plt.clf()
    plt.imshow(display_grid, cmap='Greys', origin='upper')
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(True)
    plt.title("Vehicle Navigation with Dynamic Obstacle")
    plt.pause(0.5)

def move_dynamic_obstacle(current_pos):
    # Move the dynamic obstacle randomly to adjacent free cell
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    random.shuffle(directions)
    for d in directions:
        nr, nc = current_pos[0] + d[0], current_pos[1] + d[1]
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
            return (nr, nc)
    return current_pos  # no move possible

if __name__ == "__main__":
    dynamic_obstacle = (5, 6)  # initial position

    path = a_star(start, goal)
    if not path:
        print("No path found")
        exit()

    plt.figure()
    current_index = 0
    while current_index < len(path):
        vehicle_pos = path[current_index]

        # Move dynamic obstacle
        dynamic_obstacle = move_dynamic_obstacle(dynamic_obstacle)

        # Check if path is blocked ahead
        if dynamic_obstacle in path[current_index:]:
            print("Path blocked! Recalculating...")
            # Update grid for dynamic obstacle
            temp_grid = np.copy(grid)
            temp_grid[dynamic_obstacle[0], dynamic_obstacle[1]] = 1
            new_path = a_star(vehicle_pos, goal)
            if not new_path:
                print("No alternate path found. Stopping.")
                break
            else:
                path = [vehicle_pos] + new_path[1:]
                current_index = 0

        plot_vehicle(grid, path, current_index, dynamic_obstacle)
        current_index += 1

    plt.show()
