from flask import render_template, url_for, request, redirect, current_app
from app import app
import os
import base64 # for image displaying
import datetime # for timing out
import time
from . import camera

session_name = "fall"
album_location = "/home/evan/Pictures/photobooth/" + session_name + "/"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/preview')
def preview():
    return "show preview screen here"

@app.route('/capture')
def capture_sequence():
    camera.init(session_name)
    return render_template('capture.html')

# @app.route('/background_process_test')
# def background_process_test():
#     # trigger capture
#     # return image
#     with current_app.open_resource("dog.jpg") as img_file:
#         my_string = base64.b64encode(img_file.read())
#     return my_string

@app.route('/trigger_and_return_picture')
def trigger_and_return_picture():
    # trigger capture
    img_path = camera.capture_image(album_location)

    # wait for image to come in
    start_time = datetime.datetime.now()
    while not os.path.exists(img_path):
        # wait here
        if (datetime.datetime.now() - start_time).total_seconds() > 6:
            print("Timeout")
            break

    # return image
    with open(img_path, 'rb') as img_file:
        img_string = base64.b64encode(img_file.read())

    return img_string

@app.route('/distribute')
def distribute():
    return "get emails and distribute here"

@app.route('/idle')
def idle():
    return "prompt for user to start process"
