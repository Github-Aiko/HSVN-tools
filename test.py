from pathlib import Path
import subprocess

downloads_path = str(Path.home() / "Downloads")

print(downloads_path)

# open downloads folder
def opendownloads():
	cmd = subprocess.call(["open", downloads_path])

# main
def main():
	opendownloads()

if __name__ == "__main__":
	main()
