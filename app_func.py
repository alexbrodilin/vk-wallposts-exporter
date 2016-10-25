# -*- coding: utf-8 -*-
import json
import urllib2
from urllib import urlencode

def call_api(method, params, token):
    params.append(("access_token", token))
    url = "https://api.vk.com/method/%s?%s" % (method, urlencode(params))
    return json.loads(urllib2.urlopen(url).read())["response"]

def extract_hash_tags(s):
    return set(part[1:].split("<br>")[0] for part in s.split() if part.startswith('#'))



def get_distinct(original_list):
    distinct_list = []
    for each in original_list:
        if each.lower() not in distinct_list:
            distinct_list.append(each.lower())
    return sorted(distinct_list)



