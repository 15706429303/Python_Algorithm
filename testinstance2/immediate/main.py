# -*- coding:UTF-8 -*-
import re

l1 = '\*(.+?)\*-(.+?)-'
l2 = '(http://[\.a-z0-9A-Z/]+)'
l3 = '([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)'
mat = re.search(l1,'1111*3333*-2222-')

print mat.group()