#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:58:05 2024

@author: bang_angel03
"""

a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
if a==0 and b==0:
    print("pt có vô số nghiệm")
elif a==0 and b !=0:
    print("pt vô nghiệm")
else:
    print("pt có một nghiệm x=",-b/a)