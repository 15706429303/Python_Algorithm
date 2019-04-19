# -*- coding:UTF-8 -*-
import re

import requests
from BeautifulSoup import BeautifulSoup

codeurl = 'https://blog.csdn.net/wangjvv/article/details/78235808'



def get_bat_count(url):
    r = requests.get(codeurl)
    text = r.text.replace('<!DOCTYPE html>\n','')
    soup = BeautifulSoup(text)
    # print soup.contents[0]
    headTag = soup.head
    bodyTag = soup.body
    # print headTag.parent.name
    # print headTag.parents
    # print headTag.nextSibling
    # print headTag.previousSibling

    # only back one value
    # print soup.find('head')
    # print soup.find(['head', 'body'])
    # print soup.find({'head': True, 'body': True})
    # print soup.find(re.compile('^p'))
    # soup.find(id='xxx')
    # 寻找id属性为xxx的
    # soup.find(attrs={id=re.compile('xxx'), algin='xxx'})
    # 寻找id属性符合正则且algin属性为xxx的
    # soup.find(attrs={id=True, algin=None})
    # 寻找有id属性但是没有algin属性的

    aa = soup.findAll('a')
    res = re.compile('http')
    cc = [abc(a) for a in aa if abc(a) is not None and
          res.match(abc(a)) is not None]
    cc = list(set(cc))
    cc.sort()
    for c in cc:
        print c


def abc(a):
    return dict(a.attrs).get('href')


get_bat_count(codeurl)