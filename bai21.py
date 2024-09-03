#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:50:30 2024

@author: bang_angel03
"""

N=int(input("Nhập số nguyên bất kì:"))
so_thanhchu={0:"không",
             1: "một",
             2: "hai",
             3: "ba",
             4: "bốn",
             5: "năm",
             6: "sáu",
             7: "bảy",
             8: "tám",
             9: "chín"}
if N in so_thanhchu:
    print(so_thanhchu[N])
else:
    print("không đọc được")
