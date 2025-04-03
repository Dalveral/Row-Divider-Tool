import platform
import subprocess
from settings import CURRENT_DIRECTORY


def open_folder() -> None:
    user_platform = platform.system()
    platforms = {
        'Linux': '',
        'Windows': 'explorer',
        'Darwin': 'open',
    }

    open_command = [platforms.get(user_platform), CURRENT_DIRECTORY]

    if user_platform == 'Windows':
        open_command = ['explorer', CURRENT_DIRECTORY]

    subprocess.run(open_command)
