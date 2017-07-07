#!usr/bin/env python3.6  
#-*- coding:utf-8 -*-  
""" 
@author:iBoy 
@file: get_country.py
@time: 2017/07/07
"""
import re

import requests
from lxml import etree
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0',
}


def get_country(url, country):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'

        print(response.text)

        province_list = response.text
        province_list = json.loads(province_list)

        for each in province_list:
            name = each['name']
            url = 'https://www.agoda.com' + each['url']

            print(country + '\t'+name + '\t' + url)

            with open('country_province_url', 'a') as f2:
                f2.write(country + '\t' +name + '\t' + url + '\n')


    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = 'https://www.agoda.com/api/zh-cn/GeoApi/AllStates/4/191/0'


    with open('country_GeoAPI') as f:
        tmp = f.readline()[:-1]
        country = tmp.split('\t')[0]
        url = tmp.split('\t')[1]
        while url:
            try:
                get_country(url, country)
            except Exception as e:
                print(e)
            tmp = f.readline()[:-1]
            country = tmp.split('\t')[0]
            url = tmp.split('\t')[1]

