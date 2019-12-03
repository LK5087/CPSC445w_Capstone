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
keywords = form.getvalue("keywords")
print("test")
keywords = keywords.split(',')
source_url = ""

# Build the source/catalog url from user entered data
if website == "reddit.com":
    source_url = "https://reddit.com/r/" + subreddit
if website == "4channel.org":
    source_url = "https://boards.4channel.org/" + board

# Grabbing the source url and storing it for parsing out information
print(source_url)

response = urllib.urlopen(source_url)
site_html = response.read()

# The site html is now contained within site_html variable, ready to begin searching
# Putting all threads into a list
if website == "4channel.org":
    response = urllib.urlopen(source_url)
    site_html = response.read()

    # The site html is now contained within site_html variable, ready to begin searching
    # Putting all threads into a list
    whole_thread_list = ""
    current_position = site_html.find('{"threads":') + len('{"threads":')
    while (current_position != -1):
        # Thread number
        back_position = site_html.find('"', (current_position + 1)) + len('"')
        current_position = site_html.find('"', back_position)
        thread_number = site_html[back_position:current_position]
        # Date
        back_position = site_html.find('"date":', current_position) + len('"date":')
        current_position = site_html.find(",", back_position)
        date = site_html[back_position:current_position]
        # File name
        back_position = site_html.find('"file":"', current_position) + len('"file":"')
        current_position = site_html.find('"', back_position)
        filename = site_html[back_position:current_position]
        # Num Replies
        back_position = site_html.find('"r":', current_position) + len('"r":')
        current_position = site_html.find(',', back_position)
        num_replies = site_html[back_position:current_position]
        # Num Images
        back_position = site_html.find('"i":', current_position) + len('"i":')
        current_position = site_html.find(',', back_position)
        num_images = site_html[back_position:current_position]
        # Sub (thread title)
        back_position = site_html.find('"sub":"', current_position) + len('"sub":"')
        current_position = site_html.find('"', back_position)
        sub = site_html[back_position:current_position]
        # Teaser (description)
        back_position = site_html.find('"teaser":"', current_position) + len('"teaser":"')
        current_position = site_html.find('"}', back_position)
        teaser = site_html[back_position:current_position]

        print ("</p>Thread number:" + thread_number + "</br>date:" + date + "</br>filename:" + filename + "</brnum_replies:" + num_replies + "</br>num_images:" + num_images + "</br>Thread title:" + sub + "</br>teaser:" + teaser + "</br></p>")
    
        whole_thread_list.append("thread number:" + thread_number + ",date:" + date + ",filename:" + filename + ",num_replies:" + num_replies + ",num_images:" + num_images + ",Thread title:" + sub + ",teaser:" + teaser)

        # End retreive after last thread
        if(site_html.find('},"count"', current_position, (current_position + 12)) != -1):
            break

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




  
