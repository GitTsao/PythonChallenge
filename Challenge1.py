# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
#k -> m
#O -> Q
#E -> G

fromArray = "abcdefghijklmnopqrstuvwxyz"
toArray = "cdefghijklmnopqrstuvwxyzab"
yup = []
yupper = []

trans = str.maketrans(fromArray, toArray)

example = "map"

print(example.translate(trans))