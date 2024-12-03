def calculate_total_distance_from_file(file_name):
    left_list, right_list = [], []
    with open(file_name, "r") as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    total_distance = sum(
        abs(left - right) for left, right in zip(left_list, right_list)
    )

    return total_distance


file_name = "../input.txt"
total_distance = calculate_total_distance_from_file(file_name)
print(f"Total distance: {total_distance}")
