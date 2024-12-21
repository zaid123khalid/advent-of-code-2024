def read_input(file_path):
    claws_machine = []
    with open(file_path, "r") as file:
        machines = file.read().strip().split("\n\n")
        for machine in machines:
            claws_machine.append(machine.strip().split("\n"))
    return claws_machine


def parse_input(claws_machine) -> dict:
    buttons = []
    for machine in claws_machine:
        parsed_machine = {}
        for line in machine:
            if "Button" in line:
                button = line.split(":")[0]
                x, y = line.split(":")[1].split(", ")
                x = int(x.split("+")[1])
                y = int(y.split("+")[1])
                parsed_machine[button] = (x, y)
            elif "Prize" in line:
                x = line.split(",")[0].split("=")[1]
                y = line.split(",")[1].split("=")[1]
                x = int(x)
                y = int(y)
                parsed_machine["Prize"] = (x, y)
        buttons.append(parsed_machine)

    return buttons


def check_prize(button, button2, prize):
    a_x, a_y = button
    b_x, b_y = button2
    x, y = prize
    for i in range(100):
        for j in range(100):
            if (a_x * i + b_x * j == x) and (a_y * i + b_y * j == y):
                return (i, j)
    return None


def calculate_total_cost(price_a, price_b, results):
    total_cost = 0
    for result in results:
        cost = price_a * result[0] + price_b * result[1]
        total_cost += cost
    return total_cost


file_path = "../input.txt"
claws_machine = read_input(file_path)
buttons = parse_input(claws_machine)
valid_results = []

for button in buttons:
    button_a = None
    button_b = None
    prize = None
    for key, value in button.items():
        if key == "Button A":
            button_a = value
        elif key == "Button B":
            button_b = value
        elif key == "Prize":
            prize = value

    if button_a and button_b and prize:
        result = check_prize(button_a, button_b, prize)
        if result:
            valid_results.append(result)

total_cost = calculate_total_cost(3, 1, valid_results)

print(total_cost)
