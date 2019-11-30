#!/usr/bin/python

print("Content-type: text/html\n\n")

# Importing urllib to fetch html from urls, os to perform file I/O, and cgi to interact with httpd web server
# Python2, so urllib is one import and not split
import urllib, os, cgi

# Liam Kempton
# =====================================================
# This is the python web crawler. It accepts user input,
# and retrieves and stores content locally for later use.
# It uses http post on the Apache httpd web server. 
# ===================================================== 

# Creating fieldStorage, which stores the values from the post message
form = cgi.FieldStorage()

print(form)

# Get data from the fields sent over in post from new search form
if form.getvalue("website"):
    website = form.getvalue("website")
else:
    website = "Not set"

if website == "reddit.com":
    subreddit = form.getvalue("subreddit")
    upvote_gr_ls = form.getvalue("upvote_gr_ls")
    upvote_count = form.getvalue("upvote_count")
    board = "FILLER"
    reply_gr_ls = "FILLER"
    reply_count = "FILLER"

if website == "4channel.org":
    board = form.getvalue("board")
    reply_gr_ls = form.getvalue("reply_gr_ls")
    reply_count = form.getvalue("reply_count")
    subreddit = "FILLER"
    upvote_gr_ls = "FILLER"
    upvote_count = "FILLER"

# Simple form elements, not dependant on website and don't need parsing
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")
frequency = form.getvalue("frequency")
start_time = form.getvalue("start_time")
search_name = form.getvalue("search_name")
search_description = form.getvalue("search_description")

# Keyword (properly separated by commas) can be split in one line to make an array
keywords = form.getvalue("keywords").split(',')

# Build the source/catalog url from user entered data
if website == "reddit.com":
    source_url = "https://reddit.com/r/" + subreddit
if website == "4channel.org":
    source_url = "https://boards.4channel.org/" + board

# Grabbing the source url and storing it for parsing out information
response = urllib.request.urlopen(source_url)
webContent = response.read()
print (webContent[0:100])

print ("<html>")
print ("<head>")
print ("<title>Search Confirmation</title>")
print ("</head>")
print ("<body>")
print ("website: " + website)
print ("</br>board: " + board)
print ("</br>subreddit: " + subreddit)
print ("</br>reply_gr_ls: " + reply_gr_ls)
print ("</br>upvote_gr_ls: " + upvote_gr_ls)
print ("</br>start_date: " + start_date)
print ("</br>start_time: " + start_time)
print ("</br>frequency: " + frequency)
print ("</br>end_date: " + end_date)
print ("</br>search_name: " + search_name)
print ("</br>search_description: " + search_description)
print ("</br>keywords: ")
for item in keywords:
    print(item + ",")
print ("</body>")
print ("</html>")




  
