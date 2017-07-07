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

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0',
}


def get_country(url):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        print(response.text)
        pattern1 = '\"country-link\"\>(.*?)\<\/a\>'
        countries = re.findall(pattern1, response.text)

        pattern2 = 'href=\"\/zh-cn\/country\/(.*?)\"'
        country_hrefs = re.findall(pattern2, response.text)

        print(len(countries))
        print(len(country_hrefs))

        for i in range(len(countries)):
            coutry = countries[i]
            href = country_hrefs[i]
            href = 'https://www.agoda.com/zh-cn/country/' + href
            print(coutry+'\t' + href)
            with open('country_href','a') as f:
                f.write(coutry+'\t' + href + '\n')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = 'https://www.agoda.com/zh-cn/world.html?ckuid=0e3bde13-1c6b-49d6-a5a8-f51e12b5b01b'
    get_country(url)