import subprocess,sys
def install(package):
    
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-check","-q", "install", package])

install('pygobject')