#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:19:19 2024

@author: bang_angel03
"""

N=int(input("Nhập năm sinh:"))
if N<2024: 
    print("Bạn sinh năm",N,"vậy bạn",2024-N,"tuổi")
else:
    print("Không hợp lệ")