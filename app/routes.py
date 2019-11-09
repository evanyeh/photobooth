from flask import render_template, url_for, request, redirect, current_app
from app import app
import os
import base64 # for image displaying
import datetime # for timing out
import time
import random
from app import camera
import config_file
import threading # for avoiding email sending wait
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
    del user_images[:]
    return render_template('idle.html')

@app.route('/capture')
def capture_sequence():
    del user_images[:]
    try:
        camera.init(config_file.album_location)
    except:
        print('---------CAMERA INIT FAILED')
        return redirect('/idle')
    return render_template('capture.html')

@app.route('/trigger_and_return_picture')
def trigger_and_return_picture():
    failed = False
    # trigger capture
    try:
        img_path = camera.capture_image(config_file.album_location)
    except:
        failed = True
        print('---------CAMERA CAPTURE FAILED')

    if not failed:
        # wait for image to come in
        start_time = datetime.datetime.now()
        while not os.path.exists(img_path):
            # wait here
            if (datetime.datetime.now() - start_time).total_seconds() > 6:
                print("--------- TIMEOUT")
                failed = True
                break

    # failed image
    if failed:
        img_path = 'app/static/fail/esther.JPG'

    user_images.append(img_path)

    with open(img_path, 'rb') as img_file:
            img_string = base64.b64encode(img_file.read())

    return img_string

@app.route('/distribute')
def distribute():
    print("---------PICTURES TAKEN:" + str(user_images))
    return render_template('distribute.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    # send email here
    mail = threading.Thread(target=send_mail, args=(email,user_images.copy()))
    mail.start()
    del user_images[:]
    return redirect('/idle')

def send_mail(recipient, user_images_copy):
    msg = MIMEMultipart()
    msg['Subject'] = 'Suite 214 Fall is Life Gathering Photos'
    msg['From'] = "Suite 214 (:"
    msg['To'] = recipient

    # build email message
    suite_members = ['Daniel', 'Evan', 'Alex', 'Esther', 'Yoojin', 'Brandon']
    random.shuffle(suite_members)
    body = '<p>Thanks for hanging out with us! We hope you had a good time (:&nbsp;</p><p>  <br></p><p>  <a href="https://youtu.be/eupRD3QD6yM?t=92">Season\'s greetings</a>,</p><p>'
    body += ', '.join([str(elem) for elem in suite_members]) + '</p>'

    text = MIMEText(body, 'html')
    msg.attach(text)
    log = open(config_file.album_location + 'user_log.txt','a+')
    log.write(recipient+'\n')
    for i in user_images_copy:
        log.write(i+'\n')
        img_data = open(i, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(i), _subtype="jpg")
        msg.attach(image)
    log.close()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(config_file.email_username, config_file.email_password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
