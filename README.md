# Tool Dowload

Write = Python

# how to install python
Python  >= 3.8

# install ENV for windows
```
iex((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/Github-Aiko/HSVN-tools/dev/install.ps1'))
```

## Hướng dẫn cài
```
git clone https://github.com/Github-Aiko/HSVN-tools.git
# Bạn cần cài đặt nó pip3 Quản lý túi
cd HSVN-tools
pip3 install -r requirements.txt
python3 hsvn.py
```

## build file 
```
pyinstaller --onefile hsvn.py
```