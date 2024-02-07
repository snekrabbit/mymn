import curses

# Initialize the screen
stdscr = curses.initscr()

# Turn off echoing of keys, and enter cbreak mode,
# where no buffering is performed on keyboard input
curses.noecho()
curses.cbreak()

# Clear the screen
stdscr.clear()

# Add content to the screen
stdscr.addstr(10, 10, "You can write here: ")

# Get user input
user_input = stdscr.getstr(0, len("You can write here: "))

# Exit curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

# Do something with the user input
print("User input:", user_input)