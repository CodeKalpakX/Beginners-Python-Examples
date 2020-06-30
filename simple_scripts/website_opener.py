#!/usr/bin/python
# -*- coding: utf-8 -*-

# Just Exploring webbrowser lib
from webbrowser import open as web_open

# Simple function to open given link in webbrowser
def open_website(link):
    try:
        print("Opening link: " + link)
        web_open(link)
    except Exception as e:
        print("Error Occurred:\n {}".format(e))
    
    
# Just for test
get_link = raw_input("Link to open: ")
open_website(get_link)
