# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:35:21 2019

@author: Ken
"""

# 例外ハンドラ

short_list = list(range(3))

for i in range(10):
    try:
        short_list[i]
    except IndexError as err:
        print(err)
        print("the given index is too short..", i)
        print("must be smaller than:", len(short_list)-1)
    except:
        print("something bad happened")
