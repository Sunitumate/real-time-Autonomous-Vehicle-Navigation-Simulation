import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue

rows, cols = 10, 10

grid = np.zeros((rows, cols))

# Obstacles (1 = obstacle)
obstacles = [(2, 3), (3, 3), (4, 3), (5, 5), (6, 7), (7, 7)]
for r, c in obstacles:
    grid[r, c] = 1

start = (0, 0)  # starting point
goal = (9, 9)   # goal point

def heuristic(a, b):
    # Manhattan distance heuristic for A*
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # 4-way connectivity
    result = []
    for d in directions:
        nr, nc = node[0] + d[0], node[1] + d[1]
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr, nc] == 0:  # not obstacle
                result.append((nr, nc))
    return result

def a_star(start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for next_node in neighbors(current):
            new_cost = cost_so_far[current] + 1  # all edges cost 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    # reconstruct path
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from.get(cur)
        if cur is None:
            return []  # no path
    path.append(start)
    path.reverse()
    return path

def plot_path(grid, path):
    display_grid = np.copy(grid)
    for r, c in path:
        display_grid[r, c] = 0.5  # mark path with gray
    display_grid[start[0], start[1]] = 0.7  # start with lighter gray
    display_grid[goal[0], goal[1]] = 0.9    # goal with even lighter gray

    plt.imshow(display_grid, cmap='Greys', origin='upper')
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(True)
    plt.title("A* Path Planning")
    plt.show()

if __name__ == "__main__":
    path = a_star(start, goal)
    if path:
        print("Path found:", path)
        plot_path(grid, path)
    else:
        print("No path found")
