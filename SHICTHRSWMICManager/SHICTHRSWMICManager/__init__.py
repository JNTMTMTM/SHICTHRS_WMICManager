# *-* coding: utf-8 *-*
# src\__init__.py
# SHICTHRS WMIC MANAGER
# AUTHOR : SHICTHRS-JNTMTMTM
# Copyright : © 2025-2026 SHICTHRS, Std. All rights reserved.
# lICENSE : GPL-3.0

import os
from colorama import init
init()

print('\033[1mWelcome to use SHRWMICManager\033[0m\n|  \033[1;34mGithub : https://github.com/JNTMTMTM/SHICTHRS_WMICManager\033[0m')
print('|  \033[1mAlgorithms = rule ; Questioning = approval\033[0m')
print('|  \033[1mCopyright : © 2025-2026 SHICTHRS, Std. All rights reserved.\033[0m\n')

class SHRWMICManagerException(BaseException):
    def __init__(self , message: str) -> None:
        self.message = message
    
    def __str__(self):
        return self.message