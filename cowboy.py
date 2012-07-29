import astral
import praw
import os

ucsb = astral.City(('University of California, Santa Barbara Main Campus',
                    'USA', 34.41254, -119.84813, 'US/Pacific'))

user = os.environ['REDDIT_USER']
password = os.environ['REDDIT_PASS']
subreddit = os.environ['REDDIT_SUBREDDIT']


if (ucsb.solar_elevation() > 0):
    css_filename = 'stylesheets/day.css'
else:
    css_filename = 'stylesheets/day.css'

mkdn_filename = 'markdown/sidebar.mkdn'

print("Uploading %s and %s to %s" % (css_filename, mkdn_filename, subreddit))
print("WARNING: This script has no error checking. Please make sure files work!")

r = praw.Reddit("UCSB Subreddit Style Bot aka. CowboyBeepBopBot")
r.login(user, password)

with open(css_filename, 'r') as file:
    style = file.read()

with open(mkdn_filename, 'r') as file:
    sidebar = file.read()

sr = r.get_subreddit(subreddit)
print("Got subreddit %s" % subreddit)

sr.update_settings(description = sidebar)
print("Updated sidebar for subreddit %s" % subreddit)

sr.set_stylesheet(style)
print("Updated Stylesheet for subreddit %s" % subreddit)

print(datetime.datetime.now().ctime())

print("Success for %s" % subreddit)
