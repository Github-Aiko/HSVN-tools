from link.MacOS.wget import wget

def mojave():
	print("Dowload macOS Mojave")
	print("1. macOS Mojave 10.14.6 (USB 16GB)")
	print("2. macOS Mojave 10.14.6 (USB 16GB) + WinPE")
	choice = int(input("Enter your choice: "))
	if (choice == 1):
		print("Coming soon")
		mojave()
	elif (choice == 2):
		mojave10_14_6_install_pe()
	else:
		print("Invalid choice")
		mojave()

def mojave10_14_6_install_pe():
	wget("https://www.dropbox.com/s/ygxd896uhnfxkjs/HSVN-macOS%20Mojave%2010.14.6%2BWinPE.dmg?dl=0", "macOS Mojave 10.14.6 (USB 16GB) + WinPE.dmg")