import matplotlib.pyplot as plt
import numpy as np
import time
from planning import a_star

rows, cols = 10, 10
grid = np.zeros((rows, cols))

# Static obstacles
static_obstacles = [(2, 3), (3, 3), (4, 3), (5, 5)]
for r, c in static_obstacles:
    grid[r, c] = 1

start = (0, 0)
goal = (9, 9)

vehicle_speed = 1.0  # moves per second

def plot_vehicle(grid, path, current_index):
    display_grid = np.copy(grid)
    for r, c in path:
        display_grid[r, c] = 0.5
    display_grid[start[0], start[1]] = 0.7
    display_grid[goal[0], goal[1]] = 0.9
    pos = path[current_index]
    display_grid[pos[0], pos[1]] = 0.3

    plt.clf()
    plt.imshow(display_grid, cmap='Greys', origin='upper')
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(True)
    plt.title("Vehicle Movement with Sensors")
    plt.pause(0.001)

def sensor_detect(grid, position):
    # Check the 4 adjacent cells for obstacles
    r, c = position
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr, nc] == 1:
                return True  # obstacle detected
    return False

if __name__ == "__main__":
    path = a_star(start, goal)
    if not path:
        print("No path found")
        exit()

    plt.figure()
    current_index = 0

    while current_index < len(path):
        pos = path[current_index]
        if sensor_detect(grid, pos):
            print(f"Obstacle detected near {pos}. Stopping and replanning.")
            new_path = a_star(pos, goal)
            if not new_path:
                print("No alternate path found. Stopping.")
                break
            else:
                path = new_path
                current_index = 0
                continue

        plot_vehicle(grid, path, current_index)
        time.sleep(1.0 / vehicle_speed)
        current_index += 1

    plt.show()
