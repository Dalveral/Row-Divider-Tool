from functions.calculation_func import with_zero, without_zero, base_calculation
from functions.work_with_files_func import get_staff_list, write_staff_lines, check_staff_file
from functions.questions_func import start_questions_func
from functions.response_func import response


def main() -> None:
    check_staff_file()

    number = start_questions_func()

    if not number:
        return

    staff_list = get_staff_list()
    count_staff = len(staff_list)

    if number <= count_staff or count_staff == 0:
        write_staff_lines(staff_list[:number])

        response(staff_list)

        return

    if number % count_staff == 0:
        result = without_zero(staff_list, number)
    else:
        slice1, slice2, part1, part2 = base_calculation(number, count_staff)
        result = with_zero(staff_list, slice1, slice2, part1, part2)

    write_staff_lines(result)

    response(staff_list)

    return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stop')
