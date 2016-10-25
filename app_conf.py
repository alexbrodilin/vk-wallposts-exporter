# -*- coding: utf-8 -*-

# VK application parameters
client_id = "<your_app_id>"
scope = "wall"
domain = "<your_group_id>"

# authentication parameters
email = "<your_login_email>"
password = "<your_login_password>"

# export parameters
p_count = 1500  # how much posts needed to check for export
by_tags = 1  # if set as 1, use tags_req as tags for search (AND logic)
old2new = 1  # if seat as 1, returned list of posts will be reversed
file_name = "<path_to_output_xml_file>"
t_file_name = "<path_to_output_txt_file_for_unique_tags>"


# basic filtering parameters
skip_reps = 1  # skip reposts
skip_polls = 1  # skip posts with polls inside
min_text_long = 1000  # minimal post text long

# tags for filtering
tags_req = []
