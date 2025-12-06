
import subprocess

def check_is_wmic_available() -> tuple:
    try:
        startup_info = subprocess.STARTUPINFO()
        startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startup_info.wShowWindow = 0

        result = subprocess.run(
            ['wmic', 'os', 'get', 'Caption', '/value'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            startupinfo=startup_info,
            timeout=5
        )

        return (result.returncode == 0 and "Caption" in result.stdout , result.returncode)
        
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return (False , None)

