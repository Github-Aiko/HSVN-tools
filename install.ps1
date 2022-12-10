# check if python is installed
$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
	Write-Host "Python is already installed"
	exit
}

# download python
$python = Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe" -OutFile "python-3.11.0-amd64.exe"

# install python
Start-Process -FilePath "python-3.11.0-amd64.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# check if python is installed
$python = Get-Command python -ErrorAction SilentlyContinue

if ($python) {
	Write-Host "Python is installed"
} else {
	Write-Host "Python is not installed"
}

# remove python installer
Remove-Item "python-3.11.0-amd64.exe"

# install pip
Start-Process -FilePath "python.exe" -ArgumentList "-m pip install --upgrade pip" -Wait

# install python-tk, pyinstaller
Start-Process -FilePath "python.exe" -ArgumentList "-m pip install python-tk pyinstaller pathlib wget" -Wait

# install pyinstaller
Start-Process -FilePath "python.exe" -ArgumentList "-m pip install pyinstaller" -Wait

