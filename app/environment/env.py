import subprocess
from app.system.systemcheck import wget

#check wget on macos, linux, windows and install if not installed
def checkwget():
    cmd = subprocess.call(["wget", "--version"])
    if cmd == 0:
        return True
    else:
        return False

def installwgetwin():
    wget("https://eternallybored.org/misc/wget/1.21.3/64/wget.exe", "/tmp/dowload/wget.exe")