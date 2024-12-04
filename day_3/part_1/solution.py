import re

with open("../input.txt") as f:
    lines = f.read()

pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")

matches = re.findall(pattern, lines)

result = 0

for match in matches:
    result += int(match[0]) * int(match[1])

print(f"The sum of all valid multiplications is: {result}")
