def count_word_occurence(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1),
    ]

    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False

        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy):
                    count += 1

    return count


with open("../input.txt") as file:
    lines = file.readlines()

grid = [line.strip() for line in lines]

word = "XMAS"

result = count_word_occurence(grid, word)

print("Total occurence of the '{}': {}".format(word, result))
