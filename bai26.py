#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:23:27 2024

@author: bang_angel03
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)

N = input("Nhập số nguyên N= ")
danh_sach = list(N)
sap_xep = danh_sach.sort()
sap_xep_danh_sach = "".join(danh_sach)
print(sap_xep_danh_sach)