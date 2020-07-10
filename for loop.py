# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:30:08 2020

@author: shiwa
"""


num=int(input("enter the number"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)



############ print no divisible by 5 and stop when num is greater than 150

list=[12,15,32,44,67,150,56,98,43]
for i in list:
    if (i%5==0) and (i>150):
        break
    else:
        if i%5==0:
            print(i)
            
######### print product and if product is greater than 1000 print sum
            
num1=int(input("enter the number"))
num2=int(input("enter the number"))
product=num1 * num2
if product>1000:
    sum=num1+num2
    print(sum)
else:
    print(product)


########## given range of first 10 numbers .
#####3##print the sum of curent number and previous number till ten
    
    
for i in range(1,11):
    l=i-1
    sum=i+l
    print(sum)
    
    
#### display only those numbers which r present at even index position
    
list1=input("enter the list elements")
for i in range (0,len(list1)):
    if i%2==0:
        print(list1[i])
      
 ##### enter 2 list and pint odd 
    ####multiples frm list 1 and even from listc 2 in single list
        
list1=[1,6,8,9,7,35,44]
list2=[1,5,9,4,2,82,75]
l1=len(list1)
l2=len(list2)
print(l1)
print(l2)
a=[]
b=[]
for i in range(0,l1):
    if i%2!=0:
        a.append(list1[i])
for j in range(0,l2):
    if j%2==0:
        b.append(list2[j])
print(a,b)
    
    