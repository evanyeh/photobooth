from flask import render_template, url_for, request, redirect, current_app
from app import app
import os
import base64 # for image displaying
import datetime # for timing out
import time
import random
from app import camera
import config_file
# for email sending
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

user_images = []

@app.route('/')
@app.route('/index')
def index():
    return redirect('/idle')

@app.route('/preview')
def preview():
    return "show preview screen here"

@app.route('/idle')
def idle():
    return render_template('idle.html')

@app.route('/capture')
def capture_sequence():
    user_images = []
    camera.init(config_file.album_location)
    return render_template('capture.html')

@app.route('/trigger_and_return_picture')
def trigger_and_return_picture():
    failed = False
    # trigger capture
    print('here in trigger and return')
    img_path = camera.capture_image(config_file.album_location)

    # wait for image to come in
    start_time = datetime.datetime.now()
    while not os.path.exists(img_path):
        # wait here
        if (datetime.datetime.now() - start_time).total_seconds() > 6:
            print("Timeout")
            failed = True
            break

    # return image
    if not failed:
        user_images.append(img_path)
    else:
        img_path = 'app/esther.jpg'

    with open(img_path, 'rb') as img_file:
            img_string = base64.b64encode(img_file.read())

    return img_string

@app.route('/distribute')
def distribute():
    print(user_images)
    return render_template('distribute.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    print(user_images)
    email = request.form['email']
    # send email here
    send_mail(email)
    return redirect('/idle')

def send_mail(recipient):
    msg = MIMEMultipart()
    msg['Subject'] = 'Bechtel 214 Fall is Life Gathering Photos'
    msg['From'] = config_file.email_username
    msg['To'] = recipient

    suite_members = ['Daniel', 'Evan', 'Alex', 'Esther', 'Yoojin', 'Brandon']
    random.shuffle(suite_members)

    text = MIMEText('Hope you have a wonderfull fall! \n\nSeasons greetings,\nSuite 214\n' + ', '.join([str(elem) for elem in suite_members]))
    msg.attach(text)
    log = open(config_file.album_location + 'user_log.txt','a+')
    log.write(recipient+'/n')
    for i in user_images:
        log.write(i+'/n')
        img_data = open(i, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(i))
        msg.attach(image)
    log.close()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(config_file.email_username, config_file.email_password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
