import requests
import subprocess
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

# get api github
def getApiGithub(url_link):
    response = requests.get(url_link)
    return response.json()

# print latest version
def getLatestVersion(url_link):
    data = getApiGithub(url_link)
    return data["tag_name"]

def wget(url, patch):
    cmd = subprocess.call(["wget", url, "-O", str(downloads_path)+"/"+patch])