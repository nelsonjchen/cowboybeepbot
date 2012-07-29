import astral
import praw
import os

ucsb = astral.City(('University of California, Santa Barbara Main Campus',
                    'USA', 34.41254, -119.84813, 'US/Pacific'))

user = os.environ['REDDIT_USER']
password = os.environ['REDDIT_PASS']
subreddit = os.environ['REDDIT_SUBREDDIT']

r = praw.Reddit("UCSB Subreddit Style Bot aka. CowboyBeepBopBot")
r.login(user, password)

if (ucsb.solar_elevation() > 0):
    print("day!")
else:
    print("night!")
