# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:05:07 2021

@author: kokeb
"""

#6.1
def getPentagonalNumber(n):
    pentnumber=n*(3*n-1)/2
    return pentnumber

count=0
i=1
while i <=100:
 print(getPentagonalNumber(i), end="\t")
 i=i+1
 count+=1
 if count%10==0:
    print()


#6.2
def sumDigits(n):
   sum=0 
   number=eval(input("number?"))
   while number!=0:
      d1=number%10
      number=number//10
      sum=sum+d1
   return sum 
print (sumDigits(n))   
      


#6.3
def reverse(num):
    sum=0
    while num!=0:
      d1=num%10
      num=num//10
      sum=str(sum)+str(d1)
    return int(sum) 

def isPalindrome(m):
    if m==reverse(m):
        return True
    else:
        return False
    
number=eval(input("number?"))
reverse(number)
isPalindrome(number) 



#6.4
number=eval(input("number?"))
def reverse(num):
    sum=0
    while num!=0:
      d1=num%10
      num=num//10
      sum=str(sum)+str(d1)
    return int(sum)   
print(reverse(number))    


#6.5
n1,n2,n3=eval(input("numbers"))

def displaySortedNumbers(num1,num2,num3):
    if num1<num2<num3:
        return num1,num2,num3
    elif num1<num3<num2:
        return num1,num3,num2
    elif num2<num3<num1:
        return num2,num3,num1    
    elif num2<num1<num3:
        return num2,num1,num3
    elif num3<num1<num2:
        return num3,num1,num2
    elif num3<num2<num1:
        return num3,num2,num1

print(displaySortedNumbers(n1,n2,n3)) 

#6.6
d=eval(input("rows?"))
def displayPattern(n): 
    for i in range (1,n+1):
        for j in range(n+1,0,-1):
            if j>i:
             print(" ",end=" ")
            else:
             print(j,end=" ")
        print() 

displayPattern(d)        
    
    
#6.7
investmentAmount=eval(input("investmentAmount"))
AnnualInterestRate=eval(input("annual interest"))
monthlyInterestRate=AnnualInterestRate/1200
def futureInvestmentValue(investmentAmount, monthlyInterestRate, y): 
   for i in range(1,y+1):
    futureInvestment=investmentAmount*(1+monthlyInterestRate)**(i*12)
    print (i,"\t",format(futureInvestment,".2f"))

futureInvestmentValue(investmentAmount, monthlyInterestRate,30)


#6.8
def celsiusToFahrenheit(celsius):
  fahrenheit = (9 / 5) * celsius + 32
  return fahrenheit 
    
def fahrenheitToCelsius(fahrenheit2):
  celsius2 = (5 / 9) * (fahrenheit2 - 32)
  return celsius2

v=120    
for u in range(40,30,-1): 
    
   while v >20:
      print (u,"\t",format(celsiusToFahrenheit(u),".2f"), end="\t | \t")
      print (v, "\t",format(fahrenheitToCelsius(v),".2f")," \t \t")
      v=v-10
      break
print()


#6.9
def footToMeter(foot):
  meter = 0.305 * foot
  return meter 
    
def meterToFoot(meter):
  foot = meter / 0.305
  return foot

v=20    
for u in range(1,11): 
    
   while v <=74:
      print (u,"\t",format(footToMeter(u),".2f"), end="\t | \t")
      print (v, "\t",format(meterToFoot(v),".2f")," \t \t")
      v=v+6
      break
print()

#6.10
def isPrime(number):
    primecount=0
    for i in range (2,number):
        isPrime=True
        for j in range(2,i):
            if i%j==0:
             isPrime=False
             break
        if isPrime==True:
            print (i, end=" ")
            primecount+=1
    return primecount 

print(isPrime(10000)) 


#6.11
def computeCommission(salesAmount):
   commission=0.12*salesAmount 
   return commission

for i in range(10000,105000,5000):
    print(i,"\t",computeCommission(i))
    
#6.12
def printChars(ch1, ch2, numberPerLine):
    count=0
    for i in range (ch1,ch2+1):
        print(chr(i),end=" ")
        count+=1
        if count%numberPerLine==0:
            print()
            
printChars(ord("1"),ord("Z"),10) 

#6.13
def sumOfSeries(m):
 sum1=0
 for i in range (1,m):
  sum1=sum1+(i/(i+1))
  print(i, format(sum1,".2f"))

sumOfSeries(20)      
    
     
#6.14 error
def pinum(s):
 pinum=0  
 for i in range (0,102):
   pinum=pinum+4*((-1)**(i+1)/(2*i-1))    
   return pinum

for j in range(1,1000,100):
   print (j, "\t",pinum(j)) 


#6.15
def computeTax(status,income):
  if status==0:
      if income<=8350:
          tax=0.1*income
      elif income<=33950:
          tax=0.1*8350+0.15*(income-8350)
      elif income<=82250:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(income-33950)
      elif income<=171550:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(82250-33950)+0.28(income-82250)
      elif income<=372950:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(82250-33950)+0.28(171550-82250)+0.33(income-171550)    
      else:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(82250-33950)+0.28(171550-82250)+0.33(372950-171550)+0.35(income-372950)
  
  if status==1:
      if income<=16700:
          tax=0.1*income
      elif income<=67900:
          tax=0.1*16700+0.15*(income-16700)
      elif income<=137050:
          tax=0.1*16700+0.15*(67900-16700)+0.25*(income-67900)
      elif income<=208850:
          tax=0.1*16700+0.15*(67900-16700)+0.25*(137050-67900)+0.28(income-137050)
      elif income<=372950:
          tax=0.1*16700+0.15*(67900-16700)+0.25*(137050-67900)+0.28(208850-137050)+0.33(income-208850)    
      else:
          tax=0.1*16700+0.15*(67900-16700)+0.25*(137050-67900)+0.28(208850-137050)+0.33(372950-171550)+0.35(income-372950)

  if status==2:
      if income<=8350:
          tax=0.1*income
      elif income<=33950:
          tax=0.1*8350+0.15*(income-8350)
      elif income<=68525:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(income-33950)
      elif income<=104425:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(68525-33950)+0.28(income-68525)
      elif income<=186475:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(68525-33950)+0.28(104425-68525)+0.33(income-104425)    
      else:
          tax=0.1*8350+0.15*(33950-8350)+0.25*(68525-33950)+0.28(104425-68525)+0.33(186475-104425)+0.35(income-186475)

  if status==3:
      if income<=11950:
          tax=0.1*income
      elif income<=45500:
          tax=0.1*11950+0.15*(income-11950)
      elif income<=117450:
          tax=0.1*11950+0.15*(45500-11950)+0.25*(income-45500)
      elif income<=190220:
          tax=0.1*11950+0.15*(45500-11950)+0.25*(117450-45500)+0.28(income-117450)
      elif income<=372950:
          tax=0.1*11950+0.15*(45500-11950)+0.25*(117450-45500)+0.28(190220-117450)+0.33(income-190220)    
      else:
          tax=0.1*11950+0.15*(45500-11950)+0.25*(117450-45500)+0.28(190220-117450)+0.33(372950-190220)+0.35(income-372950)          
  return tax


   
for g in range(50000,60050,50):
    print(g,end="\t")
    for h in range (0,4):
      print(format(computeTax(h,g),".1f"),end="\t")
    print()  
    
    
    
#6.16
def numberOfDaysInAYear(year):
   if (year%4==0 and year%100!=0 or year%400==0):
       return 366
   else:
       return 365
   
for n in range(2010,2021):
 print(n,"\t",numberOfDaysInAYear(n)) 


#6.17
def isValid(side1, side2, side3):
 if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
     return True
 else:
     return False
    
def area(side1, side2, side3): 
     s = (side1 + side2 + side3) / 2 
     area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
     return area
    
     
n1,n2,n3=eval(input("sides?"))
if isValid(n1, n2, n3)==True:
   print (area(n1,n2,n3))
   
elif isValid(n1, n2, n3) == False:
    print ("invalid") 
    
#6.18
def printMatrix(n):
  import random
  for i in range(1,n+1):
     for j in range (1,n+1):
          print(random.randint(0,1), end=" ")
     print() 
     
g=eval(input("size?"))
printMatrix(g) 


#6.19
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
 if (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0) >0:
     return True
def onTheSameLine(x0, y0, x1, y1, x2, y2):
 if (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0) ==0: 
     return True
def onTheLineSegment(x0, y0, x1, y1, x2, y2):
 if x0<x2<x1 and y0<y1<y2: 
     return True
    
    
x0, y0, x1, y1, x2, y2=eval(input("points?"))
if leftOfTheLine(x0, y0, x1, y1, x2, y2) == True:
 print("left")
if onTheSameLine(x0, y0, x1, y1, x2, y2):
 print("on same line")
if onTheSameLine(x0, y0, x1, y1, x2, y2):
 print("on line segment")


#6.20
def distance(x1, y1, x2, y2):
 distance=((x2-x1)**2+(y2-y1)**2)**0.5 
 return distance

n1, n2, n3, n4=eval(input("points"))
print(distance(n1,n2,n3,n4)) 


#6.21
def sqrt(n):
    lastGuess=1
    nextGuess=0
    diff=1
    while diff>0.0001:
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        diff=abs(lastGuess-nextGuess)
        lastGuess=nextGuess
    return nextGuess

q=eval(input("num"))
print(sqrt(q)) 


#6.22
year,month=eval(input("year,month"))
def currentTime(): 
 import time
 currentTime = time.time()
 totalsec=int(currentTime)
 currentsec=totalsec%60
 totalmin=totalsec//60
 currentmin=totalmin%60
 totalhour=totalmin//24
 currenthour=totalhour%24
 return (currenthour,":",currentmin,":",currentsec)

def currentdate(year,month):
    totalday=0
    for i in range(1800,year):
        if (year%4==0 and year%100!=0 or year%400==0):
          totalday+=366
        else:
          totalday+=365
          
    for i in range(1,month):
        totalday+=dayinyear(i)
    return totalday      
def dayinyear(month):
  if month== 1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12:          
      days=31  
  elif month== 4 or month==6 or month==9 or month==11:          
      days=30 
  elif month==2:
      if (year%4==0 and year%100!=0 or year%400==0):
          days=29
      else:
          days=28
  return days   

def datetoday(): 
    datetoday=3+currentdate(year,month)%7
    daytoday=0
    for i in range(1,month):
        daytoday+=dayinyear(i)
      
    if datetoday==1:
        return "mon"
    elif datetoday==2:
        return "tue"
    elif datetoday==3:
        return "wed"
    elif datetoday==4:
        return "thu"
    elif datetoday==5:
        return "fri"
    elif datetoday==6:
        return "sat"
    elif datetoday==7:
        return "sun"
    
print ("today is",datetoday(),",",month,",",year)
print("time",currentTime()) 



#6.23
def convertmilli(millis):
    totalsecs=millis//1000
    secs=totalsecs%60
    totalmins=totalsecs//60
    mins=totalmins%60
    hours=totalmins//60
    return hours,mins,secs
m=eval(input("no of millis"))
print(convertmilli(m)) 
  


#6.24error
def isPalindrome(num):
   num2=0
   while num!=0:
    d1=num%10
    num2=str(d1)+num2
    num=num//10
   if num==num2:
       return True
   else:
       return False
   
def isPrime():
  i=2
  isPrime=True
  count=0
  for count in range(1,101): 
   for d in range(2,i):
     if i%d==0:
       isPrime=False
       break
     i=i+1
     if isPrime==True: #and isPalindrome(i)==True:
       count+=1
       print(i, end=" ")
       if count==10:
           print()

isPrime()    

#6.25

#6.26
def Mersenneprime(n):
  for i in range (2,n+1):
      isPrime=True
      for j in range (2,i):
         if i%j==0:
             isPrime=False
             break
      if isPrime==True:
             print (i,"\t ", 2**i-1)
             
Mersenneprime(31)  

#6.27
def Twinprime(n):
   oldPrime=2
   for i in range (2,n+1):
      isPrime=True
      for j in range (2,i):
         if i%j==0:
             isPrime=False
             break
      if isPrime==True:
          newPrime=i 
          if newPrime-oldPrime==2:
           print (oldPrime,newPrime)
          oldPrime=newPrime 
             
Twinprime(1000) 


#6.28
def craps():
  import random
  roll1=random.randint(1,6)
  roll2=random.randint(1,6)
  if roll1+roll2==2 or roll1+roll2 == 3 or roll1+roll2 == 12:
        return ("u lose")
  elif roll1+roll2==7 or roll1+roll2 == 11:
        return ("u win") 
  elif roll1+roll2==4 or roll1+roll2 == 5 or roll1+roll2 == 6 or roll1+roll2==8 or roll1+roll2 == 9 or roll1+roll2 == 10:
        sum=roll1+roll2
        print ("point is ",roll1+roll2,"roll again") 
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        if roll1+roll2== sum:
         return ("win") 
        elif roll1+roll2==7:
         return ("lose")
        else:
         return("idk")   
     
craps()



#6.29
def moreThan10(num):
    sum=0
    while num!=0:
     d6=num%10
     sum=sum+d6
     num=num//10
    return sum
def getDigits(number):
   count=0 
   evenSum1,evenSum2,oddSum=0,0,0
   while number!=0:
       digit=number%10
       number=number//10
       count+=1
       if count%2==0:
           digit=digit*2
           if digit>=10:
             evenSum1=evenSum1+moreThan10(digit)
           else:
            evenSum2=evenSum2+digit  
           evenSum=evenSum1+evenSum2 
       else:
           oddSum+=digit
   realSum=evenSum+oddSum
   return realSum       
 
def isValid(num): 
   if getDigits(num)%10==0:
       return "Valid"
   else:
       return "Invalid"
   

number=eval(input("number?"))  
isValid(number) 




#6.30
def craps():
  import random
  roll1=random.randint(1,6)
  roll2=random.randint(1,6)
  if roll1+roll2==2 or roll1+roll2 == 3 or roll1+roll2 == 12:
        return ("u lose")
  elif roll1+roll2==7 or roll1+roll2 == 11:
        return ("u win") 
  elif roll1+roll2==4 or roll1+roll2 == 5 or roll1+roll2 == 6 or roll1+roll2==8 or roll1+roll2 == 9 or roll1+roll2 == 10:
        sum=roll1+roll2
        #print ("point is ",roll1+roll2,"roll again") 
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        if roll1+roll2== sum:
         return ("win") 
        elif roll1+roll2==7:
         return ("lose")
        else:
         return("idk")   
     
def count():
    count=0
    for r in range(1,10000):
        if craps()=="u win":
            count+=1
    return count  

count()      

#6.31 error
import time
def currentDate():
   totalSeconds=time.time()
   currentSecond=totalSeconds%60
   totalMinutes=totalSeconds//60
   currentMinute=totalMinutes%60
   totalHours=totalMinutes//60
   currentHour=totalHours%24
   '''totalDay=totalSeconds//60
   currentMinute=totalMinutes%60
   totalMinutes=totalSeconds//60
   currentMinute=totalMinutes%60'''
   
   print("current time is",currentHour,":",currentMinute,":",currentSecond)   
currentDate()


#6.32

#6.33
import math
def area(s):
    area=(5*s**2)/(4*math.tan(math.pi/5))
    return area

side=eval(input("side?"))
area(side)
       
    
    
#6.34
def area2(n, s): 
    area2=(n*s**2)/(4*math.tan(math.pi/n))
    return area2

side2=eval(input("side?"))
no=eval(input("number of side?"))
area2(no,side2)


#6.35

def RandomChar():
   import random 
   chr1=random.randint(ord("A"),ord("Z"))
   return chr(chr1)
   
def main():
 count=0   
 for g in range (1,10000):
     RandomChar()   
     if RandomChar()=="A":
       count+=1
 return count    

main()

#6.36
def RandomChar2():
   import random 
   chr1=random.randint(ord("A"),ord("Z"))
   return chr(chr1)
def RandomChar3():
   import random
   chr2=random.randint(ord("0"),ord("9"))
   return chr(chr2)

def main1():
   count=0
   for d in range (1,101):
       print (RandomChar2(), end="\t")
       count+=1
       if count%10==0:
           print()
   count2=0 
   print()       
   for e in range (1,101):
       print (RandomChar3(), end="\t")
       count2+=1
       if count2%10==0:
           print()
           
main1()



#6.37
def RandomChar4():
   import random 
   chr4=random.randint(ord("a"),ord("z"))
   return chr(chr4)

def turtle1():
 import turtle
 count3=0
 x,y=0,0
 for t in range (1,101):
     turtle.penup()
     turtle.goto(x,y)
     turtle.pendown()
     turtle.write(RandomChar4())
     x+=10
     count3+=1
     if count3%15==0:
         x=0
         y-=10 
 turtle.done()
 
turtle1() 

#6.38
def drawLine(x1, y1, x2, y2, color = "black", size = 1):
 import turtle          
 turtle.penup()
 turtle.goto(x1,y1)
 turtle.pendown()
 turtle.color(color)
 turtle.pensize(size)
 turtle.goto(x2,y2)
 turtle.done()

drawLine(0,0, 30, 30, color = "purple", size = 50) 

#6.39
def drawLine(x1, y1, x2, y2, color = "black", size = 1):
 import turtle          
 turtle.penup()
 turtle.goto(x1,y1)
 turtle.pendown()
 turtle.color(color)
 turtle.pensize(size)
 turtle.goto(x2,y2)
 turtle.penup()

def drawStar():
 import turtle   
 drawLine(0,0,100,0)
 turtle.right(30)
 drawLine(100,0,13.5,-50)
 turtle.right(30)
 drawLine(13.5,-50,45,45)
 drawLine(45,45,86.6,-50)
 drawLine(86.6,-50,0,0)
 turtle.done()
 
drawStar() 


#6.40 error
def drawRectangle(color = "black", x = 0, y = 0, width = 30, height = 30):
 import turtle
 turtle.begin_fill()          
 turtle.penup()
 turtle.goto(x=0-width/2,y=0+height/2)
 turtle.pendown()
 turtle.forward(30)
 turtle.right(90)
 turtle.forward(30)
 turtle.left(90)
 '''turtle.forward(30)
 turtle.left(90)
 turtle.forward(30)
 turtle.end_fill()
 turtle.done'''
 
'''def drawCircle(color = "black", x = 0, y = 0, radius = 50):
 import turtle
 turtle.begin_fill()          
 turtle.penup()
 turtle.goto(x=x,y=y-radius/2)
 turtle.pendown()
 turtle.circle(50)
 turtle.end_fill()
 turtle.done'''  
    
drawRectangle() 
drawCircle()  