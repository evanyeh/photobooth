################################ Image capture #################################
# for displaying in idle photobooth page
event_name = "Humpty Dumpty Had a Great Fall"
# for creating a subfolder under some larger photobooth directory, see album_location
session_name = "2022-11-19 Humpty Dumpty Fall Party"
# where all the photos are saved, should be auto-created if doesn't already exist
album_location = "/home/evan/Pictures/photobooth/" + session_name + "/"
# time in seconds to wait for an image to come back from frontend (non-neg any)
image_timeout = 6
# total number of pictures to take in each session (pos int)
num_pictures = 3
# computer will send capture command when countdown timer is at <trigger_pre_count>
# bc there is lag between command and realization. (non-neg double in seconds, must be <= countdown_time)
# but countdown only goes 100ms at a time
trigger_pre_count = 1.3
# countdown time in seconds before each picture (pos int)
countdown_time = 4
# time in seconds between each picture, to allow review (pos any)
time_between_pictures = 3

################################ Google Photos #################################
google_photos_album_name = "2022 Humpty Dumpty Had a Great Fall"

################################# Web Styling ##################################
# can browse https://fonts.google.com/ for ez fonts
styling = { \
"font_file" : "https://fonts.googleapis.com/css?family=Gloria+Hallelujah&display=swap", \
"font_name" : "Gloria Hallelujah", \
"primary_bg_color" : "#d98e71", \
"secondary_bg_color" : "#f5e4ae", \
"primary_font_color" : "#ffffff", \
"secondary_font_color" : "#836953"}

############################# Image distirbution ###############################
# email info to send out pictures right after theyre taken
# gmail works pretty well, but have to allow "Less secure apps" in gmail settings
# https://support.google.com/accounts/answer/6010255?hl=en
email_username = "username@website.com"
email_password = "password"
# pseudonym that replaces email_username 
email_from = "evan's photobooth"
email_subject = '2022 Humpty Dumpty Had a Great Fall'
# write body in HTML
email_body = '<p>Your photos are attached! View the complete album here: <a href="https://photos.app.goo.gl/SPb49krwt7hEtfd89">https://photos.app.goo.gl/SPb49krwt7hEtfd89</a></p><p>Your friends, </p><p>'
# routes.py/send_mail() will shuffle the below names and append it to the email_body
# so no member gets preferential ordering :)
signature_members = ['Evan', 'Daniel', 'Asim']

# Development
DEBUG_MODE = False # primarily for bypassing camera intiation
