import re

with open("../input.txt", "r") as file:
    data = file.read()

# Regular expressions for valid mul and conditional instructions
mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Initialize variables
enabled = True  # Start with mul enabled
total_sum = 0

# Scan through the input for matches
position = 0
while position < len(data):
    # Check for "do()" or "don't()" first
    do_match = re.search(do_pattern, data[position:])
    dont_match = re.search(dont_pattern, data[position:])
    mul_match = re.search(mul_pattern, data[position:])

    # Find the earliest match
    earliest = None
    if do_match:
        earliest = ("do", do_match.start() + position)
    if dont_match and (earliest is None or dont_match.start() + position < earliest[1]):
        earliest = ("don't", dont_match.start() + position)
    if mul_match and (earliest is None or mul_match.start() + position < earliest[1]):
        earliest = ("mul", mul_match.start() + position)

    # If no more matches, break
    if not earliest:
        break

    # Process the earliest match
    if earliest[0] == "do":
        enabled = True
        position = earliest[1] + len("do()")
    elif earliest[0] == "don't":
        enabled = False
        position = earliest[1] + len("don't()")
    elif earliest[0] == "mul":
        if enabled:
            # Extract numbers and compute product
            x, y = map(int, mul_match.groups())
            total_sum += x * y
        position = earliest[1] + mul_match.end() - mul_match.start()


print(f"The sum of enabled multiplications is: {total_sum}")
