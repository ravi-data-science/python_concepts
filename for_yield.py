#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:07:43 2019

@author: rkrovvidi
"""


def readUsers():
    with open("/etc/passwd") as f:
        for line in f:
            yield line.split(":")[0]
            
 

for user in  readUsers():
    print (user)           