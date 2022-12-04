import platform
import subprocess


# check OS Windows , Linux , Mac and print it
def checkOS():
    print(platform.system())
    return platform.system()


# get architecture
def checkArch():
    print(platform.machine())
    return platform.machine()

def wget(url, patch):
    cmd = subprocess.call(["wget", url, "-O", patch])

def cleansc():
    print("\033c", end="")
    return "\033c"