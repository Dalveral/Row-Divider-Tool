# Row Divider Tool

A simple tool for dividing rows among employees.

## Description

Row Divider Tool is a program that helps divide rows among employees as evenly as possible. The program takes the number of rows to be divided and uses a list of employees from a file named "staff.txt" in the project root. The result is written to a file named "staff_lines.txt".

## Usage

1. Create a file named "staff.txt" in the project root and add a list of employees, each on a new line.
2. Run the program and enter the number of rows to be divided.
3. The program will calculate and write the number of rows to be assigned to each employee to a file named "staff_lines.txt".

## Example of "staff.txt" file

```
Ivanov Ivan Ivanovich
Petrov Petr Petrovich
Sidorov Sergey Sergeevich
```

## Example usage

```
Enter a number: 10
```

Result (written to "staff_lines.txt"):
```
Ivanov Ivan Ivanovich
Ivanov Ivan Ivanovich
Ivanov Ivan Ivanovich
Petrov Petr Petrovich
Petrov Petr Petrovich
Petrov Petr Petrovich
Sidorov Sergey Sergeevich
Sidorov Sergey Sergeevich
Sidorov Sergey Sergeevich
Sidorov Sergey Sergeevich
```

## Requirements

* Python 3.x

## Installation

1. Download the repository.
2. Run the program using the command 
```bash
python row_divider_tool.py
```
