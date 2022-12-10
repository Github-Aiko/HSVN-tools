from link.MacOS.wget import wget

def hs():
	print("Dowload macOS High Serria")
	print("1. macOS High Serria 10.13.6 (USB 16GB)")
	print("2. macOS High Serria 10.13.6 (USB 16GB) + WinPE + Tools")
	choice = int(input("Enter your choice: "))
	if (choice == 1):
		print("Coming soon")
		hs()
	elif (choice == 2):
		hs_10_13_6()
	else:
		print("Invalid choice")
		hs()

def hs_10_13_6():
	wget("https://www.dropbox.com/s/v6q60o5mhssrye0/HSVN-macOS%20High%20Serria%2010.13.6%2BWinPE%2BTools.dmg?dl=0", "macOS High Serria 10.13.6 (USB 16GB) + WinPE + Tools.dmg")