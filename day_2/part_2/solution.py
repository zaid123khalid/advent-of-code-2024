def is_safe_report(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    return is_increasing or is_decreasing


def is_safe_report_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]

        if is_safe_report(modified_report):
            return True

    return False


def calculate_total_safe_reports(file_name):
    safe_reports = 0
    with open(file_name, "r") as f:
        for line in f:
            report = list(map(int, line.split()))

            if is_safe_report(report) or is_safe_report_with_dampener(report):
                safe_reports += 1

    return safe_reports


file_name = "../input.txt"
safe_reports = calculate_total_safe_reports(file_name)
print(f"Safe reports: {safe_reports}")
