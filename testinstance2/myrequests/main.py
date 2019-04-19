# -*- coding:UTF-8 -*-
import requests


codeurl = 'https://blog.csdn.net/wangjvv/article/details/78235808'

valcode = requests.get(codeurl)

# f = open(r'd://csdn.html','wb')
# f.write(valcode.content)
# re_text = valcode.text
# re_content = valcode.content
# print re_text
# print type(re_text)
# print re_content
# print type(re_content)
# valcode.encoding = 'utf-8'
# re_text = valcode.text
# print re_text


# print valcode.json()
# print valcode.raw
# print valcode.raw.read(10)
print valcode.status_code is requests.codes.ok
valcode.raise_for_status()

print valcode.headers['Server']
print valcode.headers.get('Server')

