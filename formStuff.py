#!/usr/bin/python3

import cgi
import random

def htmlTop():
    print ('''Content-type:text/html\n\n
<!DOCTYPE html>
<html>
    <head>
		<title>Reviews</title>
		<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        <style>
			* {
				margin: 0%;
				padding: 0%;
				font-family: 'Comic Sans MS';
				font-size: 100%;
				color: white;
			}

            .mainpage {
                width: 100%;
			}

			.titleandlogo {
				text-align: center;
				padding: 0px; 
				background-color:  #83aff0	;
			}

			.pageselector {
				background-color: #4779c4;
			}

			.pageselectorbutton {
				padding: .1%;
				background-color:  #4779c4;
				border-color: #4779c4;
			}

			.pageselectorbutton:hover{
				background-color: #1b2d48;
			}

			.reviews {
				background-color:  #3c649f;
			}

			.footer {
				background-color: #1b2d48;
				color: white;
			}

			table {
				width: 100%;
			}

            h1 {
				font-size: 300%;
				text-decoration: underline;
			}

            a {
				color: white;
				text-decoration: none;
			}
			
        </style>
    </head>

    <body>
        <div class = "mainpage">
			<div class = "titleandlogo">
				<h1>Site Making Co.</h1>
				<p>"We make sure your websites are the best they can be."</p>
				<img src = "logo.png" alt = "Company Logo Image Made in MS Paint that features a geometric design of a square background, then another square roatated 45 degrees and then a star on the top of it.; 13.6 KB" width = 7.5% height = 7.5%>
			</div>
		
			<div class = "pageselector">
				<table>
					<tr>
						<td>
							<a href="http://homer.stuy.edu/~achen62/websiteproject/mainsite.html"><button class = "pageselectorbutton">Homepage</button></a>
                			<a href="http://homer.stuy.edu/~achen62/websiteproject/page3.html"><button class = "pageselectorbutton">Our Mission</button></a>
							<a href="http://homer.stuy.edu/~achen62/websiteproject/page1.html"><button class = "pageselectorbutton">Prices</button></a>
							<a href="http://homer.stuy.edu/~achen62/websiteproject/page2.html"><button class = "pageselectorbutton">Rave Reviews</button></a>
						</td>
						<td style = "text-align: right;">
							<a href="http://homer.stuy.edu/~achen62/websiteproject/buypage.html"><button class = "pageselectorbutton"><img src="cart.png" alt = "Image of a shopping cart evoking the style of other websites" width = 10% height = 10%> Purchase NOW!:</button></a>
						</td>
					</tr>
				</table>
			</div>

			<div class = "reviews">
				<h2 style = "text-align: center;">THANK YOU FOR YOUR REVIEW! Your feedback is greatly appreciated</h2>
				<p><a href = "http://homer.stuy.edu/~achen62/websiteproject/page2.html">Return to Reviews</a></p>
			</div>
              ''')
    
def storingStuff():
    results = cgi.FieldStorage()
    user = results.getvalue("user")
    rating = results.getvalue("rating")
    optionalComments = results.getvalue("optionalComments")
    storageString = "\n" + user + "," + rating + "," + optionalComments
    storageFile = open("fileToStoreReviews.txt", "a")
    storageFile.write(storageString)

def htmlBottom():
    print('''
<div class="footer">
				<table style="width: 100%; border-color: transparent;">
					<tr>
						<td style="text-align: left; border-style: none;"><a href= mailto:"achen62@stuy.edu">Reach out to us at: achen62@stuy.edu</a></td>
						<td style="text-align: right; border-style: none;">Call us at (212) 312-4800</td>
					</tr>
					<tr>
						<td style="text-align: left; border-style: none;">Send mail to us: 345 Chambers St, New York, NY 10282</td>
						<td style="text-align: right; border-style: none;">Fax us(if you still do that): 212-587-3874</td>
					</tr>
					<tr>
						<td style="text-align: left; border-style: none;">Stuyvesant Computer Science Department</td>
						<td style="text-align: right; border-style: none;">This website is pure satire, all quotes are libel and slander. This is simply for fun and not meant to offend. </td>
					</tr>
					<tr>
						<td colspan="2" style="text-align: center; border-style: none; text-decoration: underline;"><a href="http://homer.stuy.edu/~achen62/websiteproject/mainsite.html">Back to the homepage</a></td>
					</tr>
				</table>
		
				<br>
				
				<table style="width: 100%; border-color: transparent;">
					<tr>
						<td style="text-align: center; border-style: none;">Created and &copy; Febuary 16th, 2024 by Alexander Chen(Period 9) Cocreated by Maif Biswas(Also Pd 9)</td>
					</tr>
					<tr>
						<td style="text-align: center; border-style: none; font-size: 85%;" >Legal Disclaimers: All images and videos are &copy; and &#174; by their original copyright holders. We do not claim ownership of any of the content shown in the site. This site is not for commercial use and is within definition of <a href="https://www.copyright.gov/fair-use/" style="text-decoration: underline;">Fair Use in Section 107</a> of the Copyright Act.</td>
					</tr>
				</table>
			</div>

        </div>
    </body>
</html>
          ''')

def main():
    htmlTop()
    print(''.format(storingStuff()))
    htmlBottom()

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
