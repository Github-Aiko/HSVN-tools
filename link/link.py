from os import system
import subprocess
from app.system.systemcheck import checkOS

def wget(url, patch):
    cmd = subprocess.call(["wget", url+"&download=1", "-O", patch])

def monterey12_6_1():
    wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EXTteLmivBhKhA8Z_vaOA8sBFmhhRPZvBGykIHoOwTw_mQ?e=qmvVWd", "macOS Monterey 12.6.1 (USB 16GB).dmg")

def bigsur11_7():
    wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/ERN5On2Wf2NIjOqe21omCegB7QPgWqhw76maMKsRVUyolQ?e=0oJ755", "macOS Big Sur 11.7 (USB 16GB).dmg")

def catalina10_15_7():
    wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/Ea8X8mJf9u9Arzs2nFg6pA0Bkx9rLg0HvopQNGbx4cH53w?e=HpzN1f", "macOS Catalina 10.15.7 (USB 16 GB).dmg")

def mojave10_14_6():
    wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/ESdDKYGVOppKjD9bklHF2qcBwCNUn1pho5MUFTN8zOQneQ?e=Ra8DVw", "macOS Mojave 10.14.6 + WinPE (USB 16 GB).dmg")

def highsierra10_13_6():
    wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EaCfUlLIGjZAkb0bPvr8t80BuQVw1egRYB-kB7gi6fkEvg?e=aaiTY2", "macOS High Sierra 10.13.6 + WinPE + HSVN Tools (USB 8 GB).dmg")

def ventura13():
    wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/ERdJvGDdRalChUf2UgHaTw8BPlh0V4SgQvZbPnH2sUzhDg?e=izPjZO", "macOS Ventura 13.0.0 (USB 16GB).dmg")

def tools():
    if checkOS() == "Darwin":
        wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EUw0nZE6EohGlttwfe--N8YBtiaHESwaxeTfZR31qU7DCA?e=kBq6gC", "MacOS-Tools.zip")
    elif checkOS() == "Linux":
        wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EY12YmQAAZhFkfn0ptQzMy4B7YZ_JiTp6TNmR_xXKxbXFg?e=iuCpLu", "Linux-Tools.zip")
    elif checkOS() == "Windows":
        wget("https://aikocute-my.sharepoint.com/:u:/g/personal/aiko_aikocute_onmicrosoft_com/EcTPCZNbVZtDuZ8XPXz-i-QB3It5CMcsiO4pU7KAq5iLyw?e=fJNzJ5", "Windows-Tools.zip")
