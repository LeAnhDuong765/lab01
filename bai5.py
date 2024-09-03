#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:14:01 2024

@author: bang_angel03
"""

tg=input("Nhập thời gian (hh:mm:ss):")
gio, phut, giay =map(int,tg.split(":"))
tong= giay + phut*60 + gio*3600
print("Tổng số giây là:",tong)