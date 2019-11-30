#!/usr/bin/env python

print("Content-type: text/html\n\n")

import os, cgi, hashlib

# =======================================================
# This file creates a new user account, adds to user list
# User list located at /home/ec2-user/stitch/users.txt
# =======================================================

# Creating fieldStorage, which stores the values from the post message
form = cgi.FieldStorage()

username = form.getvalue("username_field")
password = hashlib.md5(form.getvalue("password_field"))
password_confirm = hashlib.md5(form.getvalue("password_field_confirm"))
if (password != password_confirm):
    # something to return and tell user passwords do not match
email = form.getvalue("email_field")

# Write new user data into the user file, if none exists then create one
try:
    f = open("/home/ec2-user/stitch/users.txt")
    f.write(",{" + username + "," + password + "}")
except IOError:
    f = open("user_file.txt","w+")
    f.write(",{" + username + "," + password + "}")
finally:
    f.close()

print ("Location: index.html")
    
