import os


def get_staff_list() -> list:
    with open('staff.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        print(lines)
        print(len(lines))
    return lines


def write_staff_lines(result: list) -> None:
    with open('staff_lines.txt', 'w') as f:
        for i in result:
            f.write(f"{i}\n")


def check_staff_file() -> bool:
    file = os.path.isfile('staff.txt')

    if file:
        return True

    return False
