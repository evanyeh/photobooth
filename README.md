# Photobooth

A web photobooth app that takes multiple pictures over USB using any camera compatible with gphoto2. Pictures are transferred to the host immediately and displayed on screen. Users can also email session pictures to themselves.


### Initial Setup

* setup on host:
	1. `sudo apt-get update`
	2. `sudo apt-get install gphoto2`
	3. To check installation: run `gphoto --auto-detect`
		* which should list the connected camera e.g. `Nikon DSC D5300`
		* if the camera is not listed, try restarting the camera
    4. Setup python virtual environment
    ```
    python3 -m venv venv
    source venv/vin/activate
    pip3 install flask
    pip3 install sh
    ```
    5. Run `python3 photobooth.py`
    6. View app on http://127.0.0.1:5000/
    
* setup on Nikon D5300:
	1. Turn on.


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
