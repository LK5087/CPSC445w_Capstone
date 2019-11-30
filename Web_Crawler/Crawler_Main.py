import urllib.request, urllib.error, urllib.parse, os, cgi

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

if website == "4channel.org":
    board = form.getvalue("board")
    reply_gr_ls = form.getvalue("reply_gr_ls")
    reply_count = form.getvalue("reply_count")

# Simple form elements, not dependant on website and don't need parsing
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")
frequency = form.getvalue("frequency")
search_name = form.getvalue("search_name")
search_description = form.getvalue("search_description")

# Keyword (properly separated by commas) can be split in one line to make an array
keywords = form.getvalue("keywords").split(',')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>test_successful_posting</title>"
print "</head>"
print "<body>"
print "<h2> Selected website is %s</h2>" % website
print "</body>"
print "</html>"




  
