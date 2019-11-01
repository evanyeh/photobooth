from flask import render_template, url_for, request, redirect, current_app
from app import app
import os
import base64 # for image displaying

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
    # return image
    with current_app.open_resource("dog.jpg") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string

@app.route('/distribute')
def distribute():
    return "get emails and distribute here"

@app.route('/idle')
def idle():
    return "prompt for user to start process"
