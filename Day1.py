# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:02:21 2020

@author: shiwa
"""


print("hello world")


a=int(input("enter the number"));
b=int(input("enter the number"));
c=int(input("enter the number"));
if (a>b) and (a>c):
    print("a is largest");
    if b>a and b>c:
        print("b is largest");
else:
            print("c is largest");