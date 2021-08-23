#
#chore_reminder
# Author: Sydney Wells (rosescript)
# this program turns a CircuitPlayground Express
# into a chore reminder app. The app asks if you've
# done a chore, and if so you get a nice little zelda
# sound, but if not you get an annoying fairy yelling
# at you :)
#

# imports
from adafruit_circuitplayground import cp
import random
import time

#
# chores_done()
# function that asks the user if they have done their chore for the day,
# if yes (if user presses button A), the user is congratulated,
# if no (if user presses button B), the CPX will scream
#

def chores_done():

    # asks if chores are done
    cp.play_file("chores.wav")

    # turning down the brightness bc I got sensitive eyes
    cp.pixels.brightness = 0.03

    while True:
        if cp.button_a: # if the user presses A

            # give 'em some pretty lights
            cp.pixels.fill((30, 212, 23))

            # give 'em that sense of accomplishment you feel when you pick up the big key in the dungeon
            cp.play_file("zelda-item.wav")

            cp.pixels[0] = (255, 255, 255)
            cp.pixels[1] = (245, 234, 27)
            cp.pixels[2] = (30, 212, 23)
            cp.pixels[3] = (255, 255, 255)
            cp.pixels[4] = (245, 234, 27)
            cp.pixels[5] = (30, 212, 23)
            cp.pixels[6] = (255, 255, 255)
            cp.pixels[7] = (245, 234, 27)
            cp.pixels[8] = (30, 212, 23)
            cp.pixels[9] = (255, 255, 255)
            time.sleep(2)

            # lights out
            cp.pixels.fill((0, 0, 0))

        if cp.button_b: # if the user presses B

            # turn into navi (aka the annoying fairy)
            cp.pixels.fill((18, 255, 219))

            # ah, the screams
            for i in range(2): # for the sake of my sanity I have set this to 5, but ideally you'd want to run it 50-100 times, to really motivate you to get those chores done.
                cp.play_file("zelda-navi-listen.wav")
            time.sleep(2)

            # lights out
            cp.pixels.fill((0, 0, 0))


# now lets run it!
chores_done()

