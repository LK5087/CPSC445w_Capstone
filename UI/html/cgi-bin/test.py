import urllib

response = urllib.urlopen("https://boards.4channel.org/g/catalog")
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
    current_position = site_html.find('"},', back_position)
    teaser = site_html[back_position:current_position]
    # End retreive after last thread

    print ("Thread number:" + thread_number + "\ndate:" + date + "\nfilename:" + filename + "\nnum_replies:" + num_replies + "\nnum_images:" + num_images + "\nThread title:" + sub + "\nteaser:" + teaser + "\n")
    