#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
import time
import webbrowser

def timer(s, hrs, mins, secs):
    # Convert time into seconds
    _n = secs + mins*60 + hrs*60*60
    
    print("\nTimer Started...")
    print("> Countdown for: %i hours:%i minutes:%i seconds" %(hrs, mins, secs))
    # This is where real timer works
    # -0.01 is assumed time for execution of above instructions
    time.sleep(_n - 0.01)
    print("Time's up!")
    print("...\...Playing Sound.../...")
    
    # Play sound after timer count completion
    webbrowser.open(s)
    
while True:
    if raw_input("\nContinue[Y/n]? ").strip().lower() == "y": 
        timer(raw_input("\nSound(Link)?: ").strip(), int(raw_input("Hours?: ").strip()), int(raw_input("Minutes?: ").strip()), int(raw_input("Seconds?: ").strip()))
    else:
        print("\nHope You Enjoyed!")
        sys.exit(0)
