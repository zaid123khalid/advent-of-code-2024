def parse_input(file_path):
    with open(file_path, "r") as file_handle:
        sections = file_handle.read().split("\n\n")

    rules = []
    for rule in sections[0].splitlines():
        x, y = map(int, rule.split("|"))
        rules.append((x, y))

    updates = []
    for update in sections[1].splitlines():
        updates.append(list(map(int, update.split(","))))

    return rules, updates


def is_valid_update(update, rules):
    requied_before = {page: set() for page in update}
    for x, y in rules:
        if x in requied_before and y in requied_before:
            requied_before[y].add(x)

    seen = set()
    for page in update:
        if not requied_before[page].issubset(seen):
            return False
        seen.add(page)
    return True


file_path = "../input.txt"
rules, updates = parse_input(file_path)
sum_of_middle_pages = 0

for update in updates:
    if is_valid_update(update, rules):
        middle_index = len(update) // 2
        sum_of_middle_pages += update[middle_index]


print(f"Sum of middle pages for valid updates: {sum_of_middle_pages}")
