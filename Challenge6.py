# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:14:45 2015

@author: GeneralTsao
"""

import zipfile
import re

file = zipfile.ZipFile("channel.zip")
nameList = file.filelist
bigDict = dict()
for name in nameList:
    f = file.open(name)
    nextNum = f.read().decode('utf-8')
    bigDict[name.filename] = (nextNum, name.comment)
    
txt = ".txt"
ans = "90052"
message = ""
while(True):
    text = bigDict[ans + txt][0]
    comment = bigDict[ans + txt][1].decode('utf-8')
    message += comment
    try:
        ans = re.findall("\d+", text)[0]
    except IndexError:
        break

print(message)
