def counter(num_list):
    num_count = {}

    for num in num_list:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    return num_count


def calculat_similarity_score(file_name):
    right_count = {}
    left_list, right_list = [], []
    with open(file_name, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    right_count = counter(right_list)

    similarity_score = 0
    for num_left in left_list:
        if num_left in right_count:
            similarity_score += num_left * right_count[num_left]

        else:
            similarity_score += num_left * 0
    return similarity_score


file_name = "../input.txt"
similarity_score = calculat_similarity_score(file_name)
print(f"Similarity score: {similarity_score}")
