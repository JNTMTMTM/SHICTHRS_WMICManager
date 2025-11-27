
import subprocess

def install_wmic_win11(error_class) -> tuple:
    result = subprocess.run(
        ['dism', '/online', '/Add-Capability', '/CapabilityName:WMIC~~~~'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    if result.returncode == 0:
        return (True , result.returncode)
    else:
        raise error_class(f"SHRWMICManager [ERROR.7004] error occurred while installing wmic | return_code:{result.returncode}")