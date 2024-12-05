import os


def get_staff_list() -> list:
    lines = []
    with open('staff.txt', 'r') as file:
        for line, i in zip(file, lines):
            print(line)
            print(i)
            if len(line.strip()) < 4:
                continue
            if line.strip() == i:
                continue

            lines.append(line.strip())
    print(lines)
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
