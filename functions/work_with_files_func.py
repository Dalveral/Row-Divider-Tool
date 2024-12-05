import os


def get_staff_list() -> list:
    lines = []
    with open('staff.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) < 4 or line in lines:
                continue
            lines.append(line)

    return lines


def write_staff_lines(result: list) -> None:
    with open('staff_lines.txt', 'w') as f:
        for i in result:
            f.write(f"{i}\n")


def check_staff_file() -> bool:
    file = os.path.isfile('staff.txt')

    if not file:
        with open('staff.txt', 'w') as file:
            file.write('')

        return False

    size = os.path.getsize('staff.txt')
    print(size)

    if size < 8:
        return False

    return True
