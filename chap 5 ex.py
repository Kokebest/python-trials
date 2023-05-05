# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 06:21:39 2021

@author: kokeb
"""

#5.1
sum=0
num=-1
count=0
positive,negative=0,0
while (num!=0):
    num=eval(input("num?"))
    sum=sum+num
    if num!=0:
     count=count+1
     if num<0:
        negative+=1
    elif num>0:
        positive+=1
        
average=sum/count
print("positive",positive, "negative ", negative, "sum", sum, "average", average)        



#5.2
import random
import time
starttime=time.time()
correctAnswer=0
for i in range(10):
    num1=random.randint(1,15)
    num2=random.randint(1,15)
    difference=eval(input("what is the diff of "+str(num1)+" and "+str(num2)))
    i=i+1
    if difference==num1-num2:
        correctAnswer+=1

finishtime=time.time()
testtime=finishtime-starttime
print("u got ", correctAnswer, "correct answers in", testtime)


#5.3
i=0
print ("Kilogram","  ","Pounds")
while (i<=200):
    if (i%2 !=0):
     print(i,"    ",i*2.2) 
    i=i+1
            


#5.4
i=0
print ("Miles","  ","Kilogram")
while (i<=10):
    print(i,"    ",i*1.609) 
    i=i+1
    
    
#5.5
i=0
j=20
print ("kilogram","  ","pounds    ","|    ","Pounds","   ","kilogram")
for i in range (1,200,2):
    print(i,"        ",format(i*2.2,".2f"),end='    |    ')
    while j<=520:
     print(j,"    ",j*0.45) 
     j=j+5
     break
    print() 
    
 

#5.6
i=0
j=20
print ("miles","  ","kilometers    ","|    ","kilometer","   ","miles")
for i in range (1,11,1):
    print(i,"        ",format(i*1.609),end='    |    ')
    while j<=65:
     print(j,"    ",j*0.621) 
     j=j+5
     break
    print()


#5.7
import math
i=0
print("Degree","   ", "Sin", "   ","Cos")       
for i in range(0,370,10):
    print(i,"   ",format(math.sin(math.radians(i)),".4f"),"   ",format(math.cos(math.radians(i)),".4f"))
    


#5.8
import math
o=0
print("Number","   ", "square root")       
for o in range(0,22,2):
    print(o,"   ",format(math.sqrt(o),".4f"))
    

#5.9
u=10000
i=0.05
sum=0
for l in range(1,15,1):
    u=u+(u*i)
    if l==10:
        print("ten years from now tuition is ",u)
        continue
    if (l>=10 and l<15):
        sum=sum+u
print("a four year college will cost ", sum) 


#5.10
n=eval(input("what is the number of students"))
g=0 
for i in range(0,n,1):
   score=eval(input("insert score for students"))
   if score>g:
       g=score
print(g) 
          
#5.11


#5.12
count=0
for r in range(100,1000):
    if (r%5==0 and r%6==0):
        print(r,end=' ')
        count+=1
        if count%10==0:
          print()
        
#5.13
count=0
for r in range(100,200):
    if (r%5==0 or r%6==0):
        if (r%5==0 and r%6==0):
            continue
        print(r,end=' ')
        count+=1
        if count%10==0:
          print()
          
          
          
#5.14
n=0
y=0
while(y<13000):
    n=n+1
    y=n**2
    if y>12000:
        print (n)
        break
 
#5.15
n=0
y=0
while(y<13000):
    n=n+1
    y=n**3
    if y>=12000:
        break    
print(n-1)


#5.16
gcd=1
n1=eval(input("num1"))
n2=eval(input("num2"))
n3=min(n1,n2)
for k in range(n3,1,-1):
  if n1%k==0 and n2%k==0:
      gcd=k
      break

print(gcd)    
  
#5.17
count=0
for f in range (33,127):
    print(chr(f),end=' ')
    count+=1
    if count%10==0:
        print()
        
#5.18 error
num=eval(input("number")) 
isPrime=True
for u in range(0,num):
  divisor=2
  while divisor<num:
     if num%divisor==0:
         isPrime=False
         break
     divisor+=1
         
     
        
#5.19

#5.20a
line=eval(input("no of line"))
for i in range(0,line+1):
    for j in range(1,i+1):
     print(j, end=' ')
    print() 
        
#5.20b  
line=eval(input("no of line"))
for i in range(line,0,-1):
    for j in range(1,i+1,1):
     print(j, end=' ')
    print() 
            
#5.20c  
line=eval(input("no of line"))
for i in range(1,line+1,1):
    num=i
    for j in range(line,0,-1):
      if j>i:
        print(" ",end=' ')
      else:  
        print(num, end=' ')
        num-=1
    print()      
    

#5.23
loanAmount=eval(input("loan amount"))
loanPeriod=eval(input("loan period"))
print("Interest Rate","  ","Monthly Pay","  ","Total Pay")
monthlyInterest =5
while monthlyInterest<=8:
      monthlyPay=((monthlyInterest/1200)*loanAmount)/(1-1/((1+(monthlyInterest/1200))**(loanPeriod*12)))
      totalPay=monthlyPay*loanPeriod*12
      print(format(monthlyInterest,".3f"),"   ",format(monthlyPay,".2f"),"   ",format(totalPay,".2f"))
      monthlyInterest+=1/8


#5.24
loanAmount=eval(input("loan amount"))
loanPeriod=eval(input("loan period"))
annualInterestRate=eval(input("annual Interest"))
print("payment","\t\t","interest","\t\t","principal","\t\t","Balance")
monthlyPay=((annualInterestRate/1200)*loanAmount)/(1-1/((1+(annualInterestRate/1200))**(loanPeriod*12)))
balance=loanAmount
for month in range(1,loanPeriod*12+1):
  monthlyInterest=annualInterestRate*balance/1200
  principal=monthlyPay-monthlyInterest
  balance=balance-principal
  print(month,"\t\t\t\t", format(monthlyInterest,".2f"),"\t\t\t",format(principal, ".2f"),"\t\t",format(balance,".2f"))


#5.25
sum=0
sum2=1/50000
for n in range(1,50000,1):
  sum=sum+1/n
print(sum)
for m in range(500000-1,1,-1):
  sum2=sum2+1/m
print(sum2)

#5.26
sum=0
for n in range(1,97,2):
    sum=sum+n/(n+2)
    print(sum)

#5.27
sum=0
for i in range(1,10000):
    sum=sum+(((-1)**(i+1))/(2*i-1))
pi=4*sum
print (pi)
sum2=0
for i in range(1,20000):
    sum2=sum2+(((-1)**(i+1))/(2*i-1))
pi2=4*sum2
print (pi2)
sum3 = 0
for i in range(1,100000):
    sum3=sum3+(((-1)**(i+1))/(2*i-1))
pi3=4*sum3
print (pi3)

#5.28
sum=1
for i in range(1,1000,1):
    product = 1
    for j in range (i,0,-1):
        product=product*j
    sum=sum+1/product
print("e=",sum)
sum2=1
for o in range(1,2000,1):
    product2 = 1
    for p in range (o,0,-1):
        product2=product2*p
    sum2=sum2+1/product2
print("e=",sum2)
sum3=1
for q in range(1,10000,1):
    product3 = 1
    for w in range (q,0,-1):
        product3=product3*w
    sum3=sum3+1/product3
print("e=",sum3)



#5.29
count=0
for year in range (2001,2100,1):
    if ((year%4==0 and year%100!=0) or (year%400==0)):
        print(year,end= " ")
        count+=1
        if count%10==0:
            print()

#5.30
year=eval(input("year?"))
firstDay=eval(input("day?"))
num=firstDay
for i in range(2,13,1):
 if i==1:
    month='Jan'
    num=num+0
 if i == 2:
     month='Feb'
     num = num + 31 % 7
 if i == 3:
     month='March'
     num = num + 28 % 7
 if i == 4:
     month='April'
     num = num + 31 % 7
 if i == 5:
     month='May'
     num = num + 30 % 7
 if i == 6:
     month='June'
     num = num + 31 % 7
 if i == 7:
     month='July'
     num = num + 30 % 7
 if i == 8:
     month='August'
     num = num + 31 % 7
 if i == 9:
     month='Sept'
     num = num + 31 % 7
 if i == 10:
     month='Oct'
     num = num + 30 % 7
 if i == 11:
     month='Nov'
     num = num + 31 % 7
 if i == 12:
     month='Dec'
     num = num + 30 % 7
 if num==1 or num==8 or num==15 or num==22:
    day='Monday'
 if num==2 or num==9 or num==16 or num==23:
    day='Tuesday'
 if num==3 or num==10 or num==17 or num==24:
    day='Wedensday'
 if num==4 or num==11 or num==18 or num==25:
    day='Thursday'
 if num==5 or num==12 or num==19 or num==26:
    day='Friday'
 if num==6 or num==13 or num==20 or num==27:
    day='Saturday'
 if num==7 or num==14 or num==21 or num==28:
    day='Sunday'
 print("the first day of",month, "is on",day)

    
#5.31 error 
year=eval(input("year?"))
firstDay=eval(input("day?"))
num=firstDay
for i in range(2,13,1):
 if i==1:
    month='Jan'
    num=num+0
    print(month,year)
    print ("Mon   ","Tues","Wed ","Thu ","Fri ","Sat ","Sun ")
    count=0
    for j in range (1,31,1):
        print (j)
        if count==7:
            print()
 if i == 2:
     month='Feb'
     num = num + 31 % 7
 if i == 3:
     month='March'
     num = num + 28 % 7
 if i == 4:
     month='April'
     num = num + 31 % 7
 if i == 5:
     month='May'
     num = num + 30 % 7
 if i == 6:
     month='June'
     num = num + 31 % 7
 if i == 7:
     month='July'
     num = num + 30 % 7
 if i == 8:
     month='August'
     num = num + 31 % 7
 if i == 9:
     month='Sept'
     num = num + 31 % 7
 if i == 10:
     month='Oct'
     num = num + 30 % 7
 if i == 11:
     month='Nov'
     num = num + 31 % 7
 if i == 12:
     month='Dec'
     num = num + 30 % 7
 if num==1 or num==8 or num==15 or num==22:
    day='Monday'
 if num==2 or num==9 or num==16 or num==23:
    day='Tuesday'
 if num==3 or num==10 or num==17 or num==24:
    day='Wedensday'
 if num==4 or num==11 or num==18 or num==25:
    day='Thursday'
 if num==5 or num==12 or num==19 or num==26:
    day='Friday'
 if num==6 or num==13 or num==20 or num==27:
    day='Saturday'
 if num==7 or num==14 or num==21 or num==28:
    day='Sunday'
 print("the first day of",month, "is on",day) 




#5.32
Amount=eval(input("amount?"))
annualInterest=eval(input("annual interest"))
numberOfMonths=eval(input("no of month"))
#n=eval(input("which month do you want to know?"))
accountValue=0
n=1
while n<=numberOfMonths:
  accountValue=(accountValue+Amount)*(1+annualInterest/1200)
  print(accountValue)
  n=n+1



#5.33
Amount=eval(input("amount?"))
annualInterest=eval(input("annual interest"))
numberOfMonths=eval(input("no of month"))
#n=eval(input("which month do you want to know?"))
accountValue=Amount+(Amount)*(annualInterest/1200)
print(1, accountValue)
n=2
while n<=numberOfMonths:
  accountValue=accountValue+(accountValue)*(annualInterest/1200)
  print(n, accountValue)
  n=n+1 


#5.34
import random
d1=random.randint(0,9)
for i in range(1,100):
    d2=random.randint(0,9)
    if d2==d1:
        continue
    if d2!=d1:
        break
lottery=d1*10+d2
guess=eval(input("number"))
gd1=guess//10
gd2=guess%10
if guess==lottery:
     print ("u win 10000")
elif gd1==d2 and gd2==d1:
     print ("u win 3000")
elif (gd1==d1 or gd1 == d2 or gd2 == d1 or gd2 == d2):
     print("Match one digit: you win $1,000")     
else:
    print("loss")     
    
    
  
#5.35
for i in range(1,10000):
    sum=0
    for j in range(1,i):
     if i%j==0:
        sum=sum+j
    if sum==i:
        print("perfect number",i)


#5.36
import random
compWin,uWin=0,0
while compWin<=2 or uWin<=2:
    compchoose=random.randint(0,2)
    uchoose=eval(input("rock(1),paper(2),scissors(0)"))    
    if uchoose==0:
        if compchoose==0:
            print ("draw")
            continue
        if compchoose==1:
            print ("compwins")
            compWin=compWin+1
        if compchoose==2:
            print ("uwins")
            uWin=uWin+1
    if uchoose==1:
        if compchoose==0:
            print ("uwin")
            uWin=uWin+1
        if compchoose==1:
            print ("draw")
            continue
        if compchoose==2:
            print ("compwin")
            compWin=compWin+1
    if uchoose==2:
        if compchoose==0:
            print ("compwin")
            compWin=compWin+1
        if compchoose==1:
            print ("uwin")
            uWin=uWin+1
        if compchoose==2:
            print ("drw")
            continue
    if compWin==2:
         print("copwins the war")
         break
    if uWin==2:
         print("u win the war")
         break
            

#5.37
sum=0
for i in range(2,626):
  sum=sum+(1/((i-1)**0.5+(i)**0.5))
print(sum) 


#5.38
import time
noOfSeconds=eval(input("seconds"))
i=0
for i in range(noOfSeconds,0,-1):
    print(i," seconds left")
    time.sleep(i) 

#5.39
saleOf5000,saleOf10000,saleOfmorethan10000=0,0,0
import random
salary=5000
while salary<=30000:
 r=random.randint(1,3) 
 if r==1: #sales<=5000:
  commission=8/100
  saleOf5000+=1
  salary=salary+commission*salary
 elif r==2: #sales<=10000:
  commission=10/100
  salary=salary+commission*salary
  saleOf10000+=1
 elif r==3: #sales>10000:
  commission=12/100
  salary=salary+commission*salary
  saleOfmorethan10000+=1
print("below 5000 ",saleOf5000,"b/n 5000 n 10000",saleOf10000,"above 100000",saleOfmorethan10000)
print("salary", salary) 
 
 
#5.40
import random
heads,tails=0,0
for i in range(1,1000001):
    g=random.randint(1,2)
    if g==1:
        heads=heads+1
    elif g==2:
         tails=tails+1

print(heads, " heads and", tails," tails") 


#5.41
max=eval(input("number"))
count=1
num=-100000
while num!=0:
    num=eval(input("number"))
    if num>max:
        max=num
        count=1
    elif num==max:
        count=count+1
    elif num<max:
        continue
print(max, end=" ")
print("appeared ", count," times")  

#5.42
import random
Area1,Area2,Area3,Area4=0,0,0,0
for i in range (1,1000001):
    x=random.random()*2-1  
    y=random.random()*2-1
    if (-1<=x<=0) and (-1<=y<=1):
       Area1+=1
    elif (0<=x<=1) and (0<=y<=1) and y<-x+1:       
       Area2+=1 
    elif (0<=x<=1) and (0<=y<=1) and y>-x+1:       
       Area3+=1   
    elif (0<=x<=1) and (-1<=y<=0):       
       Area4+=1  
   
prob1=Area1/1000000
prob3=Area3/1000000 
totprob=prob1+prob3
print (format(totprob,".5f"))  

#5.43
count=0
for i in range(1,8):
    for j in range(1,i):
        print(j,i)
        count+=1
print(count)  

#5.44 decimal to binary
num=eval(input("number"))
binnum=""
while num!=0:
    rem=num%2
    binnum=str(rem)+binnum
    num=num//2
print(binnum)


#5.45 decimal to hex
num=eval(input("number"))
hexnum=""
while num!=0:
    rem=num%16
    if 0<=rem<=9:
     addthis=chr(rem+ord("0"))
    else:
     addthis=chr(rem-10+ord("A"))   
    hexnum=addthis+hexnum
    num=num//16
print(hexnum)



#5.46
sum,sum2=0,0
for i in range(1,11):
    num=eval(input("number?"))
    sum=sum+num
    sum2=sum2+num**2

average=sum/i
stdDev=((sum2-(sum)**2/i)/(i-1))**0.5
print(format(average,".2f"))
print(format(stdDev,".2f"))


#5.47
import turtle
import random
turtle.penup()
turtle.goto(-60,50)
turtle.pendown()
turtle.forward(120)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(100)
turtle.penup()

for i in range(1,11):
    x=random.randint(-59,59)
    y=random.randint(-49,49)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("purple")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    
    
    
#5.48
import turtle
turtle.goto(0,0)
for r in range(50,160,10):
    turtle.penup()
    turtle.goto(0,-r)
    turtle.pendown()
    turtle.circle(r)
    
turtle.done() 


#5.49 
import turtle
turtle.penup()
turtle.goto(20,20)
turtle.pendown()
turtle.write("multiplication table")
turtle.penup()
turtle.goto(0,0)
x,y=0,0
turtle.pendown()
for i in range(1,11):
    x=0
    #turtle.write(i)
    for j in range(1,10):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.write(i*j)
        x+=30
    y=y-30
turtle.done()

#5.50
import turtle
turtle.penup()
turtle.goto(0,0)
x,y=0,0 
for i in range (1,11):
 for j in range (1,i):
   turtle.penup()
   turtle.goto(x,y)
   turtle.pendown()
   turtle.write(j)
   x=x+10
 y=y-10
 x=0  
turtle.done() 

#5.51
import turtle
x,y=0,0
for i in range (0,19):
 turtle.penup()
 turtle.goto(x,y)
 turtle.pendown() 
 turtle.forward(180)
 y=y-10
x,y=0,0
turtle.right(90)
for h in range (0,19):
 turtle.penup()
 turtle.goto(x,y)
 turtle.pendown() 
 turtle.forward(180)
 x=x+10 
turtle.done()

#5.52 error
import turtle
import math
x=0
turtle.penup()
for x in range(-175, 176):
  turtle.pendown()  
  turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
turtle.done()  
                       