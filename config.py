import sys
import curses

CONFIG = {}

def parse_args():
    for arg in sys.argv:
      if arg == "-f":
          CONFIG["FAST"] = True
      elif arg == "-t":
          CONFIG["VERBOSE"] = True
      else:
          CONFIG["BEGIN"] = arg

# to get regular line output we may need to https://stackoverflow.com/questions/14010073/print-to-standard-console-in-curses
def setup_screen(window):
    window.scrollok(1)
    curses.echo()
    curses.nocbreak()
    curses.noraw()
    curses.nl()
    curses.curs_set(1) # visible normal cursor
    curses.def_shell_mode()

    curses.noecho()
    curses.def_prog_mode()

    curses.reset_shell_mode()
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN, -1)

    print("curses config " + repr(window))
    print("next line")
      
    
