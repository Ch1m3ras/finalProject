#!/usr/bin/python

import cgi
print("THIS PAGE FUNCIONS")

def Main():
    print("TRY DIS")

    
if __name__ == '__main__':
    try:
        Main()
    except:
        cgi.print_exception()