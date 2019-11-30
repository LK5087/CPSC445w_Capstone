#!/usr/bin/python

print("Content-type: text/html\n\n")

import os, cgi, hashlib

# Creating fieldStorage, which stores the values from the post message
form = cgi.FieldStorage()

username = form.getvalue("username_field")
username_length = len(username)
password = hashlib.md5(form.getvalue("password_field"))
password_length = len(password)
total_length = username_length + password_length

# Find username and password in text document to compare entered data into
try:
    f = open("/home/ec2-user/stitch/users.txt")
    username_start = f.find(username)
    username_end = username + total_length
    print(username + "," + password)
    print(f[username_start:username_end])
    if((username + "," + password) == (f[username_start:username_end])):
        print ("Location: homepage.html")
except IOError:
    # In case of invalid login, refresh the page (clear fields)
    print ("Location: index.html")
finally:
    f.close()