import platform
import subprocess
from app.system.systemcheck import check_brew, checkchoco
from pathlib import Path

# check wget if not install it 
def checkwget():
	if platform.system() == "Linux":
		cmd = subprocess.call(["which", "wget"])
		if cmd == 0:
			print("wget is installed")
		else:
			print("wget is not installed")
			cmd = subprocess.call(["sudo", "apt", "update"])
			cmd = subprocess.call(["sudo", "apt", "install", "wget"])
	elif platform.system() == "Darwin":
		check_brew()
		cmd = subprocess.call(["which", "wget"])
		if cmd == 0:
			print("wget is installed")
		else:
			print("wget is not installed")
			cmd = subprocess.call(["brew", "install", "wget"])
	elif platform.system() == "Windows":
		checkchoco()
		cmd = subprocess.call(["where", "wget"])
		if cmd == 0:
			print("wget is installed")
		else:
			print("wget is not installed")
			cmd = subprocess.call(["choco", "install", "wget"])
	else:
		print("Can't find your OS")

def opendownloads():
	cmd = subprocess.call(["open", downloads_path])