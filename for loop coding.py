# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:01:17 2020

@author: shiwa
"""


###############divisiblity check

list=[12,15,32,42,55,75,122,150]
for val in list:
   if val%5==0:
    print(val)
    
    ####################### LOOP 
    
list=[]
for i in range (1,50):
    if i %2!=0:
        list.append(i)
print(list)
        


################table

num=int(input("enter a number"))
for i in range (1,50):
    table=num*i
    print(table)
    
    
    ###################  FACTORIAL OF A NUMBER

fact=1
num=int(input("enter the number"))
for i in range (2,num+1):
    fact=fact*i
print(fact)


#################   FIBONACI SERIES

num=int(input("enter the value"))
i=0
j=1
for f in range(1,num):
    k=i+j
    i=j
    j=k
    print(k)
    

################ PRINT THE LEN OF ELEMENT IN LIST
    

list=["PYTHHON","SHIWANI","CHIKU","JULIE"]
leng=len(list)
print(leng)
for i in range(0,leng):
    d=len(list[i])
    print(list[i],d)
    

######################## POP ROCK JAZZ
    
    
b=["POP","ROCK","JAZZ"]
leng=len(b)
print(leng)
for i in range(0,leng):
    print("I LIKE",b[i])
    

    
#################### OUTPUT [2,4,9,16,25,36,49,64 ......]
    
num=int(input("enter the number"))
list=[]
for i in range (1,num):
    d=i*i
    list.append(d)
print(list)


############## x=[1,2,3], y=[2,1,3] op={(1,2),(1,3)......}

x=[1,2,3,4]
y=[3,2,1,4]
comb=[]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        if x[i]!=y[j]:
            d=x[i],y[j]
            comb.append(d)
print(comb)            



################# PRIME NUMBER

num=int(input("enter the number"))
count=0
for i in range(1,num):
    if num%i==0:
        count=count+1
    if count==2:
            print("prime")
    else:
            print("nt")
                
        