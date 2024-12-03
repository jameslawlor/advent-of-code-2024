def is_report_safe(report,):
    if not ((report==sorted(report)) or (report==sorted(report,reverse=True))):
        print(f"Report {report} not safe")
        return False

    differences = [abs(report[i+1] - report[i]) for i in range(len(report) - 1)]
    if ((max(differences) > 3) or (min(differences)<1)):
        print(f"Report {report} not safe")
        return False
    
    print(f"Report {report} SAFE")

    return True


def solve_part_1(input):
    safe_report_count = 0
    for report in input:
        if is_report_safe(report):
            safe_report_count += 1
    return safe_report_count


def solve_part_2(input,):

    safe_report_count = 0

    for report in input:
        if is_report_safe(report):
            safe_report_count += 1
        else:
            for idx, _ in enumerate(report):
                tmp_report = report[:]
                del tmp_report[idx]
                if is_report_safe(tmp_report,):
                    safe_report_count += 1
                    break
    return safe_report_count