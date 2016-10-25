# vk-wallposts-exporter
Wall posts exporter for filtering and exporting contents of VK.com walls to XML file

WARNING! For correct running vk_auth.py module requiered. Please, download it at https://github.com/dzhioev/vk_api_auth

To create your VK APP ID read documentations here https://vk.com/dev/standalone

Application config parameters description
=========================================
# VK application parameters
- client_id = "<your_app_id>" # your VK APP ID
- scope = "wall" # page scope
- domain = "<your_group_id>" # your group ID or domain. For example, my_public

# authentication parameters
- email = "<your_login_email>" # your VK login e-mail
- password = "<your_login_password>" # your VK login password

# export parameters
- p_count = 1500  # how much posts needed to check for export
- by_tags = 1  # if set as 1, use tags_req as tags for search (AND logic)
- old2new = 1  # if seat as 1, returned list of posts will be reversed
- file_name = "<path_to_output_xml_file>" # path to output xml file
- t_file_name = "<path_to_output_txt_file_for_unique_tags>" # path to output txt file for unique tags


# basic filtering parameters
- skip_reps = 1  # skip reposts
- skip_polls = 1  # skip posts with polls inside
- min_text_long = 1000  # minimal post text long

# tags for filtering
- tags_req = [] # array of hashtags for filtering. For example ['hastag1', 'hashtag2']
