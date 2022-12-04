from app.efi.getapiefi import *
from app.efi.getapiefi import *

def efiopencore():
    # dowload efi opencore latest
    str(wget("https://github.com/acidanthera/OpenCorePkg/releases/download/"+getLatestVersion("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest")+"/OpenCore-"+getLatestVersion("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest")+"-RELEASE.zip", "OpenCore-"+getLatestVersion("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest")+"-RELEASE.zip"))

def eficlover():
    # dowload efi clover latest
    str(wget("https://github.com/CloverHackyColor/CloverBootloader/releases/download/"+getLatestVersion("https://api.github.com/repos/CloverHackyColor/CloverBootloader/releases/latest")+"/CloverV2-"+getLatestVersion("https://api.github.com/repos/CloverHackyColor/CloverBootloader/releases/latest")+".zip" , "CloverV2-"+getLatestVersion("https://api.github.com/repos/CloverHackyColor/CloverBootloader/releases/latest")+".zip"))
    
