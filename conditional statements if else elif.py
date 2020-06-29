# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:42:39 2020

@author: shiwa
"""
###################TASKONE

length=int(input("enter the lenghth"))
breadth=int(input("enter the breadth"))
if (length==breadth) :
    print("square")
else:
    print("not")
    
    
################TASKTWO

sal=int(input("enter the sal"))
yrofservice=int(input("enter year of service"))
if sal>25000 and yrofservice>3:
    netbonus=sal*(5/100)
    netsalary=netbonus+sal
    print(netsalary,netbonus)
else:
    print("false")
    
    
    ############################    TASK THREE


marks=int(input("enter ypur marks"))
if marks<25:
    print("FAIL")
elif marks>=25 and marks<45:
    print("E")
elif marks>=45 and marks<50:
    print("D")
elif marks>=50 and marks<60:
    print("C")
elif marks>=60 and marks<80:
    print("B")
else:
    print("A")
     

#####################TSK FOUR     
    
    
age=int(input("enter ur age"))
if age<4:
        print ("no charge")
elif age>=4 and age<18:
    print("5rs")
else:
    print("10rs")    
    
    
    ################# CALCULATE ELEcTRICITY BILL
    
unit=int(input("enter the units"))
if unit>=1 and unit<=100:
    print("bill",unit*20)
elif unit>=100 and unit<=200:
    print("bill",unit*30)  
elif unit>=200 and unit<=300:
    print("bill",unit*40)  
elif unit>=300:
    print("bill",unit*50) 
     
    
    ########################  
    

for num in range(51):
    if num %5==0 and num%3==0:
        print("fizzbuzz")
    elif num %3==0:
        print("fizz")
        continue
    elif num %5==0:
        print("BUzz")
        continue
    else:
        print(num)


