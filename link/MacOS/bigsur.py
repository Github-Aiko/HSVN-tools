from link.MacOS.wget import wget

def bigsur():
	print("Dowload macOS Big Sur")
	print("1. macOS Big Sur 11.7 (USB 16GB)")
	print("2. macOS Big Sur 11.7 (USB 16GB) + WinPE")
	print("3. macOS Big Sur 11.6.8 (USB 16GB) + WinPE")
	print("4. macOS Big Sur 11.2.3 (USB 16GB) + WinPE")
	choice = int(input("Enter your choice: "))
	if (choice == 1):
		bigsur11_7_install()
	elif (choice == 2):
		bigsur11_7_install_pe()
	elif (choice == 3):
		bigsur11_6_8_install_pe()
	elif (choice == 4):
		bigsur11_2_3_install_pe()
	else:
		print("Invalid choice")
		bigsur()

def bigsur11_7_install():
    wget("https://www.dropbox.com/s/jqc0oy1v9rgmme4/HSVN-macOS%20Big%20Sur%2011.7.dmg?dl=0", "macOS Big Sur 11.7 (USB 16GB).dmg")

def bigsur11_7_install_pe():
	wget("https://www.dropbox.com/s/prfyt0hjuabu7en/HSVN-macOS%20Big%20Sur%2011.7%20%2B%20WinPE.dmg?dl=0", "macOS Big Sur 11.7 (USB 16GB) + WinPE.dmg")

def bigsur11_6_8_install_pe():
	wget("https://www.dropbox.com/s/z8a39mtw14i9lit/HSVN-macOS%20Big%20Sur%2011.6.8%20%2B%20WinPE.dmg?dl=0", "macOS Big Sur 11.6.8 (USB 16GB) + WinPE.dmg")

def bigsur11_2_3_install_pe():
	wget("https://www.dropbox.com/s/o6x2wqpxuz5nd1h/HSVN-macOS%20Big%20Sur%2011.2.3%20%2B%20WinPE.dmg?dl=0", "macOS Big Sur 11.2.3 (USB 16GB) + WinPE.dmg")

