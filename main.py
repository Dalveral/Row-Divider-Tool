number = int(input())

def add_staff_list() -> list:
    lines = []
    with open('staff.txt', 'r') as file:
        lines = [line.strip() for line in file]
    return lines

staff_list = add_staff_list()
staff = (len(staff_list))

slice1 = (number - ((int(number / staff) * staff))) *  (int(number / staff) + 1)
slice2 = number - slice1
part1 = number - (int(number / staff) * staff)
part2 = int(slice2 / int(number / staff))

def adding_with_zero(staff_list, slice1, slice2, part1, part2, number) -> list: 
    lst = []
    for s in staff_list[:part2]:
        for i in range(int(slice2 / part2)):
            lst.append(s)

    for s in staff_list[part2:part1+part2]:
        for i in range(int(slice1 / part1)):
            lst.append(s)

    return lst

def adding_without_zero(staff_list, number) -> list:
    lst = []
    for s in staff_list:
        for i in range(number):
            lst.append(s)

    return lst

if number % staff == 0:
    lst = adding_without_zero(staff_list, number)
else:
    lst = adding_with_zero(staff_list, slice1, slice2, part1, part2, number)

with open('staff_lines', 'w') as f:
    for i in lst:
        f.write(f"{i}\n")
