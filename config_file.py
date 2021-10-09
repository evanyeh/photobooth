################################ Image capture #################################
# for displaying in idle photobooth page
event_name = "Suite 214 Picnic"
# for creating a subfolder under some larger photobooth directory, see album_location
session_name = "winterpicnictest"
# where all the photos are saved, should be auto-created if doesn't already exist
album_location = "/home/evan/Pictures/photobooth/" + session_name + "/"
# time in seconds to wait for an image to come back from frontend (non-neg any)
image_timeout = 6
# total number of pictures to take in each session (pos int)
num_pictures = 1
# computer will send capture command when countdown timer is at <trigger_pre_count>
# bc there is lag between command and realization. (non-neg int)
trigger_pre_count = 2
# countdown time in seconds before each picture (pos int)
countdown_time = 5
# time in seconds between each picture (pos any)
time_between_pictures = 6

################################# Web Styling ##################################
# can browse https://fonts.google.com/ for ez fonts
styling = { \
"font_file" : "https://fonts.googleapis.com/css?family=Itim&display=swap", \
"font_name" : "Itim", \
"primary_bg_color" : "8cb9b6", \
"secondary_bg_color" : "dad2bf", \
"primary_font_color" : "000000", \
"secondary_font_color" : "f45a24"}

############################# Image distirbution ###############################
# email info to send out pictures right after theyre taken
# gmail works pretty well, but have to allow "Less secure apps" in gmail settings
# https://support.google.com/accounts/answer/6010255?hl=en
email_username = "username@website.com"
email_password = "password"
# pseudonym that replaces email_username 
email_from = "Suite 214 (:"
email_subject = 'Suite 214 Picnic Photos'
# write body in HTML
email_body = '<p>Thanks for hanging out with us! We hope you had a good time (:&nbsp;</p><p>  <br></p><p>  <a href="https://twitter.com/MichaelaOkla/status/1195771517868498944">hav a gud winter term</a>,</p><p>'
# routes.py/send_mail() will shuffle the below names and append it to the email_body
# so no member gets preferential ordering :)
signature_members = ['Daniel', 'Evan', 'Alex', 'Esther', 'Yoojin', 'Brandon']

# Development
DEBUG_MODE = False # primarily for bypassing camera intiation
