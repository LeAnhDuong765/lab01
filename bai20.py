#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:36:22 2024

@author: bang_angel03
"""
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
max_value =a
if a>b and a>c:
    print("Max: ",a)
elif b>a and b>c:
    print("Max: ",b)
elif c>a and c>b:
    print("Max",c)

