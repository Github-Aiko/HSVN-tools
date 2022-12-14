import platform
import subprocess
from app.system.systemcheck import check_brew, checkchoco
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

# check wget if not install it 
def checkwget():
	if platform.system() == "Linux":
		cmd = subprocess.call(["which", "wget"])
		if cmd == 0:
			print("wget is installed")
		else:
			# if centos
			if platform.linux_distribution()[0] == "CentOS Linux":
				cmd = subprocess.call(["yum", "update"])
				cmd = subprocess.call(["yum", "install", "wget"])
			# if ubuntu
			elif platform.linux_distribution()[0] == "Ubuntu":
				cmd = subprocess.call(["apt", "update"])
				cmd = subprocess.call(["apt", "install", "wget"])
			# if debian
			elif platform.linux_distribution()[0] == "Debian GNU/Linux":
				cmd = subprocess.call(["apt", "update"])
				cmd = subprocess.call(["apt", "install", "wget"])
			# if fedora
			elif platform.linux_distribution()[0] == "Fedora":
				cmd = subprocess.call(["dnf", "update"])
				cmd = subprocess.call(["dnf", "install", "wget"])
			# if arch
			elif platform.linux_distribution()[0] == "Arch Linux":
				cmd = subprocess.call(["pacman", "-Syu"])
				cmd = subprocess.call(["pacman", "-S", "wget"])
			else:
				print("Can't find your OS")
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

def openfolder():
	cmd = subprocess.call(["open", downloads_path])