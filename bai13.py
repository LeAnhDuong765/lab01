#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:19:35 2024

@author: bang_angel03
"""
ngay_thang_nam= input("Nhập ngày tháng năm (dd mm yyyy):")
dd, mm, yyyy =ngay_thang_nam.split(" ")
print(dd,"/",mm,"/",yyyy)
print(dd,"/",mm,"/",yyyy[2:4])
print(yyyy,"/",mm,"/",dd)
a=input("Nhập theo định dạng Ngày/tháng/năm:")
b=input("Nhập theo định dạng Ngày/tháng/ 2 số cuối của năm:")
c=input("Nhập theo định Năm/tháng/ngày:")
day_a, month_a, year_a= map(int(a.split('/')))
day_b, month_b, year_b= map(int(b.split('/')))
nam_hien_tai=24 # 2 số cuối hiện tại của năm 2024
year_b +=1900 if year_b > nam_hien_tai else 2000
year_c, month_c, day_c= map(int(c.split('/')))
print("Kết quả từ a", day_a, month_a, year_a)
print("kết quả từ b", day_b, month_b, year_b)
print("kết quả từ c", day_c, month_c, year_c)