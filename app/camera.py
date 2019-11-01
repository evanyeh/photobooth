from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

# Kill the gphoto2 process that starts whenever we connect the camera.
def killgphoto2process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # Search for the line that has the process we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # Kill the process
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)


shot_date = datetime.now().strftime("%Y.%m.%d")
shot_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
picID = "testpics"

clearCommand = ["--folder", "/store_00010001/DCIM/100D5300", "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]

folder_name = picID + shot_date
save_location = "/home/pi/Desktop/gphoto2/images/" + folder_name 

def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("failed to create the new directory")
    os.chdir(save_location)

def captureImages():
    gp(triggerCommand)
    sleep(3)
    gp(downloadCommand)
    gp(clearCommand)

def renameFiles(ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith(".JPG"):
                os.rename(filename, (ID + "_" + shot_time + ".JPG"))
                print("Renamed the JPG")

 
killgphoto2process()
gp(clearCommand)
createSaveFolder()
captureImages()
renameFiles(picID)
