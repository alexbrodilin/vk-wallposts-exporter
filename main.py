#!/usr/bin/python
# -*- coding: UTF-8 -*-

import vk_auth
import math
import time
import datetime
from app_conf import *
from app_func import *

# authenticate to vk.com
token, user_id = vk_auth.auth(email, password, client_id, scope)

# determin count of requests to VK
reqs = int(math.ceil(p_count / 100.0))

print "[INFO] Count of requests to VK: {}".format(reqs)

# get posts' JSON representation
wall_posts = []
offset = 0
for i in xrange(reqs):
    if by_tags is 1:
        posts = call_api("wall.search", [("domain", domain), \
        ("count", 100), ("offset", offset), ("query", "#" + " #".join(tags_req))], token)
    else:
        posts = call_api("wall.get", [("domain", domain), \
        ("count", p_count), ("offset", offset)], token)
    wall_posts += posts[1:]
    offset += 100

print "[INFO] Posts requested: {}".format(len(wall_posts))

# create output file
output = open(file_name, "w")
output.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<posts>")

# export counter
exp_counter = 0

export_time = time.time()

# all posts tags
all_tags = []

# reverse posts list
if old2new is 1:
    wall_posts = list(reversed(wall_posts))
    print "[INFO] Posts list represented from old to new"

# loop through JSON responce
for (i, post) in enumerate(wall_posts):
    post_text = post["text"].replace("<br>", "\n")
    # apply basic filtering
    if post["post_type"] is "copy" and skip_reps is 1:
        continue
    try:
        if post["attachment"]["poll"]:
            continue
    except:
        pass
    if len(post_text) < min_text_long:
        continue
    # extract post's hashtags
    post_tags = extract_hash_tags(post["text"].encode('utf-8'))
    # collect tags
    all_tags += post_tags
    # extract author's name and check
    try:
        post_auth = call_api("users.get", [("user_ids", post["signer_id"]), ("lang", "ru")], token)
        name = post_auth[0]["first_name"]
        lname = post_auth[0]["last_name"]
    except:
        name = "4bit - Games community"
        lname = ""
    # extract fields and make some good stuff with it
    try:
        post_image = post["attachment"]["photo"]["src_big"]
    except:
        post_image = ""
    # append extracted post's fields to opened file
    dt = datetime.datetime.fromtimestamp(post['date']).strftime('%Y-%m-%d %H:%M')
    output.write('\n\t<post>\n\t\t<id>{}</id>\n\t\t<title></title>\n\t\t<image>{}</image>\n\t\t<text>{}</text>\n\t\t<tags>{}</tags>\n\t\t<author>{} {}</author>\n\t\t<time>{}</time>\n\t</post>'.format(post["id"], post_image, post_text.encode('utf-8'), ", ".join(post_tags), name.encode("utf-8"), lname.encode("utf-8"), dt))
    exp_counter += 1
# finish XML and close file
output.write("\n</posts>")
output.close

print "[INFO] Posts exported to XML: {}".format(exp_counter)

if by_tags is not 1:
    with open(t_file_name, "w") as tags_out:
        tags_out.write("\n".join(get_distinct(all_tags)))
        tags_out.close
    print "[INFO] All unique tags exported to file"
