################################ Image capture #################################
# for displaying in idle photobooth page
event_name = "Happy Birthday!!"
# for creating a subfolder under some larger photobooth directory, see album_location
session_name = "2022-02-19 Feb Birthday"
# where all the photos are saved, should be auto-created if doesn't already exist
album_location = "/home/evan/Pictures/photobooth/" + session_name + "/"
# time in seconds to wait for an image to come back from frontend (non-neg any)
image_timeout = 6
# total number of pictures to take in each session (pos int)
num_pictures = 3
# computer will send capture command when countdown timer is at <trigger_pre_count>
# bc there is lag between command and realization. (non-neg double in seconds, must be <= countdown_time)
# but countdown only goes 100ms at a time
trigger_pre_count = 1.6
# countdown time in seconds before each picture (pos int)
countdown_time = 5
# time in seconds between each picture, to allow photo transfer and review (pos any)
time_between_pictures = 6

################################ Google Photos #################################
google_photos_album_name = "2022 Avery Bay Birthdays"

################################# Web Styling ##################################
# can browse https://fonts.google.com/ for ez fonts
styling = { \
"font_file" : "https://fonts.googleapis.com/css2?family=Neucha&display=swap", \
"font_name" : "Neucha", \
"primary_bg_color" : "#2D3047", \
"secondary_bg_color" : "#ED217C", \
"primary_font_color" : "#FFFD82", \
"secondary_font_color" : "#1B998B"}

############################# Image distirbution ###############################
# email info to send out pictures right after theyre taken
# gmail works pretty well, but have to allow "Less secure apps" in gmail settings
# https://support.google.com/accounts/answer/6010255?hl=en
email_username = "username@website.com"
email_password = "password"
# pseudonym that replaces email_username 
email_from = "evan's photobooth"
email_subject = '2022 Avery Bay Birthday Photos'
# write body in HTML
email_body = '<p>Your photos are attached! View the complete album here: <a href="https://photos.app.goo.gl/inBB8pB21WQKUzmz8">https://photos.app.goo.gl/inBB8pB21WQKUzmz8</a></p><p>Happy birthday '
# routes.py/send_mail() will shuffle the below names and append it to the email_body
# so no member gets preferential ordering :)
signature_members = ['Betty', 'Miriam', 'Rachel', 'Tanvi']

# Development
DEBUG_MODE = False # primarily for bypassing camera intiation
