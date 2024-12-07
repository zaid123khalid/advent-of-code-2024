def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "||":
            result = int(str(result) + str(numbers[i + 1]))
    return result


def generate_operator_combinations(length):
    if length == 0:
        return [[]]
    smaller_combinations = generate_operator_combinations(length - 1)
    return (
        [combo + ["+"] for combo in smaller_combinations]
        + [combo + ["*"] for combo in smaller_combinations]
        + [combo + ["||"] for combo in smaller_combinations]
    )


def calculate_calibration(file_name):

    equations = []
    with open(file_name, "r") as file:
        equations = file.readlines()

    total = 0
    for equation in equations:
        test_value, numbers = equation.split(":")
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))

        operator_combinations = generate_operator_combinations(len(numbers) - 1)

        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                total += test_value
                break

    return total


file_name = "../input.txt"
result = calculate_calibration(file_name)
print("Total Calibration Result:", result)
