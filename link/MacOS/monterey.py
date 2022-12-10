from link.MacOS.wget import wget as wget

def monterey():
	print("Dowload macOS Monterey")
	print("1. macOS Monterey 12.6.1 (USB 16GB)")
	print("2. macOS Monterey 12.6 (USB 16GB)")
	print("3. macOS Monterey 12.5 (USB 16GB)")
	print("4. macOS Monterey 12.4 (USB 16GB)")
	print("5. macOS Monterey 12.0.1 (USB 16GB)")
	choice = int(input("Enter your choice: "))
	if (choice == 1):
		monterey12_6_1_install()
	elif (choice == 2):
		monterey12_6_install()
	elif (choice == 3):
		monterey12_5_install()
	elif (choice == 4):
		monterey12_4_install()
	elif (choice == 5):
		monterey12_0_1_install()
	else:
		print("Invalid choice")
		monterey()


def monterey12_6_1_install():
    wget("https://www.dropbox.com/s/o273bwtltfvymqi/HSVN-macOS%20Monterey%2012.6.1.dmg?dl=0", "macOS Monterey 12.6.1 (USB 16GB).dmg")

def monterey12_6_install():
	wget("https://www.dropbox.com/s/pgftkrxoaxcezd9/HSVN-macOS%20Monterey%2012.6.dmg?dl=0", "macOS Monterey 12.6 (USB 16GB).dmg")

def monterey12_5_install():
	wget("https://www.dropbox.com/s/xov22ixssw59d1v/HSVN-macOS%20Monterey%2012.5.dmg?dl=0", "macOS Monterey 12.5 (USB 16GB).dmg")

def monterey12_4_install():
	wget("https://www.dropbox.com/s/sutxxizcdehqyks/HSVN-macOS%20Monterey%2012.4.dmg?dl=0", "macOS Monterey 12.4 (USB 16GB).dmg")

def monterey12_0_1_install():
	wget("https://www.dropbox.com/s/0v9r8vetzakgw6r/HSVN-macOS%20Monterey%2012.0.1.dmg?dl=0", "macOS Monterey 12.0.1 (USB 16GB).dmg")
