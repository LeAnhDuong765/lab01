#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:07:29 2024

@author: bang_angel03
"""

N=int(input("Nhập số nguyên dương có 2 chữ số:"))
if N>=10 and N<=99:
    print("Tổng các chữ số là:",N%10 + N//10)                                                                                           
else:
    print("Không hợp lệ")
    
        