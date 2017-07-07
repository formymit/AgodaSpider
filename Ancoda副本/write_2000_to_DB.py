#!usr/bin/env python3.6  
#-*- coding:utf-8 -*-  
""" 
@author:iBoy 
@file: write_2000_to_DB.py 
@time: 2017/07/07 
"""
from mongodb_queue import MongoQueue

spider_queue = MongoQueue('yueyu', 'province_urls')

with open('country_province_url') as f:
    tmp = f.readline()[:-1]
    country = tmp.split('\t')[0]
    province = tmp.split('\t')[1]
    url = tmp.split('\t')[2]

    while tmp:
            spider_queue.agoda_push(url, country, province)
            tmp = f.readline()[:-1]
            country = tmp.split('\t')[0]
            province = tmp.split('\t')[1]
            url = tmp.split('\t')[2]



