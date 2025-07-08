# utils.py

import os
import platform

def terminal_clean():
    os.system("cls" if platform.system() == "Windows" else "clear")