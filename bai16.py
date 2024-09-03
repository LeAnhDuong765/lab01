#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:50:47 2024

@author: bang_angel03
"""

time= input("Nhập giờ, phút, giây (hh mm ss):")
time1= time.split()
gio= int(time1[0])
phut= int(time1[1])
giay= int(time1[2])
tong= gio *3600 + phut *60 + giay
print("Tổng số giây:",tong)