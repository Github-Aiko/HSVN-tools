from app.environment.env import * 

def wget(url, filename):
    cmd = subprocess.call(["wget", url, "-O", str(downloads_path)+"/"+filename])