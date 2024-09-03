#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:04:40 2024

@author: bang_angel03
"""
import math
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
denta= b**b - (4*a*c)
if a==0:
    print("Pt có 1 nghiệm duy nhất x=", -b/c)
elif a !=0 and denta <0:
    print("Pt vô nghiệm")
elif a !=0 and denta ==0:
    print("Pt có nghiệm kép x1=x2=", -b/(2*a))
elif a !=0 and denta >0:
    print("Pt có 2 nghiệm x1=",(-b+ math.sqrt(denta))/(2*a))
    print("Pt có 2 nghiệm x2=",(-b - math.sqrt(denta))/(2*a))