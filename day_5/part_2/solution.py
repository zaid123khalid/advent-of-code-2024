from collections import deque, defaultdict


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


def reorder_update(update, rules):
    subgraph = defaultdict(set)
    for x, y in rules:
        if x in update and y in update:
            subgraph[x].add(y)

    in_degree = {page: 0 for page in update}
    for x in subgraph:
        for y in subgraph[x]:
            in_degree[y] += 1

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    while queue:
        page = queue.popleft()
        sorted_update.append(page)
        for neighbor in subgraph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


file_path = "../input.txt"
rules, updates = parse_input(file_path)
invalid_updates = []

for update in updates:
    if not is_valid_update(update, rules):
        invalid_updates.append(update)


reordered_updates = [reorder_update(update, rules) for update in invalid_updates]
middle_sum = sum([update[len(update) // 2] for update in reordered_updates])

print(f"Sum of middle pages for valid updates: {middle_sum}")
