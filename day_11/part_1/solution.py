def read_input(file_path: str):
    with open(file_path, "r") as file:
        for line in file:
            return line.strip().split(" ")


def evolve_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                mid = len(digits) // 2
                left, right = int(digits[:mid]), int(digits[mid:])
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones


input_data = read_input("../input.txt")
stones = [int(stone) for stone in input_data]
result = evolve_stones(stones, 25)
print(len(result))
