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


def calculate_trail_rating(grid, start):
    rows, cols = len(grid), len(grid[0])
    memo = {}

    def dfs(x, y):
        if grid[x][y] == 9:
            return 1

        if (x, y) in memo:
            return memo[(x, y)]

        total_trails = 0

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == grid[x][y] + 1:
                    total_trails += dfs(nx, ny)

        memo[(x, y)] = total_trails
        return total_trails

    return dfs(*start)


file = read_input("../input.txt")
trailheads = find_trailheads(file)
total = 0
for trailhead in trailheads:
    total += calculate_trail_rating(file, trailhead)


print(trailheads)

print(total)
