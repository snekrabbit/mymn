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
        term = Term(config.get("FAST"), config.get("VERBOSE"))
        term.trace("initialized terminal")

        g = game.Game(term, config.get("BEGIN"))
        g.run()
    finally:
        Term.restore()

begin()
