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
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0',
}


def get_country(url, country):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        # print(response.text)

        #拿到GeoApi
        pattern = '\/api\/zh-cn\/GeoApi/AllStates(.*?)\''
        GeoAPI = re.findall(pattern, response.text)

        if len(GeoAPI) == 1:
            GeoAPI = 'https://www.agoda.com/api/zh-cn/GeoApi/AllStates' + GeoAPI[0]
        print(GeoAPI)

        with open('country_GeoAPI', 'a')as f2:
            f2.write(country + '\t' + GeoAPI + '\n')

    except Exception as e:
        print(e)


if __name__ == '__main__':


    with open('country_href') as f:
        tmp = f.readline()[:-1]
        country = tmp.split('\t')[0]
        href = tmp.split('\t')[1]
        while tmp:
            try:
                get_country(href, country)
                time.sleep(0.5)
            except Exception as e:
                print(e)

            tmp = f.readline()[:-1]
            country = tmp.split('\t')[0]
            href = tmp.split('\t')[1]



#直接请求API
# https://www.agoda.com/api/zh-cn/GeoApi/AllStates/4/191/0
#https://www.agoda.com/api/zh-cn/GeoApi/AllStates/4/140/0
