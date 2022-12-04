import platform
import subprocess
import getpass as gt

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

def check_brew():
	if platform.system() == "Darwin":
		# nếu là chip intel
		if platform.machine() == "x86_64":
			cmd = subprocess.call(["which", "brew"])
			if cmd == 0:
				print("brew is installed")
			else:
				print("brew is not installed")
				cmd = subprocess.call(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])
				cmd = subprocess.call(["echo", "'# Set PATH, MANPATH, etc., for Homebrew.'", ">>", "/Users/"+str(gt.getuser())+"/.zprofile"])
				cmd = subprocess.call(["echo", "'eval $(/opt/homebrew/bin/brew shellenv)'", ">>", "/Users/"+str(gt.getuser())+"/.zprofile"])
				cmd = subprocess.call(["eval", "$(/opt/homebrew/bin/brew shellenv)"])
		# nếu là chip m1
		elif platform.machine() == "arm64":
			cmd = subprocess.call(["which", "brew"])
			if cmd == 0:
				print("brew is installed")
			else:
				print("brew is not installed")
				cmd = subprocess.call(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])
		else:
			print("Can't find your chip")
	else:
		print("Can't find your OS")

def checkchoco():
	if platform.system() == "Windows":
		cmd = subprocess.call(["where", "choco"])
		if cmd == 0:
			print("choco is installed")
		else:
			print("choco is not installed")
			cmd = subprocess.call(["powershell", "-Command", "Set-ExecutionPolicy", "Bypass", "-Scope", "Process", "-Force;[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"])
	else:
		print("Can't find your OS")