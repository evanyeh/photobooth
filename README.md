# Photobooth

A web photobooth app that takes multiple pictures over USB using any camera compatible with gphoto2. Pictures are transferred to the host immediately and displayed on screen. Users can also email session pictures to themselves.

### General Flow

There are 3 main html pages:
1. idle.html - what users see when they first walk up to photobooth with a `Start` button
2. capture.html - directed to after `Start` is selected. shows countdown, takes the picture, shows the picture for review, repeat countdown
3. distribute.html - directed to after a fixed number of pictures are captured in capture.html. prompts for email address(es) to send pictures to then redirects back to idle.html

### Initial Setup
* email account setup
  1. Create new gmail account for event (recommended) or use existing
  2. Allow less secure apps in gmail [settings](https://support.google.com/accounts/answer/6010255?hl=en)

* `config_file.py` setup
  1. adjust constants in `config_file.py` to your liking!

* setup on host
	1. `sudo apt-get update`
	2. `sudo apt-get install gphoto2`
	3. To check installation: run `gphoto2 --auto-detect`
		* which should list the connected camera e.g. `Nikon DSC D5300`
		* if the camera is not listed, try restarting the camera
  4. Setup python virtual environment
      ```
      python3 -m venv venv
      source venv/bin/activate
      pip3 install flask
      pip3 install sh
      pip3 install flask-bootstrap
      ```
  5. Run `python3 photobooth.py`
  6. View app on http://127.0.0.1:5000/
    
* setup on Nikon D5300:
	1. Turn camera on
	2. Connect to host computer via USB
  3. Setup camera settings to how you want it, the app just "presses" the shutter button for you
     * Notes:
       * .jpg images are expected, can figure out in `camera.py` if you want something else
       * There is lag between computer sending out capture command to the camera actually capturing. Account for this in `config_file.trigger_pre_count`, increase if camera is firing after counting down to 0
       * Transfering the captured image to the computer takes a long time! Two mitigations:
         * Select lower picture quality in your camera, lower megapixel count or higher compression
         * Increase `config_file.time_between_pictures` to allow for more time to review the captured image in between captures
     * Tips:
       * Set to Manual mode with auto focus
       * Having up-firing flash really helps with the look!


### below outdated but good info on using gphoto2 from terminal

### Configuring Picture Save Location

gphoto2 defaults to the internal RAM as the save location. Run the following to view the save location.

`gphoto2 --get-config capturetarget`

example output:

```
Label: Capture Target
Type: RADIO
Current: Internal RAM
Choice: 0 Internal RAM
Choice: 1 Memory Card
```

Run the following to change the save location.

`gphoto2 --set-config capturetarget=1`

Then run `gphoto2 --get-config capturetarget` to verify changed save location.

### Helpful gphoto2 commands:

```
gphoto2 --auto-detect
gphoto2 --trigger-capture
gphoto2 --get-config capturetarget
gphoto2 --set-config capturetarget=
gphoto2 --list-files
gphoto2 --get-all-files
gphoto2 --folder="/folder/of/pics" -R --delete-all-files
```
