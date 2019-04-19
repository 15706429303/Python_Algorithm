import re
from HTMLParser import HTMLParser

import requests


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        '''
        :param tag: is tag such as <a></a> <p></p>
        :param attrs: in tag parameter  such as href class
        :return:
        '''
        if tag == 'a':
            if len(attrs) == 0:
                pass
            else:
                for variable, value in attrs:
                    if variable == 'href':
                        self.links.append(value)

if __name__ == "__main__":
    codeurl = 'https://blog.csdn.net/wangjvv/article/details/78235808'
    r = requests.get(codeurl)
    hp = MyHTMLParser()
    hp.feed(r.text)
    hp.close()
    https = list(set(hp.links))
    https.sort()
    for hh in https:
        if re.search('^http',hh) == None:
            https.remove(hh)
            continue
        print hh