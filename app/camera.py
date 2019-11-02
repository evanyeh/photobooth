from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

clearCommand = ["--folder", "/store_00010001/DCIM/100D5300", "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]
captureAndDownloadCommand = ["--capture-image-and-download", "--filename", "name.JPG"]
save_location = ""
# Kill the gphoto2 process that starts whenever we connect the camera.
def kill_gphoto2_process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # Search for the line that has the process we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # Kill the process
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)

def init(album_location):
    kill_gphoto2_process()
    create_save_folder(album_location)

def create_save_folder(album_location):
    try:
        os.makedirs(album_location)
    except:
        print("failed to create the new directory")

def capture_image(album_location):
    img_path = album_location + datetime.now().strftime("%Y.%m.%d %H:%M:%S") + ".JPG"
    captureAndDownloadCommand[2] = img_path
    gp(captureAndDownloadCommand)
    return img_path

# def captureImages():
#     gp(triggerCommand)
#     sleep(3)
#     gp(downloadCommand)
#     gp(clearCommand)
#
# def renameFiles(ID):
#     shot_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
#     for filename in os.listdir("."):
#         if len(filename) < 13:
#             if filename.endswith(".JPG"):
#                 os.rename(filename, (ID + "_" + shot_time + ".JPG"))
#                 print("Renamed the JPG")


# killgphoto2process()
# gp(clearCommand)
# createSaveFolder()
# captureImages()
# renameFiles(picID)
