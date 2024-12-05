import os
import platform
import subprocess

platforms = {
    'Linux': '',
    'Windows': '',
    'Darwin': '',
}

current_directory = os.getcwd()

def open_folder(c) -> None:
    subprocess.run(['open', c])

open_folder(current_directory)
print(platform.system())
print(current_directory)
