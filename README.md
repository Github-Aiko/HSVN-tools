# Tool Dowload

Write = Python

# how to install python
Python  >= 3.8

# install ENV for windows 
Run powershell as admin
```
$ScriptFromGitHub = Invoke-WebRequest https://raw.githubusercontent.com/Github-Aiko/HSVN-tools/dev/install.ps1
Invoke-Expression $($ScriptFromGitHub.Content)
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

- Build file 1 lần và chạy nhiều lần cho dù bạn có reset windows và mất môi trường còn file là còn chạy dc nhé :D 