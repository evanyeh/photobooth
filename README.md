# Photobooth

This repo allows the control of a Nikon D5300 over USB using a Raspberry Pi (Zero W).


### Initial Setup

* setup on Raspberry PI:
	1. `sudo apt-get update`
	2. `sudo apt-get install gphoto2`
	3. `sudo pip3 install sh`
	4. To check installation: run `gphoto --auto-detect`
		* which should list the connected camera e.g. `Nikon DSC D5300`
		* if the camera is not listed, try restarting the camera

* setup on Nikon D5300:
	1. None.


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
gphoto2 --set-config capturetarget
gphoto2 --list-files
gphoto2 --get-all-files
gphoto2 --folder="/folder/of/pics" -R --delete-all-files
```

```
python3 -m venv venv
source venv/vin/activate
pip3 install flask
pip3 install python-dotenv
pip3 install -v gphoto2
pip3 install flask-bootstrap
```

If get "No such file or directory: 'pkg-config': 'pkg-config'" during pip3 install -v gphoto2, then run
```
sudo apt install pkg-config
pip3 install --upgrade setuptools
pip3 install ez_setup


```
sudo apt install linuxbrew-wrapper
brew install pkg-config
```


Run with `flask run` or `python photobooth.py`


