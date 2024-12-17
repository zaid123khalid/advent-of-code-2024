def read_input(file_path):
    with open(file_path, "r") as file_handle:
        grid = [line.strip() for line in file_handle.readlines()]

    return grid


def get_unique_antinodes(grid):
    antennas_positions = {}
    row = len(grid)
    col = len(grid[0])
    for r in range(row):
        for c in range(col):
            char = grid[r][c]
            if char.isalnum():
                if char not in antennas_positions:
                    antennas_positions[char] = []
                antennas_positions[char].append((r, c))

    antinodes = set()
    for freq, positions in antennas_positions.items():
        n = len(positions)
        if n < 2:
            continue
        antinodes.update(positions)
        for i in range(n):
            for j in range(i, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                dr = r2 - r1
                dc = c2 - c1
                for k in range(-max(row, col), max(row, col)):
                    r_antin = r1 + k * dr
                    c_antin = c1 + k * dc
                    if 0 <= r_antin < row and 0 <= c_antin < col:
                        antinodes.add((r_antin, c_antin))

    return len(antinodes)


file_path = "../input.txt"

grid = read_input(file_path)
print(get_unique_antinodes(grid))
