#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2019 by Keno "docplay" Hummel.
# All rights reserved. Do not distribute!
# This file is part of the PYBot Project.

from colorama import *
from colorama import init
init()
import time

def log(content, type = 1):
    if type == 1:
        print(Fore.WHITE + f"{time.ctime()} | LOG ::: {content}" + Fore.RESET)
    elif type == 2:
        print(Fore.YELLOW + f"{time.ctime()} | INF ::: {content}" + Fore.RESET)
    elif type == 3:
        print(Fore.RED + f"{time.ctime()} | ERR ::: {content}" + Fore.RESET)
    elif type == 4:
        print(Fore.GREEN + f"{time.ctime()} | SUC ::: {content}" + Fore.RESET)
    elif type == 5:
        print(Fore.BLUE + f"{time.ctime()} | SUP ::: {content}" + Fore.RESET)
    elif type == 6:
        print(Fore.RED + f"{time.ctime()} | MOD ::: {content}" + Fore.RESET)