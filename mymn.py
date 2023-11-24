import curses
import os
import sys
import time

import commands
import rooms
import game

from term import Term

def parse_args(args):
    config = {}

    for arg in args:
      if arg == "-f":
          config["FAST"] = True
      elif arg == "-t":
          config["VERBOSE"] = True
      else:
          config["BEGIN"] = arg

    return config

def begin():
    config = parse_args(sys.argv[1:])
    try:
        Term.initialize(config.get("FAST"),
                        config.get("VERBOSE"))
        Term.trace("initialized terminal")

        g = game.Game(config.get("BEGIN"))
        g.run()
    finally:
        Term.restore()

begin()
