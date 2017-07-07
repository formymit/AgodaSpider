#!usr/bin/env python3.6  
#-*- coding:utf-8 -*-  
""" 
@author:iBoy 
@file: test_city_API.py 
@time: 2017/07/07 
"""

import requests
import json

url = 'https://www.agoda.com/api/zh-cn/GeoApi/NeighborHoods/8/3133/0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0',
}

response = requests.get(url, headers=headers)

print(response.text)
