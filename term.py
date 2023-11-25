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
    def __init__(self, fast=False, verbose=False):
        self.fast = fast
        self.verbose = verbose
        self.win = init_curses()

    def restore(self):
        curses.endwin()

    def clear(self):
        self.win.refresh()

    def input(self, msg=""):
        self.print(msg)
        return self.win.getstr().decode("utf-8")

    def print(self, msg, end=""):
        print(msg, end=end)
        sys.stdout.flush()

    def println(self, msg=""):
        self.print(msg, end="\n\r")

    def trace(self, msg):
        if self.verbose:
            self.println("### " + msg)

    def prompt_until(self, msg, until, tries=4):
        self.say(msg)
        count = 1
        while count < tries:
            count = count+1
            self.print("> ")
            i = input()
            if i == until:
                return True
            else:
                self.say("INCORRECT\n"+str(tries-count)+" TRIES LEFT")
        if count == tries:
            return False

    def say(self, msg, char_wait=0.01, line_wait=1):
        # os.system("say "+msg)
        last_c = None
        for c in msg:
            self.print(c)
            if c == "\n":
                if last_c == "\n":
                    continue
                else:
                    self.nap(line_wait)
                    self.println("")
            else:
                self.nap(char_wait)
            last_c = c
        self.println("")

    def type(self, msg):
        self.nap(1.5)
        self.say(msg, 0.15, 0.15)
        self.nap(0.5)

    def nap(self, secs):
        if self.fast:
            return
        else:
            time.sleep(secs)
