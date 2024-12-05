import platform
import subprocess


def ask_folder(folder_path: str) -> bool:
    try:
        folder_question = input(f"Folder app: {folder_path}. Open it? \n 1 - Yes \n 2 - No \n q - Quit\n Input: ")
    except (ValueError, KeyboardInterrupt):
        print('Stopp app.')
        return False

    if folder_question == "1":
        open_folder(folder_path)
        return True
    if folder_question == "2":
        return True

    return False


def open_folder(folder_path: str) -> None:
    user_platform = platform.system()
    platforms = {
        'Linux': '',
        'Windows': '',
        'Darwin': 'open',
    }

    open_command = [platforms.get(user_platform), folder_path]

    subprocess.run(open_command)
