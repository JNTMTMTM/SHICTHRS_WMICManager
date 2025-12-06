# *-* coding: utf-8 *-*
# src\__init__.py
# SHICTHRS WMIC MANAGER
# AUTHOR : SHICTHRS-JNTMTMTM
# Copyright : © 2025-2026 SHICTHRS, Std. All rights reserved.
# lICENSE : GPL-3.0

from colorama import init
init()

from .utils.SHRWMICManager_check_is_wmic_available import check_is_wmic_available
# from .utils.SHRWMICManager_install_wmic_win10 import install_wmic_win10
# from .utils.SHRWMICManager_install_wmic_win11 import install_wmic_win11
# from .utils.SHRWMICManager_uninstall_wmic_win11 import uninstall_wmic_win11

__all__ = ['SHRWMICManager_check_is_wmic_available']

print('\033[1mWelcome to use SHRWMICManager\033[0m\n|  \033[1;34mGithub : https://github.com/JNTMTMTM/SHICTHRS_WMICManager\033[0m')
print('|  \033[1mAlgorithms = rule ; Questioning = approval\033[0m')
print('|  \033[1mCopyright : © 2025-2026 SHICTHRS, Std. All rights reserved.\033[0m\n')

class SHRWMICManagerException(Exception):
    def __init__(self , message: str) -> None:
        self.message = message
    
    def __str__(self):
        return self.message

def SHRWMICManager_check_is_wmic_available():
    try:
        return check_is_wmic_available()
    except Exception as e:
        raise SHRWMICManagerException(f"SHRWMICManager [ERROR.7000] unable to check wmic | {str(e)}")

# def SHRWMICManager_install_wmic_win10():
#     try:
#         return install_wmic_win10(SHRWMICManagerException)
#     except Exception as e:
#         raise SHRWMICManagerException(f"SHRWMICManager [ERROR.7001] unable to install wmic [win10] | {str(e)}")

# def SHRWMICManager_install_wmic_win11():
#     try:
#         return install_wmic_win11(SHRWMICManagerException)
#     except Exception as e:
#         raise SHRWMICManagerException(f"SHRWMICManager [ERROR.7003] unable to install wmic [win11] | {str(e)}")
    
# def SHRWMICManager_uninstall_wmic_win11():
#     try:
#         return uninstall_wmic_win11(SHRWMICManagerException)
#     except Exception as e:
#         raise SHRWMICManagerException(f"SHRWMICManager [ERROR.7005] unable to uninstall wmic [win11] | {str(e)}")