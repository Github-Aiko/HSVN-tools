import platform
import subprocess

def cleansc():
    print("\033c", end="")
    return "\033c"

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