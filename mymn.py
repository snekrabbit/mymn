import curses
import os
import commands
import rooms
import utils
import time
import sys
import config
import game

def begin(window):
    config.parse_args()
    #config.setup_screen(window)
    begin_room = config.CONFIG.get("BEGIN") or "the_plane"

    print ("WELCOME TO M Y M N")
    un = input("ENTER USERNAME\n> ")
    print ("WELCOME " + un)

    g = game.Game(un, begin_room)
    g.run()

#curses.wrapper(begin) # resets the terminal to sane values if we exit unexpectedly
begin(None)
