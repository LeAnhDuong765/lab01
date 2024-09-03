#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:13:53 2024

@author: bang_angel03
"""

gio = int(input("Nhập giờ = "))
phut = int(input("Nhập phút = "))
giay = int(input("Nhập giây = "))
if gio > 24 or (phut and giay) > 60:
    print("Thời gian nhập vào không hợp lệ!")
else:
    print("Thời gian hợp lệ:",gio,phut,giay)