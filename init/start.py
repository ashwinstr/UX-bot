

import os

def upstream() -> None:
    os.system("git remote rm upstream")
    os.system("git remote add upstream https://github.com/ashwinstr/UX-bot.git")