setup.py

heroku create myapp --buildpack heroku/python

$ python -V
Python 3.7.2

import os
import time
import sys
print ("Howdy yall, my name is Jessie! Which one of my friends have found today?")

def main():
    while True:
        TSCN = input ("Enter name: ")

        if TSCN == 'Slinky':
            print ("Slinky had 12!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Little Bo Peep':
            print ("Little Bo Peep had 2!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Mr Potato Head':
            print ("Mr Potato Head had 5!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Rex':
            print ("Rex had 12!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Woody':
            print ("Woody had 21!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Aliens':
            print ("Aliens had 5!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Andy':
            print ("Andy had 25!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Buzz':
            print ("Buzz had 19!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Buzz Lightyear':
            print ("Buzz Lightyear had 19!")
            logged()
        else:
           time.sleep(0.0000000001)

        if TSCN == 'Bullseye':
            print ("I can't believe I lost Bullseye, how silly of me! Anyway I wish to congratulate you on finishing the treasure hunt!")
            print ("Well done!")
            time.sleep(5)
            sys.exit()
        else:
           time.sleep(0.0000000001)

def logged():
    time.sleep(0.5)
    print ("Have you found another friend of mine or who I am missing?")

main()
