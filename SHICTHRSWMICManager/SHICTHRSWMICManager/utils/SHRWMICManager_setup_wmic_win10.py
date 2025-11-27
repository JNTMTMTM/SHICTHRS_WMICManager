
import subprocess

def setup_wmic_win10() -> tuple:
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
        return (False , result.returncode)