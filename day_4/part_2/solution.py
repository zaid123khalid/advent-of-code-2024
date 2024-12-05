def count_x_mas_pattern(grid):
    cols, rows = len(grid[0]), len(grid)
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                mas_tuple = ("MAS", "SAM")

                try:
                    diagonal_1 = (
                        grid[r + (-1)][c + (-1)] + grid[r][c] + grid[r - (-1)][c - (-1)]
                    )
                    diagonal_2 = (
                        grid[r + (-1)][c + 1] + grid[r][c] + grid[r - (-1)][c - 1]
                    )
                    if diagonal_1 in mas_tuple and diagonal_2 in mas_tuple:
                        count += 1

                except IndexError:
                    pass

    return count


with open("../input.txt") as file:
    lines = file.readlines()

grid = [line.strip() for line in lines]

result = count_x_mas_pattern(grid)

print("Total occurence are {}".format(result))
