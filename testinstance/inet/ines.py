# -*- coding:UTF-8 -*-
import re
import urllib

oriurl = 'https://blog.csdn.net/yuxiaosmd/article/details/80160899'
urlalready = []
entercount = 0

urlmatch = r'<a(.*)(href.*)a>'
urlmatch2 = '(https:|http:)(.*?)["\'].*?">(.*?)</'

def printfUrl(title,session,url,type):
    strip = "-"
    for index in range(0,type):
        strip.join(strip)
    print strip + title.strip() + "--" + session + url


def getUrlData(url):
    response = urllib.urlopen(url)
    return response.read()


def findallurl(url):
    if entercount is 2:
        return
    ++entercount
    pagestr = getUrlData(url);
    urls = re.findall(urlmatch2, pagestr)
    for item in urls:
        if item[2] is '':
            continue
        if item[1].find('blog.csdn.net') is -1:
            continue
        if 'UpdateTime' in item[1] or 'ViewCount' in item[1] or 't=1' in item[1]:
            continue
        # if item[1].find('UpdateTime','ViewCount') is not -1:
        #     continue
        if item[0]+item[1] in urlalready:
            continue
        urlalready.append(item[0]+item[1])
        printfUrl(item[2],item[0],item[1],0)
        findallurl(item[0]+item[1])

findallurl(oriurl);