from collections import deque


def read_input(file_path):
    grid = []
    with open(file_path, "r") as file_handle:
        for line in file_handle:
            grid.append([int(x) for x in line.strip()])
    return grid


def find_trailheads(grid):
    trailheads = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                trailheads.append((row, col))
    return trailheads


def count_reachable_nines(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[x][y] == 9:
            reachable_nines.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == grid[x][y] + 1:
                    queue.append((nx, ny))

    return len(reachable_nines)


file = read_input("../input.txt")
trailheads = find_trailheads(file)
total = 0
for trailhead in trailheads:
    total += count_reachable_nines(file, trailhead)


print(trailheads)

print(total)
