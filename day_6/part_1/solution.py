map_input = []
with open("../input.txt") as f:
    for line in f:
        map_input.append(line.strip())
directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

direction_order = ["^", ">", "v", "<"]
guard_pos = None
guard_dir = None
rows, cols = len(map_input), len(map_input[0])

for r in range(rows):
    for c in range(cols):
        if map_input[r][c] in directions:
            guard_pos = (r, c)
            guard_dir = map_input[r][c]
            break
    if guard_pos:
        break


visited = set()
visited.add(guard_pos)

while True:
    dr, dc = directions[guard_dir]
    next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

    out_of_bounds = (
        next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= cols
    )

    if not out_of_bounds and map_input[next_pos[0]][next_pos[1]] != "#":
        guard_pos = next_pos
        visited.add(guard_pos)
    else:
        current_index = direction_order.index(guard_dir)
        guard_dir = direction_order[(current_index + 1) % 4]

    if out_of_bounds:
        break

print(visited)
