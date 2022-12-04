# importing getpass library using import command
# Here gt is a alias name for getpass
# Instead of writing getpass we can use gt
import getpass as gt
 
# using getuser() method , returning current
# username
print(str(gt.getuser()))

# run this code in terminal : echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /Users/aiko/.zprofile
# run this code in terminal : echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/aiko/.zprofile
# run this code in terminal : echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/aiko/.zshrc

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
