import os
import re

from settings import STAFF_FILES, CURRENT_DIRECTORY


def get_staff_list() -> list:
    lines = []
    with open(f'{CURRENT_DIRECTORY}/{STAFF_FILES[0]}', 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) < 4:
                continue
            parts = re.findall(r'[A-ZА-ЯЁ][a-zа-яё]* [A-ZА-ЯЁ][a-zа-яё]* [A-ZА-ЯЁ][a-zа-яё]*|[A-ZА-ЯЁ][a-zа-яё]*[A-ZА-ЯЁ][a-zа-яё]*[A-ZА-ЯЁ][a-zа-яё]*', line)
            if len(parts) > 1:
                for part in parts:
                    lines.append(part)
            else:
                lines.append(line)

    return list(dict.fromkeys(lines))


def write_staff_lines(result: list) -> None:
    with open(f'{CURRENT_DIRECTORY}/{STAFF_FILES[1]}', 'w') as f:
        for i in result:
            f.write(f"{i}\n")


def check_staff_file() -> None:
    file = os.path.isfile(f'{CURRENT_DIRECTORY}/{STAFF_FILES[0]}')

    if not file:
        with open(f'{CURRENT_DIRECTORY}/{STAFF_FILES[0]}', 'w') as file:
            file.write('')

