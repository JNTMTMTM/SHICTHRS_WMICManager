
import subprocess

def install_wmic_win10(error_class) -> tuple:
    result = subprocess.run(
        ['dism', '/online', '/Enable-Feature', '/FeatureName:WMIC', '/NoRestart'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    if result.returncode == 0:
        return (True , result.returncode)
    else:
        raise error_class(f"SHRWMICManager [ERROR.7002] error occurred while installing wmic | return_code:{result.returncode}")