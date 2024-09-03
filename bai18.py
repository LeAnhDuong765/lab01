#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:19:58 2024

@author: bang_angel03
"""

thoi_gian_1 = input("Nhập thời gian thứ nhất(hh:mm:ss) ")
thoi_gian_2 = input("Nhập thời gian thứ hai(hh:mm:ss) ")
hh, mm, ss = map(int, thoi_gian_1.split(":"))
h, m, s = map(int, thoi_gian_2.split(":"))
tong_giay_1 = hh * 3600 + mm * 60 + ss
tong_giay_2 = h * 3600 + m * 60 + s
hieu_thoi_gian = tong_giay_1 - tong_giay_2
if hieu_thoi_gian > 0:
    h1 = hieu_thoi_gian // 3600
    m1= (hieu_thoi_gian %3600)//60
    s1=(hieu_thoi_gian)%60
    print("Hiệu của 2 thời gian là:", h1, ":",m1,":",s1)
else:
    print("Thời gian nhỏ hơn")
tong_thoi_gian= tong_giay_1 + tong_giay_2
h2= tong_thoi_gian //3600
m2= (tong_thoi_gian % 3600) // 60
s2= tong_thoi_gian % 60
print("Tổng của 2 thời gian:",h2,":",m2,":",s2)