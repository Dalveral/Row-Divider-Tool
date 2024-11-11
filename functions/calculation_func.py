def with_zero(staff_list: list, slice1: int, slice2: int, part1: int, part2) -> list:
    lst = []
    for s in staff_list[:part2]:
        for i in range(int(slice2 / part2)):
            lst.append(s)

    for s in staff_list[part2:part1 + part2]:
        for i in range(int(slice1 / part1)):
            lst.append(s)

    return lst


def without_zero(staff_list: list, number: int) -> list:
    lst = []
    for s in staff_list:
        for i in range(int(number / len(staff_list))):
            lst.append(s)

    return lst


def base_calculation(number: int, count_staff: int) -> tuple[int, int, int, int]:
    slice1 = (number - (int(number / count_staff) * count_staff)) * (int(number / count_staff) + 1)
    slice2 = number - slice1
    part1 = number - (int(number / count_staff) * count_staff)
    part2 = int(slice2 / int(number / count_staff))

    return slice1, slice2, part1, part2
