from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

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
    gp(["--capture-image-and-download", "--filename", img_path])
    return img_path
