import astral
import praw

ucsb = astral.City(('University of California, Santa Barbara Main Campus',
                    'USA', 34.41254, -119.84813, 'US/Pacific'))

if (ucsb.solar_elevation() > 0):
    print("day!")
else:
    print("night!")
