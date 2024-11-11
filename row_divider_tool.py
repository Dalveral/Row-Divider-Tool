from functions.calculation_func import with_zero, without_zero, base_calculation
from functions.work_with_files_func import get_staff_list, write_staff_lines, check_staff_file


def main() -> None:
    if not check_staff_file():
        print('Error find file, please try again.')
        return

    try:
        number = int(input('Enter a number: '))

    except (ValueError, KeyboardInterrupt):
        print('Error in input, please try again.')
        return

    if number < 3:
        print('Error in input, please try again.')
        return

    staff_list = get_staff_list()
    count_staff = len(staff_list)

    if number % count_staff == 0:
        result = without_zero(staff_list, number)
    else:
        slice1, slice2, part1, part2 = base_calculation(number, count_staff)
        result = with_zero(staff_list, slice1, slice2, part1, part2)

    if result:
        write_staff_lines(result)


if __name__ == '__main__':
    main()
