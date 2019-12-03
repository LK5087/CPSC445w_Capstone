#!/usr/bin/python

print("Content-type: text/html\n\n")

# Importing urllib to fetch html from urls, os to perform file I/O, and cgi to interact with httpd web server
# Python2, so urllib is one import and not split
import urllib, os, cgi, time

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
print("Keywords: " + keywords)
keyword_list = keywords.split(',')
keyword_list = [x.strip(' ') for x in keyword_list]
print(keyword_list)

source_url = ['test']

# Build the source/catalog url from user entered data
if website == "reddit.com":
    source_url = "https://reddit.com/r/" + subreddit
if website == "4channel.org":
    source_url = "https://boards.4channel.org/" + board + "catalog"
# The site html is now contained within site_html variable, ready to begin searching
# Putting all threads into a list
response = urllib.urlopen(source_url)
site_html = response.read() 
print("</br>Source URL: " + source_url)
# Creating a folder for this specific search
search_folder_name = (search_name + '-' + time.asctime(time.localtime(time.time()))).replace(" ", "")
print("</br>Search folder name: " + search_folder_name)
search_folder_path = r'/var/www/html/stitch_content/' + search_folder_name 
# OS.MAKEDIRS having serious issues, must fix!!!!   
if not os.path.exists(search_folder_path):
    os.makedirs(search_folder_path)
print("path was created")
# Creating a search index page in the above folder
search_index_name = search_folder_name + "-index.html"
print("</br>Search index name: " + search_index_name)
search_index_path = search_folder_path +  "/" + search_index_name
print("</br>Search index Path: " + search_index_path)
search_index = open(search_index_path,"w+")
search_index.write("<html><head><title>" + search_folder_name + "</title></head><body><h3>" + search_folder_name + "</h3></br>Search Name: " + search_name + "</br>Search Decription: " + search_description + "</br>Board: " + board + "</br>Search Keywords: " + keywords + "</br></br>")
# Create link to search index in main page index
main_index = open("/var/www/html/stitch_content/main_page.html","a+")
index_file_path = ("http://ec2-54-224-12-132.compute-1.amazonaws.com/stitch_content/" + search_folder_name + "/" + search_index_name)
print(search_folder_name)
print(search_index_name) 
print(index_file_path)
main_index.write('<a href="' + index_file_path + '">' + search_folder_name + '</a></br>')

    # The site html is now contained within site_html variable, ready to begin searching
    # Putting all threads into a list

# DO NOT MODIFY ABOVE THIS LINE

if(website == "reddit.com"):
        current_position = site_html.find('html')
        loop_num = site_html.count('href="https://www.reddit.com/r/ImaginaryWastelands/comments')
        print(loop_num)
        x = 0
        while (x < loop_num):
                #Post id number
                #back_position = site_html.find('3_', current_position) + len('3_')
                #current_position = site_html.find('"', back_position)
                #post_id = site_html[back_position:current_position]
                #print("</br>post id :" + post_id)
                # Post upvote count
                #back_position = site_html.find('1a1a1b">', current_position) + len('1a1a1b">')
                #print(back_position)
                #current_position = site_html.find('<', back_position)
                #print(current_position)
                #upvote_count = site_html[back_position:current_position]
                #print("</br>upvote count: " + upvote_count)
                # Post href link
                back_position = site_html.find('href="https://www.reddit.com/r/ImaginaryWastelands/comments', (current_position+1)) + 6
                current_position = site_html.find('"', back_position)
                thread_url = site_html[back_position:current_position]
                thread_url = thread_url[:-1]
                print("</br></br>thread_url: " + thread_url)
                response = urllib.urlopen(thread_url)
                thread_html = response.read()
                x = x+1
# DO NOT MODIFY BELOW THIS LINE

if(website == "4channel.org"):
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

        print ("</p>Thread number:" + thread_number + "</br>date:" + date + "</br>filename:" + filename + "</br>num_replies:" + num_replies + "</br>num_images:" + num_images + "</br>Thread title:" + sub + "</br>teaser:" + teaser + "</br></p>")
       
        # Searching thread data for user keywords
        for i in keyword_list:
                if(sub.find(i) != -1)  or (teaser.find(i) != -1):
                        thread_url = ("https://boards.4channel.org/" + board + "thread/" + thread_number)
                        print(thread_url)
                        response = urllib.urlopen(thread_url)
                        print('test')
                        thread_html = response.read()
                        print('test1')
                        thread_path = (search_folder_path + "/" + thread_number + ".html")
                        thread_path_pt_2 = (search_folder_name + "/" + thread_number + ".html")
                        print('test2')
                        print(thread_path_pt_2)
                        thread_file = open(thread_path,"w+")
                        print("test3")
                        thread_file.write(thread_html)
                        print('test')
                        search_index.write("<a href=http://ec2-54-224-12-132.compute-1.amazonaws.com/stitch_content/" + thread_path_pt_2 + ">" + board + sub + "</a></br>") 

        # list_entry = "thread number:" + thread_number + ",date:" + date + ",filename:" + filename + ",num_replies:" + num_replies + ",num_images:" + num_images + ",title:" + sub + ",teaser: " + teaser
        if(site_html.find('},"count"', current_position, (current_position + 12)) != -1):
            break

#if(website == "reddit.com"):
        #print("</br>test1")
        #current_position = site_html.find('<div id="t') + len('<div id="t')
        #print('test2')
        #while(current_position != -1):
                # Post number
                #back_position = site_html.find('<div id="_', (current_position + 1)) + len('_')
                #current_position = site_html.find('"', back_position)
                #post_number = site_html[back_position:current_position]
                # Post title
                #back_position = site_html.find('<h3 class="', current_position) + len('<h3 class"')
                #back_position = site_html.find('>', back_position) + length('>')
                #current_position = site_html.find('</h3>', back_position)
                #post_title = site_html[back_position:current_position]
                # Upvote number
                #back_position = site_html.find('</i><span class="F', current_position) + len('</i><span class="F')
                #current_position = site_html.find(' ', back_position)
                #upvote_number = site_html[back_position:current_position]
                
                #print("</br>post_number: " + post_number + "</br>post_title: " + post_title + "</br>upvote_number: " + upvote_number)

print ("<html>")
print ("<head>")
print ("<title>Search Confirmation</title>")
print ("</head>")
print ("<body>")
print ("<h3>Search Successsful</h3>")
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
    print(item + ",")
print ("</body>")
print ("</html>")
