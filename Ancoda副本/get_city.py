#!usr/bin/env python3.6
#-*- coding:utf-8 -*-  
""" 
@author:iBoy 
@file: get_country.py
@time: 2017/07/07
"""
import json
import re

import requests
from lxml import etree
import time
from mongodb_queue import MongoQueue
import multiprocessing

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0',
}
spider_queue = MongoQueue('yueyu', 'province_urls')

def get_info():
    while True:
        try:
            url = spider_queue.pop()
            country = spider_queue.pop_country(url)
            province = spider_queue.pop_province(url)
            print(url)
        except KeyError:
            print('No data...')
            break
        else:
            status_code = get_country(url, country, province)
            if status_code == 200:
                spider_queue.complete(url)
            else:
                spider_queue.reset(url)

def get_country(url, country, province):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        # print(response.text)

        #get GeoApi/NeighborHoods
        pattern = '\/api\/zh-cn\/GeoApi\/NeighborHoods(.*?)\''
        GeoAPI = re.findall(pattern, response.text)
        if len(GeoAPI) == 1:
            GeoAPI = 'https://www.agoda.com/api/zh-cn/GeoApi/NeighborHoods' + GeoAPI[0]
        print(GeoAPI)

        print('Request province_API to get city_url....')

        get_city_API(GeoAPI, country, province)

    except Exception as e:
        print(e)
    return response.status_code



def get_city_API(url, country, province):
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

            with open('country_province_city_url', 'a') as f2:
                f2.write(country + '\t' + province + '\t' + name + '\t' + url + '\n')


    except Exception as e:
        print(e)

def process_cralwer():
    process = []
    for i in range(2):
        p = multiprocessing.Process(target=get_info)
        p.start()
        process.append(p)
    for p in process:
        p.join()

if __name__ == '__main__':
    process_cralwer()

    # url = 'https://www.agoda.com/zh-cn/region/guangdong-province-cn.html'
    # get_country(url, 'counrty1', 'province1')


