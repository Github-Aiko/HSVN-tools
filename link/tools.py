import subprocess
import platform
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

def wget(url, filename):
    cmd = subprocess.call(["wget", url+"&download=1", "-O", str(downloads_path)+"/"+filename])

def openfolder():
	cmd = subprocess.call(["open", downloads_path])
	
def tools():
    if platform.machine() == "Darwin":
        wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EUw0nZE6EohGlttwfe--N8YBtiaHESwaxeTfZR31qU7DCA?e=kBq6gC", "MacOS-Tools.zip")
    elif platform.machine() == "Linux":
        wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EY12YmQAAZhFkfn0ptQzMy4B7YZ_JiTp6TNmR_xXKxbXFg?e=iuCpLu", "Linux-Tools.zip")
    elif platform.machine() == "Windows":
        wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EcTPCZNbVZtDuZ8XPXz-i-QB3It5CMcsiO4pU7KAq5iLyw?e=fJNzJ5", "Windows-Tools.zip")
