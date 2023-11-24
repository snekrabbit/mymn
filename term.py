import curses
import os
import sys
import time

def init_curses():
    win = curses.initscr()

    curses.nocbreak() #wait for enter, "cooked" mode
    curses.echo()
    curses.raw()
    curses.nl()
    # curses.curs_set(0) # invisible cursor or else it will be a lock
    # curses.def_shell_mode()

    # curses.noecho()
    # curses.def_prog_mode()

    # curses.reset_shell_mode()
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN, -1)

    win.scrollok(1)
    win.refresh()
    return win

class Term(object):

    @classmethod
    def initialize(cls, fast=False, verbose=False):
        cls.fast = fast
        cls.verbose = verbose
        cls.win = init_curses()

    @classmethod
    def restore(cls):
        curses.endwin()

    @classmethod
    def clear(cls):
        cls.win.refresh()

    @classmethod
    def input(cls, msg=""):
        Term.print(msg)
        return cls.win.getstr().decode("utf-8")

    @classmethod
    def print(cls, msg, end=""):
        print(msg, end=end)
        sys.stdout.flush()

    @classmethod
    def println(cls, msg=""):
        cls.print(msg, end="\n\r")

    @classmethod
    def trace(cls, msg):
        if cls.verbose:
            cls.println("### " + msg)

    @classmethod
    def prompt_until(cls, msg, until, tries=4):
        cls.say(msg)
        count = 1
        while count < tries:
            count = count+1
            cls.print("> ")
            i = input()
            if i == until:
                return True
            else:
                cls.say("INCORRECT\n"+str(tries-count)+" TRIES LEFT")
        if count == tries:
            return False

    @classmethod
    def say(cls, msg, char_wait=0.01, line_wait=1):
        # os.system("say "+msg)
        last_c = None
        for c in msg:
            cls.print(c)
            if c == "\n":
                if last_c == "\n":
                    continue
                else:
                    cls.nap(line_wait)
                    cls.println("")
            else:
                cls.nap(char_wait)
            last_c = c
        cls.println("")

    @classmethod
    def type(cls, msg):
        cls.nap(1.5)
        cls.say(msg, 0.15, 0.15)
        cls.nap(0.5)

    @classmethod
    def nap(cls, secs):
        if cls.fast:
            return
        else:
            time.sleep(secs)
