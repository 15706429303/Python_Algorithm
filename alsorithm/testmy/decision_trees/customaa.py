import httplib,json

c = httplib.HTTPConnection('localhost', 8080)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
c.request('GET', '/jobs/123/321', '{}', headers)
s = c.getresponse().read().strip()

print json.loads(s)