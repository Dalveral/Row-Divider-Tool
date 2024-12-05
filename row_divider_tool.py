import os

from functions.calculation_func import with_zero, without_zero, base_calculation
from functions.work_with_files_func import get_staff_list, write_staff_lines, check_staff_file
from functions.open_folder_func import ask_folder

ZERO = 0
ONE = 1

current_directory = os.getcwd()


def main() -> None:

    ask = ask_folder(current_directory)

    if not ask:
        return

    if not check_staff_file():
        print('The file "staff.txt" seems to be empty.')
        return

    try:
        number = int(input('Enter a number: '))

    except (ValueError, KeyboardInterrupt):
        print('Error in input, please try again.')
        return

    staff_list = get_staff_list()
    count_staff = len(staff_list)

    if number <= count_staff:
        if number < ONE:
            print('Error in input, please try again.')
            return

        write_staff_lines(staff_list[:number])
        return

    if number % count_staff == ZERO:
        result = without_zero(staff_list, number)
    else:
        slice1, slice2, part1, part2 = base_calculation(number, count_staff)
        result = with_zero(staff_list, slice1, slice2, part1, part2)

    write_staff_lines(result)
    print(f'All done. Unique staff: \n{'; '.join(staff_list)}')


if __name__ == '__main__':
    main()
