#!/usr/bin/python3

import cgi
import random

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>My first server-side script. </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')
    
def getData():
    formData = cgi.FieldStorage()
    firstname = formData.getvalue("first_name")
    return firstname
        
 

def main():
    htmlTop()
    print('Hello {}'.format(getData()))
    print('Random number {}'.format(random.randint(1,100)))
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()

