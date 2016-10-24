#!/usr/bin/python python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import html


def getZhiHuRawContent(keyword):
    u = {'Connection': 'Keep-Alive',
         'Accept': 'text/html, application/xhtml+xml, */*',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'Accept-Encoding': 'gzip,deflate,sdch',
         'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    params = {'query': keyword,
              "ie": 'utf8'}
    html = requests.get('http://zhihu.sogou.com/zhihu',
                        params=params,
                        timeout=5,
                        headers=u).content.decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all('div', class_='result-about-list')


def getZhiHuResultList(keyword):
    result = getZhiHuRawContent(keyword)
    findTitleRe = re.compile(r'>(.+?)</a>')
    findThumbRe = re.compile(r'src="(.+?)"\s+style=')
    return [{'title': findTitleRe.findall(str(x.h4))[0],
             'link': x.h4.a.get('href'),
             'thumb': 'https://img02.sogoucdn.com/v2/thumb/resize/w/100/h/100/ir/3/zi/on/iw/75/ih/75/crop/x/0/y/0/w/100/h/100?t=2&appid=200648&url=http%3A%2F%2Fpic1.zhimg.com%2Fe82bab09c_l.jpg&referer=http://www.zhihu.com/topic/19836490'
                      if len(x.find_all('span', class_='about-img')) == 0
                      else html.unescape(findThumbRe.findall(str(x.find_all('span', class_='about-img')))[0]).replace('http','https'),
             'author': '知乎用户' if x.p.a is None else x.p.a.text,
             'like': x.find_all('span', class_='count')[0].text} for x in result if x.p is not None][:6 if len(result) > 6 else len(result)]

if __name__ == '__main__':
    result = getZhiHuResultList('我们')
    for b in result:
        print(b['title'])
        print(b['link'])
        print(b['thumb'])
        print(b['author'])
        print(b['like'])
