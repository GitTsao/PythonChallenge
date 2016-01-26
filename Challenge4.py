# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:50:30 2015

@author: GeneralTsao
"""

import urllib
import re

site = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
first = '94191'
num = 400
a = urllib.request.urlopen(site + first)
txt = ""
for i in range(400):
    txt = a.read().decode("utf-8")
    print(txt)
    if(not re.match("Yes. Divide", txt)):
        num = re.findall('next nothing is [0-9]+', txt)
        num = re.findall('[0-9]+', num[0])
        a = urllib.request.urlopen(site + num[0])
    else:
        num = int(num[0], 0)//2
        num = str(num)
        a = urllib.request.urlopen(site + num) 
    


