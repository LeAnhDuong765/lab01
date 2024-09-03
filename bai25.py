#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:19:44 2024

@author: bang_angel03
"""

chucai = input("Nhập vào chữ cái thường:")
if chucai.islower():
    chucai = chucai.upper()
elif chucai.isupper():
    chucai = chucai.lower()
else:
    print("Đây không phải là chữ cái hợp lệ")
print("Kết quả", chucai)