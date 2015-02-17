#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An example of using the Socrata API in Python.
"""
from __future__ import print_function

import urllib, urllib2
import json

def get_trees(args):
    """Get trees using passed arguments."""
    
    api = "https://data.oaklandnet.com/resource/4jcx-enxf.json?"
    try:
        url = api + urllib.urlencode(args)
        data = urllib2.urlopen(url)
        response_data = json.load(data)
        data.close()
    except urllib2.HTTPError, e:
        print("HTTP error: {}".format(e.code))
    except urllib2.URLError, e:
        print("Network error: {}".format(e.reason.args[1]))

    return response_data

if __name__ == '__main__':
    # make request for first five trees and order by id
    args = {"$order": ":id", "$limit": 5, "$offset": 0}
    five_trees = get_trees(args)
    
    # print out the raw data
    for n, tree in enumerate(five_trees):
        print("-- Tree {}:\n{}".format(n+1, tree), end='\n\n')
    
    for n, tree in enumerate(five_trees):
        # accessing the fields is fairy complicated
        st_num = eval(tree[u'location_1'][u'human_address'])['address']
        st_name =eval(tree[u'stname'][u'human_address'])['address'] 
        spec = tree[u'species']
        print("-- Tree {}: {}".format(n+1, spec))
        print("address: {} {}".format(st_num, st_name), end='\n\n')
 
#    # get all tree data
#    args2 = {"$limit": 40000, "$offset": 0, "$order": ":id"}
#    all_data = get_trees(args2)
#    print("number of trees: {}".format(len(all_data)))
