# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:22:45 2021

@author: kokeb
"""

count=0
while count<100:
    print("progrmming is fun")
    count=count+1
    
    
sum=0
i=1
while i<10:
    sum=sum+i
    i=i+1
print(sum)    
    
import random
r1=random.randint(0,9)
r2=random.randint(0,9)
answer=abs(eval(input("what is the deifference between"+str(r1)+"and"+str(r2)))) 
while answer!=abs(r1-r2):
    answer=eval(input("wrong try again"))
print("right") 


import random
num=random.randint(0,100)
guess=-1
while guess!=num:
    guess=eval(input("guess"))    
    if guess<num:
        print("you r too low")
    elif guess>num:
        print("u r too high")
print("u got it")  




'''import random
i=0
while i<5:
  r1=random.randint(0,9)
  r2=random.randint(0,9)
  diff=abs(eval(input("diff bn"+str(r1)+"and"+str(r2))))
  if diff!=abs(r1-r2):'''
      
      
data=eval(input("integer"))
sum=0
while data !=0:
  sum=sum+data
  data=eval(input("integer"))
#python Chap5.py <input.txt      
print(sum)      


num=0
sum=0
for count in range(5):
  num=eval(input("integer")) 
  sum+=num
print(sum) 


i=1
for sum in range(10000):
  sum=sum+i
  i=i+1    
  
  
for j in range(1,10):
    print(" ",j,end= '')
print()
print("---------------------")
for i in range(1,10):
    print(i,"|",end='')    
    for j in range(1,10):
        print(format(i*j,"4d"),end='')
    print()    


n1=eval(input("enter the first integer"))
n2=eval(input("the second integer"))
gcd=1
k=2
while k<=n1 and k<=n2:
 if n1%k==0 and n2%k==0:
     gcd=k
 k=k+1  

n1=eval(input("enter the first integer"))
n2=eval(input("the second integer"))
gcd=1
k=2
while k<=n1/2 and k<=n2/2:
 if n1%k==0 and n2%k==0:
     gcd=k
 k=k+1  


year=0
tuition=10000
while tuition<20000:
    year=year+1
    tuition=tuition*1.07
print(year)


import random
numofHits=0
for i in range(1000000):
 x=random.random()*2-1
 y=random.random()*2-1
 if x**2+y**2<=1:
     numofHits+=1
pi=4*numofHits/1000000
print(pi)     
 
sum,num=0,0
while num<20:
    num+=1
    sum+=num
    if sum>=100:
        break
print(num)   

sum,num=0,0
while num<20:
    num+=1
    if num==10 or num==11:
        continue
    sum+=num
    
print(sum)

number=2
count=0
while count<50:
    for j in range(2,number):
        if number%j==0:
            continue
        print (number)
        count+=1
    number+=1  


import turtle
import random
turtle.speed(1)
turtle.color("gray")
x=-80
for y in range (-80,80+1,10):
   turtle.penup()
   turtle.goto(x,y)
   turtle.pendown()
   turtle.forward(160)
   
y=80
turtle.right(90)
for x in range (-80,80+1,10):
   turtle.penup()
   turtle.goto(x,y)
   turtle.pendown()
   turtle.forward(160)

turtle.color("red")
turtle.pensize(3)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
x=y=0
while abs(x)< 80 and abs(y)<80:
    r=random.randint(0,3)
    if r==0:
        x+=10
        turtle.setheading(10)
        turtle.forward(10)
    elif r==1:    
        y+=10
        turtle.setheading(10)
        turtle.forward(10)
    elif r==2:    
        x-=10
        turtle.setheading(10)
        turtle.forward(10)
    elif r==3:    
        y+=10
        turtle.setheading(10)
        turtle.forward(10)
        
        
        
        
        