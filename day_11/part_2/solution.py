def read_input(file_path: str):
    with open(file_path, "r") as file:
        for line in file:
            return line.strip().split(" ")


def evolve_stones_optimized(stones, blinks):
    from collections import Counter

    stone_counts = Counter(stones)

    for _ in range(blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                mid = len(digits) // 2
                left = int(digits[:mid])
                right = int(digits[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        stone_counts = new_counts
    return sum(stone_counts.values())


input_data = read_input("../input.txt")
stones = [int(stone) for stone in input_data]
result = evolve_stones_optimized(stones, 75)
print(result)
