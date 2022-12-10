from link.MacOS.wget import wget

def catalina():
	print("Dowloada macOS Catalina")
	print("1. macOS Catalina 10.15.7 (USB 16GB)")
	print("2. macOS Catalina 10.15.7 (USB 16GB) + WinPE + Tools")
	choice = int(input("Enter your choice: "))
	if (choice == 1):
		catalina_10_15_7_install()
	elif (choice == 2):
		catalina_10_15_7_install_pe()
	else:
		print("Invalid choice")
		catalina()

def catalina_10_15_7_install():
	wget("https://www.dropbox.com/s/qwnxfdeesbxymw3/HSVN-macOS%20Catalina%2010.15.7%20installer.dmg?dl=0", "macOS Catalina 10.15.7 (USB 16GB).dmg")

def catalina_10_15_7_install_pe():
	wget("https://www.dropbox.com/s/3q15edgwsznn9en/HSVN-macOS%20Catalina%2010.15.7%20%2B%20WinPE%20%2B%20Tools.dmg?dl=0", "macOS Catalina 10.15.7 (USB 16GB) + WinPE + Tools.dmg")