#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:41:13 2024

@author: bang_angel03
"""

sx=int(input("Nhập số xe có 4 chữ số:"))
hang_nghin= sx // 1000
hang_tram= (sx % 1000) //100
hang_chuc= ((sx % 1000) % 100) // 10
hang_donvi=(sx % 10)
sn= hang_nghin + hang_tram + hang_chuc + hang_donvi
if 0<= sn <=9:
    print("Số nút của bạn là:",sn)
else:
    print("Số nút của bạn là:",sn %10)