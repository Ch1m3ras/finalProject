#!/usr/bin/python3

import cgi
import random

def htmlTop():
    print ('''
# Content-type:text/html\n\n
<!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta charset="utf-8" >
        <title>Signup Complete!</title>
    </head>
    <body>
       <p>This work.</p>
    </body>
</html>
              ''')

def main():
    htmlTop()

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()