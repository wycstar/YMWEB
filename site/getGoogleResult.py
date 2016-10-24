#!/usr/bin/python python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from langconv import *
import globals


def getRawContent(keyword, pn):
    u = {'Connection': 'Keep-Alive',
         'Accept': 'text/html, application/xhtml+xml, */*',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'Accept-Encoding': 'gzip,deflate,sdch',
         'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    params = {'q': keyword,
              "start": (pn - 1) * 10,
              'gws_rd': "ssl"}
    html = requests.get('https://www.google.com.hk/search',
                        params=params,
                        timeout=5,
                        headers=u).content.decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, "html.parser")
    findResultSumRe = re.compile(r'<div\s*id="resultStats">\D*([\d,]*).*<nobr>')
    findResultTimeRe = re.compile(r'<nobr>\D*([\d.]*)\D*</nobr>')
    resultInfo = soup.find_all("div", id="resultStats")
    globals.resultSum = findResultSumRe.findall(str(resultInfo))
    globals.resultTime = findResultTimeRe.findall(str(resultInfo))
    return soup.find_all("div", class_="rc")


def getResultList(soup):
    findAbstractRe = re.compile(r'<span\s+class="st">(.+?)</span></?div')
    findCiteRe = re.compile(r'<cite\s+class="_Rm.*">(.+?)</cite>')
    return [{'title': Converter('zh-hans').convert(b.h3.get_text()),
             'link': b.h3.a.get('href'),
             'cite': Converter('zh-hans').convert(findCiteRe.findall(str(b))[0]),
             'abstract': Converter('zh-hans').convert(findAbstractRe.findall(str(b))[0])} for b in soup if findAbstractRe.findall(str(b))]


if __name__ == "__main__":
    rawContent = getRawContent('宇宙', 1)
    result = getResultList(rawContent)
    for x in result:
        print(x['abstract'])
