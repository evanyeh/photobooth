from flask import render_template, url_for, request, redirect, current_app
from app import app
import os
import base64 # for image displaying
import datetime # for timing out
import random
from app import camera
import config_file
import threading # for avoiding email sending wait
# for email sending
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# a list of filepaths of images taken in a current picture-taking session
user_images = []

'''
root and /idle show welcome screen to start a picture-taking session
'''
@app.route('/')
@app.route('/index')
def index():
    return redirect('/idle')

@app.route('/idle')
def idle():
    del user_images[:]
    return render_template('idle.html', \
        styling=config_file.styling, \
        event_name=config_file.event_name)

'''
Clears sessions image filepaths, initiates gphoto2 camera settings, renders
picture taking page with countdown text block and image review screen
'''
@app.route('/capture')
def capture_sequence():
    del user_images[:]
    try:
        camera.create_save_folder(config_file.album_location)
        camera.init()
    except:
        print('---------CAMERA INIT FAILED')
        if not config_file.DEBUG_MODE:
            return redirect('/idle')
    return render_template('capture.html', \
        styling=config_file.styling, \
        num_pictures=config_file.num_pictures, \
        countdown_time=config_file.countdown_time, \
        trigger_pre_count=config_file.trigger_pre_count, \
        time_between_pictures=config_file.time_between_pictures)

'''
Called by javascript in /capture to attempt to capture and download
an image, log the filepath, return the base64 encoded image
'''
@app.route('/trigger_and_return_picture')
def trigger_and_return_picture():
    failed = False
    try:
        img_path = camera.capture_image(config_file.album_location)
    except:
        failed = True
        print('--------- CAMERA CAPTURE FAILED')

    if not failed:
        # wait for image to come in
        start_time = datetime.datetime.now()
        while not os.path.exists(img_path):
            # wait here
            if (datetime.datetime.now() - start_time).total_seconds() > config_file.image_timeout:
                print('--------- TIMEOUT')
                failed = True
                break

    # failed image
    if failed:
        img_path = 'app/static/fail/esther.JPG'

    # add taken image to list of filepaths from current session
    user_images.append(img_path)

    # encode in base64 for returning to image review screen
    with open(img_path, 'rb') as img_file:
            img_string = base64.b64encode(img_file.read())

    return img_string

'''
Distribution page that prompts for email or allows user to skip
'''
@app.route('/distribute')
def distribute():
    print('--------- PICTURES TAKEN:' + str(user_images))
    return render_template('distribute.html', styling=config_file.styling)

'''
Called after submitting email form and starts an email-sending thread before
immediately redirecting to standy page (/idle)
'''
@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email'].strip(" ").split(";")
    # send email as separate thread so browser does not get hung up on this page
    # waiting for large attachments to send
    mail = threading.Thread(target=send_mail_thread, args=(email,user_images.copy()))
    mail.start()
    # done with current session, clear filepaths
    del user_images[:]
    return redirect('/idle')

'''
Sends an email to a recipient with images in user_images_copy attached
'''
def send_mail_thread(recipient, user_images_copy):
    msg = MIMEMultipart()
    msg['Subject'] = config_file.email_subject
    msg['From'] = config_file.email_from

    # build email message
    body = config_file.email_body
    # shuffle the order of the suite members for the signature
    signature_members = config_file.signature_members
    random.shuffle(signature_members)
    body += ', '.join([str(elem) for elem in signature_members]) + '</p>'

    text = MIMEText(body, 'html')
    msg.attach(text)
    # log which email and which pictures are sent
    log = open(config_file.album_location + 'user_log.txt','a+')
    log.write(datetime.datetime.now().strftime('%Y-%m-%d %T') + '\n')
    log.write(str(recipient)+'\n')
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
    for r in recipient:
        s.sendmail(msg['From'], r, msg.as_string())
        print("---------EMAIL SENT TO: " + r)

    s.quit()
