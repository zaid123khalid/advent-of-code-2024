def calculate_total_safe_reports(file_name):
    safe_reports = 0
    with open(file_name, "r") as f:
        for line in f:
            report = list(map(int, line.split()))

            differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

            is_increase = all([diff in [1, 2, 3] for diff in differences])
            is_decrease = all([diff in [-1, -2, -3] for diff in differences])

            if is_increase or is_decrease:
                safe_reports += 1

    return safe_reports


file_name = "../input.txt"
safe_reports = calculate_total_safe_reports(file_name)
print(f"Safe reports: {safe_reports}")
