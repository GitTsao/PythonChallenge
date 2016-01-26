# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:20:45 2015

@author: GeneralTsao
"""

import pickle

a = pickle.load(open("banner.p",'rb'))

for combo in a:
    print("".join(symbol*num for symbol, num in combo))