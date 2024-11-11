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
python row_divider_tool.py`
```

## License

MIT License

Copyright (c) 2024 Andrey Lybkov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.