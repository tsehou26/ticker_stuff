import subprocess
from datetime import date
today = str(date.today()).split("-")
kyouwa = today[1] + "/" + today[2] + "/" + today[0]


def acp(file_name):
    subprocess.run(['git', 'add', f"{file_name}"])
    subprocess.run(['git', 'commit', '-m', f"Updated {file_name} on {kyouwa}"])
    subprocess.run(['git', 'push', 'origin', 'main'])