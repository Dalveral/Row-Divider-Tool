import platform
import subprocess
from settings import CURRENT_DIRECTORY


def open_folder() -> None:
    user_platform = platform.system()
    platforms = {
        'Linux': '',
        'Windows': '',
        'Darwin': 'open',
    }

    open_command = [platforms.get(user_platform), CURRENT_DIRECTORY]

    subprocess.run(open_command)
