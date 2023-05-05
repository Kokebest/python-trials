# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 06:43:10 2021

@author: kokeb
"""
#4.1-4.6 done on phone

#4.7

#4.8
x,y,z=eval(input("numbers"))
a=max(x,y)
b=max(y,z)
c=max(x,z)
if x>y and z>y:
    if x>z:
     print(x,z,y)
    else:
     print(z,x,y)
elif x>z and y>z:
    if x>y:
     print(x,y,z)
    else:
     print(y,x,z) 
elif z>x and y>x:
    if z>y:
     print(z,y,x)
    else:
     print(y,z,x)
     
     
#4.9     
weight1,price1=eval(input("weight and price")) 
weight2,price2=eval(input("weight and price")) 

cost1=weight1/price1
cost2=weight2/price2

if cost1>cost2:
    print("package 1")
else:
    print("package 2")
    
    
    
#4.10    
import random
a=random.randint(0,100)
b=random.randint(0,100)
product=eval(input("what is the product of " +str(a)+"and"+str(b))) 
if product==a*b:
  print("correct")




#4.11  
year,month=eval(input("year and month?"))

if month==1:
     print("its January with 31 days")
elif month==2:
     isLeapyear=(year%4==0 and year%100!=0) or (year%400==0)   
     if isLeapyear == True:
         print ("its February with 29 days")
     else:
         print ("its February with 28 days")
elif month==3:
     print("its March with 31 days")             
elif month==4:
     print("its April with 30 days") 
elif month==5:
     print("its May with 31 days")    
elif month==6:
     print("its June with 30 days") 
elif month==7:
     print("its July with 31 days")
elif month==8:
     print("its August with 31 days")  
elif month==9:
     print("its September with 30 days")
elif month==10:
     print("its October with 31 days") 
elif month==11:
     print("its November with 30 days")
elif month==12:
     print("its December with 31 days")  
     
     
#4.12
x=eval(input("number?"))
if x%5==0 and x%6==0:
 print("is it diviible by both True")
else:
 print ("is it diviible by both false") 
if x%5==0 or x%6==0:
 print("is it divisible by one True")
else:
 print ("is it divisible by one false")    
if (x%5==0 and x%6!=0) or (x%5!=0 and x%6==0):
 print("is it divisible by one but not both True")
else:
 print ("is it divisible by one but not both false")       
     
#4.13     
status=eval(input("single,married,married but separately, head of household")) 
income=eval(input("income"))
tax=0
if status==0:
   if income<=8350:
        tax=10*income/100
   elif income<=33950:
        tax=10*8350/100+15*(income-8350)/100
   elif income<=82250:
        tax=10*8350/100+(33950-8350)*15/100+25*(income-33950)/100
   elif income<=171550:
        tax=10*8350/100+(33950-8350)*15/100+25*(82250-33950)/100+28*(income-82250)/100
   elif income<=372950:
        tax=10*8350/100+(33950-8350)*15/100+25*(82250-33950)/100+28*(171550-82250)/100+0.33*(income-171550)
   else: 
        tax=10*8350/100+(33950-8350)*15/100+25*(82250-33950)/100+28*(171550-82250)/100+0.33*(372950-171550)+0.35*(income-372950)
elif status==1:
   if income<16700:
        tax=10*income/100
   elif income<67900:
        tax=10*16700/100+15*(income-16700)/100
   elif income<137050:
        tax=10*16700/100+(67900-16700)*15/100+25*(income-67900)/100
   elif income<208850:
        tax=10*16700/100+(67900-16700)*15/100+25*(137050-67900)/100+28*(income-137050)/100
   elif income<372950:
        tax=10*16700/100+(67900-16700)*15/100+25*(137050-67900)/100+28*(208850-137050)/100+0.33*(income-208850)
   else: 
        tax=10*16700/100+(67900-16700)*15/100+25*(137050-67900)/100+28*(208850-137050)/100+0.33*(372950-208850)+0.35*(income-372950)
elif status==2:
   if income<8350:
        tax=10*income/100
   elif income<33950:
        tax=10*8350/100+15*(income-8350)/100
   elif income<68525:
        tax=10*8350/100+(33950-8350)*15/100+25*(income-33950)/100
   elif income<104425:
        tax=10*8350/100+(33950-8350)*15/100+25*(68525-33950)/100+28*(income-68525)/100
   elif income<186475:
        tax=10*8350/100+(33950-8350)*15/100+25*(68525-33950)/100+28*(104425-68525)/100+0.33*(income-104426)
   else: 
        tax=10*8350/100+(33950-8350)*15/100+25*(68525-33950)/100+28*(104425-68525)/100+0.33*(186475-171550)+0.35*(income-186476)    
elif status==3:
   if income<11950:
        tax=10*income/100
   elif income<45500:
        tax=10*11950/100+15*(income-11950)/100
   elif income<117450:
        tax=10*11950/100+(45500-11950)*15/100+25*(income-45500)/100
   elif income<190200:
        tax=10*11950/100+(45500-11950)*15/100+25*(117450-45500)/100+28*(income-117450)/100
   elif income<372950:
        tax=10*11950/100+(45500-11950)*15/100+25*(117450-45500)/100+28*(190200-117450)/100+0.33*(income-190200)
   else: 
        tax=10*11950/100+(45500-11950)*15/100+25*(117450-45500)/100+28*(190200-117450)/100+0.33*(372950-190200)+0.35*(income-372950)
print(tax)       



#4.14
import random
u=random.randint(0,1)
z=input("Heads or tails? enter H or T")
if u==0:
    if z=='H':
        print("correct")
    else:
        print("nah it was tails")
if u==1:
    if z=='T':
        print("correct")
    else:
        print("nah it was heads") 
        

#4.15
g=eval(input("enter a three digit number"))
d1=g//100
r1=g%100
d2=r1//10
d3=r1%10
import random
t=random.randrange(100,1000)
dr1=t//100
rr1=t%100
dr2=rr1//10
dr3=rr1%10
if g==t:
 print("u win 10000")     

elif (dr1==d1 or dr1==d2 or dr1==d3) and (dr2==d1 or dr2==d2 or dr2==d3) and ((dr3==d1 or dr3==d2 or dr3==d3)):
  print("u won 3000")

elif (dr1==d1 or dr1==d2 or dr1==d3) or (dr2==d1 or dr2==d2 or dr2==d3) or ((dr3==d1 or dr3==d2 or dr3==d3)):
  print("u won 1000")   

else:
  print("u got nothing") 
  
#4.16  
import random
j=random.randint(65,90)
print(chr(j)) 

#4.17
import random
y=random.randint(0,2)
d=input("rock,paper, scissor?")
if y==0:
    if d=='rock':
        print("both rock")
    elif d=='scissor':
        print("rock-scissor u lost")
    elif d=='paper':
        print("rock-paper u won")    
if y==1:
    if d=='rock':
        print("scissor-rock u won")
    elif d=='scissor':
        print("both scissor")
    elif d=='paper':
        print("scissor-paper u lost")    
if y==2:
    if d=='rock':
        print("paper rock u lost")
    elif d=='scissor':
        print("paper-scissor u won")
    elif d=='paper':
        print("paper-paper")
        
#4.18        
i=eval(input("exchange rate"))
k=eval(input("dollar to RMI (0) or RMI to dollar (1) "))
if k==0:
    moneyInDollar=eval(input("money in dollar"))
    moneyInRMI=moneyInDollar*i
    print(moneyInRMI)
elif k==1:
    moneyInRMI=eval(input("money in RMI"))
    moneyInDollar=moneyInRMI/i
    print(moneyInDollar) 
else:
   print("incorrect input")    
      

#4.19
u,v,x=eval(input("3 edges")) 
if u+v>x and v+x>u and u+x>v:
    print("perimeter is", u+v+x)
else:
    print("incorrect input") 
    
    
    
    
#4.20    
temperature=eval(input("temp in fahrenheight")) 
windSpeed=eval(input("wind speed")) 
if temperature>=-58 and temperature<=41 and windSpeed>=2: 
   windChillIndex=35.74+0.6215*temperature-35.75*(windSpeed)**0.16+0.4275*temperature*(windSpeed)**0.16 
   print(windChillIndex)
else:
    print("incorrect input")
    
#4.21 error
import math    
year=eval(input("enter year"))
month=eval(input("enter month"))
if month==1:
    month=13
    year=year-1
elif month==2:
   month=14
   year=year-1
else:
   month=month
   year=year     
day=eval(input("day of the month"))
h=(day+(26*(month+1)/10)+year%100+(year%100)/4+(year/400)+5*year/100)%7
h=math.ceil(h)
if h==0:
 print("saturday")
elif h==1:
 print("sunday")
elif h==2:
 print("monday")
elif h==3:
 print("tuesday") 
elif h==4:
 print("wedensday")
elif h==5:
 print("thursday") 
elif h==6:
 print("friday") 
 
#4.22 
x1,y1=eval(input("insert a point"))
r=10
d=(x1**2+y1**2)**0.5 
if d<=r:
    print("inside")
else:
    print("outside")
 
#4.23
x1,y1=eval(input("insert a point"))
x2,y2=10,5
if x1<=x2/2 and y1<=y2/2:
    print("inside")
else:
    print("outside")
    
    
#4.24
import random
rankOfCard=random.randint(1,13)
suitOfCard=random.randint(1,4)
if suitOfCard == 1:
    suit='clubs'
    if rankOfCard == 1:
        print("u picked the Ace of", suit)
    elif rankOfCard == 2:
        print("u picked the 2 of", suit)
    elif rankOfCard == 3:
        print("u picked the 3 of", suit)
    elif rankOfCard == 4:
        print("u picked the 4 of", suit)
    elif rankOfCard == 5:
        print("u picked the 5 of", suit)    
    elif rankOfCard == 6:
        print("u picked the 6 of", suit) 
    elif rankOfCard == 7:
        print("u picked the 7 of", suit)
    elif rankOfCard == 8:
        print("u picked the 8 of", suit)
    elif rankOfCard == 9:
        print("u picked the 9 of", suit)
    elif rankOfCard == 10:
        print("u picked the 10 of", suit)
    elif rankOfCard == 11:
        print("u picked the Jack of", suit)
    elif rankOfCard == 12:
        print("u picked the Queen of", suit) 
    elif rankOfCard == 13:
        print("u picked the King of", suit)    
elif suitOfCard == 2:
    suit='Diamonds'
    if rankOfCard == 1:
        print("u picked the Ace of", suit)
    elif rankOfCard == 2:
        print("u picked the 2 of", suit)
    elif rankOfCard == 3:
        print("u picked the 3 of", suit)
    elif rankOfCard == 4:
        print("u picked the 4 of", suit)
    elif rankOfCard == 5:
        print("u picked the 5 of", suit)    
    elif rankOfCard == 6:
        print("u picked the 6 of", suit) 
    elif rankOfCard == 7:
        print("u picked the 7 of", suit)
    elif rankOfCard == 8:
        print("u picked the 8 of", suit)
    elif rankOfCard == 9:
        print("u picked the 9 of", suit)
    elif rankOfCard == 10:
        print("u picked the 10 of", suit)
    elif rankOfCard == 11:
        print("u picked the Jack of", suit)
    elif rankOfCard == 12:
        print("u picked the Queen of", suit) 
    elif rankOfCard == 13:
        print("u picked the King of", suit)
elif suitOfCard == 3:
    suit='Hearts'
    if rankOfCard == 1:
        print("u picked the Ace of", suit)
    elif rankOfCard == 2:
        print("u picked the 2 of", suit)
    elif rankOfCard == 3:
        print("u picked the 3 of", suit)
    elif rankOfCard == 4:
        print("u picked the 4 of", suit)
    elif rankOfCard == 5:
        print("u picked the 5 of", suit)    
    elif rankOfCard == 6:
        print("u picked the 6 of", suit) 
    elif rankOfCard == 7:
        print("u picked the 7 of", suit)
    elif rankOfCard == 8:
        print("u picked the 8 of", suit)
    elif rankOfCard == 9:
        print("u picked the 9 of", suit)
    elif rankOfCard == 10:
        print("u picked the 10 of", suit)
    elif rankOfCard == 11:
        print("u picked the Jack of", suit)
    elif rankOfCard == 12:
        print("u picked the Queen of", suit) 
    elif rankOfCard == 13:
        print("u picked the King of", suit) 
elif suitOfCard == 4:
    suit='Spades'
    if rankOfCard == 1:
        print("u picked the Ace of", suit)
    elif rankOfCard == 2:
        print("u picked the 2 of", suit)
    elif rankOfCard == 3:
        print("u picked the 3 of", suit)
    elif rankOfCard == 4:
        print("u picked the 4 of", suit)
    elif rankOfCard == 5:
        print("u picked the 5 of", suit)    
    elif rankOfCard == 6:
        print("u picked the 6 of", suit) 
    elif rankOfCard == 7:
        print("u picked the 7 of", suit)
    elif rankOfCard == 8:
        print("u picked the 8 of", suit)
    elif rankOfCard == 9:
        print("u picked the 9 of", suit)
    elif rankOfCard == 10:
        print("u picked the 10 of", suit)
    elif rankOfCard == 11:
        print("u picked the Jack of", suit)
    elif rankOfCard == 12:
        print("u picked the Queen of", suit) 
    elif rankOfCard == 13:
        print("u picked the King of", suit)                   
        
        
        
        
#4.25        
x1,y1,x2,y2,x3,y3,x4,y4=eval(input("enter the 4 points"))
if ((y1-y2)*(x4-x3)-(x2-x1)*(y3-y4))!=0:
 x=((((y1-y2)*x1-(x1-x2)*y1)*(x4-x3))-(((y3-y4)*x3-(x3-x4)*y3)*(x2-x1)))/((y1-y2)*(x4-x3)-(x2-x1)*(y3-y4))
 y=(((y3-y4)*x3-(x3-x4)*y3)*(y1-y2)-((y1-y2)*x1-(x1-x2)*y1)*(y3-y4))/((y1-y2)*(x4-x3)-(x2-x1)*(y3-y4))
 print('(',x,',',y,')', "is the point of intersection")
elif ((y1-y2)*(x4-x3)-(x2-x1)*(y3-y4))==0:
 print("parallel")    
 
#4.26 
number=eval(input("number?"))
d1=number//100
r1=number%100
d2=number//10
d3=number%10
if (d1==d3):
    print("palindrome")
else:
    print("nah")  
    
#4.27   
x1,y1=eval(input("enter point"))
if x1<=200 and y1<=-0.5*x1+100:
  print("inside") 
else:
    print("outside")
    
#4.28   
cx1,cy1,w1,h1=eval(input("insert center and width and height"))
cx2,cy2,w2,h2=eval(input("insert center, width, and height")) 
if w2<=w1 and h2<=h1 and abs(cx1-cx2)<=w1/2 and abs(cy1-cy2)<=h2/2: 
    print("inside")
elif abs(cx1-cx2)<=(w1+w2)/2 or abs(cy1-cy2)<=(h1+h2)/2:
    print("overlap")    
else:
    print("nothing")

#4.29    
cx1,cy1,r1=eval(input("radius and center")) 
cx2,cy2,r2=eval(input("radius and center"))
if ((((cx2-cx1)**2+(cy2-cy1)**2))**0.5)<=abs(r1-r2):
    print("inside")
elif ((((cx2-cx1)**2+(cy2-cy1)**2))**0.5)<=(r1+r2):
    print("overlap") 
else:
    print("nothing") 
    

#4.30

    
#4.31
p0x,p0y,p1x,p1y,p2x,p2y=eval(input("p0,p1,p2"))
if ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))>0:
  print("left")
elif ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))==0:
  print("same line")  
elif ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))<0:
  print("right")

#4.32
p0x,p0y,p1x,p1y,p2x,p2y=eval(input("p0,p1,p2"))
m=(p1y-p0y)/(p1x-p0x)
b=p1y-m*p1x
if p0x<p2x<p1x and p0y<p2y<p1y and p2y-b-m*p2x == 0:
   print("on the line")
else:
  print("not on line")  
  
#4.33
num=eval(input("decimal?"))
if 0<=num<=9:
    print("hex is ", num)
elif num==10:    
    print("hex is A") 
elif num==11:    
    print("hex is B")
elif num==12:    
    print("hex is C")
elif num==13:    
    print("hex is D")
elif num==14:    
    print("hex is E")
elif num==15:    
    print("hex is F")
else:
    print("invalid input")

#4.34 error
num=input("hex?")
'''if '0'<=num<='9':
    print("decmial is ", num)'''
elif num=='A' or 'a':    
    print("decimal is 10") 
elif num=='B' or 'b':    
    print("decimal is 11")
elif num=='C' or 'c':    
    print("decimal is 12")
elif num=='D' or 'd':    
    print("decimal is 13")
elif num=='E' or 'e':    
    print("decimal is 14")
elif num=='F' or 'f':    
    print("decimal is 15")    
else:
    print("invalid input")
    
 
#4.35
p0x,p0y,p1x,p1y,p2x,p2y=eval(input("p0,p1,p2"))
import turtle
turtle.penup()
turtle.goto(p0x,p0y)
turtle.pendown()
turtle.goto(p1x,p1y)
if ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))>0:
    turtle.begin_fill()
    turtle.goto(p2x,p2y)
    turtle.circle(3)
    turtle.end_fill()
    turtle.goto(p2x+1,p2y+1) 
    turtle.write("left")
elif ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))==0:
    turtle.begin_fill()
    turtle.goto(p2x,p2y)
    turtle.circle(3)
    turtle.end_fill()
    turtle.goto(p2x+1,p2y+1) 
    turtle.write("on line")
elif ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))<0:
    turtle.begin_fill()
    turtle.goto(p2x,p2y)
    turtle.circle(3)
    turtle.end_fill()
    turtle.goto(p2x+1,p2y+1) 
    turtle.write("right")
    
    
#4.36
    
    
         
