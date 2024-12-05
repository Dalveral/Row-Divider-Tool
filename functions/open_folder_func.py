import os
import platform
import subprocess

current_directory = os.getcwd()


def ask_folder(folder_path: str) -> None:
    folder_question = input(f"Folder app: {folder_path}. Open it? \n 1 - Yes \n 2 - No: ")

    if folder_question != "1":
        print('Invalid input please try again')
        return

    open_folder(folder_path)


def open_folder(c) -> None:
    platforms = {
        'Linux': '',
        'Windows': '',
        'Darwin': '["open"]',
    }

    subprocess.run(['open', c])

open_folder(current_directory)
print(platform.system())
print(current_directory)
