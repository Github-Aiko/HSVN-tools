from app.system.systemcheck import cleansc
import webbrowser
import app.efi.dowloadefi as dowloadefi
from app.system.systemcheck import *
from app.environment.env import *
from link.tools import *

# import OS
from link.MacOS.monterey import monterey
from link.MacOS.bigsur import bigsur
from link.MacOS.catalina import catalina
from link.MacOS.mojave import mojave
from link.MacOS.hs import hs
from link.MacOS.ventura import ventura


def openLink():
	webbrowser.open("https://www.facebook.com/groups/hackintoshsvn")


def inputNumber():
	cleansc()
	print("Tools Dowload FirmwareMacOS")
	print("Create by HSVN - Hackintosh Vietnam")
	print("1. MacOS 12 Monterey")
	print("2. MacOS 11 Bigsur")
	print("3. MacOS 10 Catalina")
	print("4. MacOS 10 Mojave")
	print("5. MacOS 10 High Sierra")
	print("6. MacOS 13 Ventura")
	print("7. Tools")
	print("8. Efi Newest")
	print("9. Tham gia HSVN - Hackintosh Vietnam")
	print("0. Exit")
	textInput = int(input('Please enter a number: '))

	if (textInput == 1):
		cleansc()
		monterey()
	
	elif (textInput == 2):
		cleansc()
		bigsur()

	elif (textInput == 3):
		cleansc()
		catalina()

	elif (textInput == 4):
		cleansc()
		mojave()

	elif (textInput == 5):
		cleansc()
		hs()

	elif (textInput == 6):
		cleansc()
		ventura()

	elif (textInput == 7):
		cleansc()
		tools()

	elif (textInput == 8):
		print("[1] OpenCore")
		print("[2] Clover")
		print("[3] Back")
		textInput = int(input('Please enter a number: '))
		if (textInput == 1):
			dowloadefi.efiopencore()
		elif (textInput == 2):
			dowloadefi.eficlover()
		elif (textInput == 3):
			inputNumber()
		else:
			print("Can't find the character you entered, do you want to do it again?")
			print("[1] Yes")
			print("[2] No")
			textInput = int(input('Please enter a number: '))
			if (textInput == 1):
				inputNumber()
			elif (textInput == 2):
				exit()
			else:
				inputNumber()

	elif (textInput == 9):
		openLink()
		inputNumber()

	elif (textInput == 0):
		exit()

	else:
		print("Can't find the character you entered, do you want to do it again?")
		print("[1] Yes")
		print("[2] No")
		textInput = int(input('Please enter a number: '))
		if (textInput == 1):
			inputNumber()
		elif (textInput == 2):
			exit()
		else:
			inputNumber()

def wantopenfile():
	cleansc()
	print("Do you want to open the folder?")
	print("[1] Yes")
	print("[2] No")
	textInput = int(input('Please enter a number: '))
	if (textInput == 1):
		openfolder()
		inputNumber()
	else:
		inputNumber()

def main():
	checkwget()
	cleansc()
	inputNumber()
	wantopenfile()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
