import sys

CONFIG = {}

def parse_args():
    for arg in sys.argv:
      if arg == "-f":
          CONFIG["FAST"] = True
      elif arg == "-t":
          CONFIG["VERBOSE"] = True
        
      
    
