from link.MacOS.wget import wget

def ventura():
	print("Dowload macOS Ventura")
	print("1. macOS Ventura 13.0.1 (USB 16GB)")
	print("2. macOS Ventura 13.0.1 (USB 16GB) + WinPE + Tools")
	choice = int(input("Enter your choice: "))
	if (choice == 1):
		ventura13_0_1_install()
	elif (choice == 2):
		print("Coming soon")
		ventura()
	else:
		print("Invalid choice")
		ventura()

def ventura13_0_1_install():
	wget("https://www.dropbox.com/s/r2hr5mdeqzg229d/HSVN-macOS%20Ventura%2013.01%20install.dmg?dl=0", "macOS Ventura 13.0.1 (USB 16GB).dmg")