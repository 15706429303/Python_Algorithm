import textwrap
from email import message_from_string
from nntplib import NNTP
from time import localtime, time, strftime

day = 24 * 60 * 60
def wrap(string,max = 70):
    '''
    :param string:
    :param max:
    :return:
    '''
    return '\n'.join(textwrap.wrap(string,max)) + '\n'

class NewsAgent:
    '''

    '''
    def __init__(self):
        self.sources = []
        self.destinations = []
    def addSource(self,source):
        self.sources.append(source)
    def addDestination(self,dest):
        self.destinations.append(dest)
    def distribute(self):
        items = []
        for source in self.sources:
            items.extend(source.getItems())
        for dest in self.destinations:
            dest.receiveItems(items)

class NewsItem:
    def __init__(self,title,body):
        self.title = title
        self.body = body
class NNTPSource:
    def __init__(self,servername,group,window):
        self.servername = servername
        self.group = group
        self.window = window
    def getItems(self):
        start = localtime(time() - self.window * day)
        date = strftime('%y%m%d',start)
        hour = strftime('%H%M%S',start)
        server = NNTP(self.servername)
        ids = server.newnews(self.group,date,hour)[1]
        for id in ids :
            lines = server.article(id)[3]
            message = message_from_string('\n'.join(lines))
            title = message['subject']
            body = message.get_payload()
            if message.is_multipart():
                body = body[0]
            yield NewsItem(title,body)
        server.quit()