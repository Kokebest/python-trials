# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 06:08:40 2021

@author: kokeb
"""

#7.1
class Rectangle():
    def __init__(self, width=1,height=1):
        self.width=width
        self.height=height
    def getArea(self):
         return self.width*self.height
    def getPerimeter(self):
         return 2*(self.width+self.height)
     
def main():
 r1=Rectangle(4,40)
 r2=Rectangle(3.5,35.7)
 print("rect 1 with width and height", r1.width,"and",r1.height,"has area",r1.getArea(),"and perimeter",r1.getPerimeter())
 print("rect 2 with width and height", r2.width,"and",r2.height,"has area",r2.getArea(),"and perimeter",r2.getPerimeter())        
 
main() 


#7.2
class Stock():
    def __init__(self,name,symbol, previousClosingPrice, currentPrice):
        self.__name=name
        self.__symbol=symbol
        self.__previousClosingPrice=previousClosingPrice
        self.__currentPrice=currentPrice
    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    def getCurrentPrice(self):
        return self.__currentPrice
    def getChangePercent(self):
        return (self.__currentPrice-self.__previousClosingPrice)*100/(self.__previousClosingPrice)
    
    
def main():
 stock1=Stock("Intel Corporation", "INTC", 20.5,20.35) 
 print("Percentage diff is",stock1.getChangePercent())

main()

#7.3
class Account():
    def __init__(self,id=0,balance=100,annualInterestRate=0):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
    def getId(self):
        return self.__id
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/1200
    def getMonthlyInterest(self):
        return self.__balance*self.__annualInterestRate/1200
    def withdraw(self,withdraw):
        self.__balance=self.__balance-withdraw
        return self.__balance
    def deposit(self,deposit):
        self.__balance=self.__balance+deposit
        return self.__balance
    def getBalance(self):
        return self.__balance

def main():
 account1=Account("1122",20000,4.5)
 account1.withdraw(2500)
 account1.deposit(3000) 
 print("the balance of account",account1.getId(),"is",account1.getBalance(),"with monthly Interest",account1.getMonthlyInterest())
main()   


#7.4
SLOW,MEDIUM,FAST=1,2,3
class Fan():
    def __init__(self, speed=SLOW,on=False,radius=5,color="blue"):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
    def getSpeed(self):
        return self.__speed
    def getOn(self):
        return self.__on    
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
def main ():
   fan1=Fan(FAST,True,10,"Yellow")
   fan2=Fan(MEDIUM,False,5,"Blue")
   print("the first fan has a speed of",fan1.getSpeed()," is ",fan1.getColor()," has radius of ",fan1.getRadius(),"and it is on")
   print("the first fan has a speed of ",fan2.getSpeed()," is ",fan2.getColor()," has radius of ",fan2.getRadius(),"and it is off")  
main() 

#7.5
import math
class RegularPolygon():
    def __init__(self,n=3,side=1,x=0,y=0):
     self.__n=n
     self.__side=side
     self.__x=x
     self.__y=y
    def getn(self):
        return self.__n
    def getSide(self):
        return self.__side
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getPerimeter(self):
        return self.__n*self.__side
    def getArea(self):
        return (self.__n*(self.__side)**2)/(4*math.tan(math.pi/self.__n)) 
def main():
    polygon1 = RegularPolygon(n=6, side=4,x=0,y=0) 
    polygon2 = RegularPolygon(n=10, side=4, x=5.6, y=7.8)
    print ("polygon1 has area of ",format(polygon1.getArea(),".2f"),"and perimeter of ", polygon1.getPerimeter())
    print ("polygon2 has area of ",format(polygon2.getArea(),".2f"),"and perimeter of ", polygon2.getPerimeter()) 
main()

#7.6
class QuadraticEquation():
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c        
    def getDiscriminant(self):
        return ((self.__b)**2-4*self.__a*self.__c)
    def getroot1(self):
        if ((self.__b)**2-4*self.__a*self.__c)>0:
            root1=(-self.__b+((self.__b)**2-4*self.__a*self.__c)**0.5)/(2*self.__a)
        elif ((self.__b)**2-4*self.__a*self.__c)==0:
            root1=(-self.__b+((self.__b)**2-4*self.__a*self.__c)**0.5)/(2*self.__a)
        else:
            return ("no root")
        return root1 
    def getroot2(self):
        if ((self.__b)**2-4*self.__a*self.__c)>0:
            root2= (-self.__b-((self.__b)**2-4*self.__a*self.__c)**0.5)/(2*self.__a)
            return root2
    
def Input():
  a,b,c=eval(input("coefficients?"))
  q1= QuadraticEquation(a,b,c)
  print("roots are",q1.getroot1(),"and",q1.getroot2())
Input()
  
#7.7
class LinearEquation():
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c 
    def getd(self):
        return self.__d
    def gete(self):
        return self.__e
    def getf(self):
        return self.__f
    def isSolvable(self):
        if self.__a*self.__d - self.__b*self.__c==0:
            return False
        else:
            return True
    def getx(self):
     x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d - self.__b*self.__c)
     return x
    def gety(self):
     y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d - self.__b*self.__c)
     return y
def test1():
    a,b,c,d,e,f=eval(input("coeff?"))
    x1=LinearEquation(a,b,c,d,e,f)
    if x1.isSolvable()==True:
      print("x=",x1.getx()," y=",x1.gety())
    else:
        print ("unsolvable")

test1()

#7.8
import time
class stopWatch():
 def __init__(self,startTime,endTime):
     self.__startTime=time.time()
     self.__endTime=endTime
     
 def getStarttime(self):
  return self.__startTime    
 def getEndtime(self):
  return self.__endTime
 def start(self):
   self.__startTime=time.time()
 def stop(self):
   self.__endTime=time.time()
 def getElapsedTime(self):
    return self.__endTime-self.__startTime


def test():
    sum=0
    t1=stopWatch(0,0)
    t1.start()
    for t in range(0,10000):
      sum=sum+t
    t1.stop()
    print(t1.getElapsedTime())
    print(sum)    
test()        
   
#7.9
class LinearEquation():
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c 
    def getd(self):
        return self.__d
    def gete(self):
        return self.__e
    def getf(self):
        return self.__f
    def getx(self):
     self.x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d - self.__b*self.__c)
     return self.x
    def gety(self):
     self.y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d - self.__b*self.__c)
     return self.y

def intersectingPoint():
 x1,y1,x2,y2=eval(input("first line?"))  
 x3,y3,x4,y4=eval(input("second line?"))
 m1=(y2-y1)/(x2-x1)
 m2=(y4-y3)/(x4-x3)
 b1=y1-m1*x1
 b2=y3-m2*x3
 lines=LinearEquation(-m1,1,-m2,1,b1,b2)
 print("intersecting point is",lines.getx(),",",lines.gety())
intersectingPoint()


#7.10
import time
class Time():
  def __init__(self, currentHour, currentMinute, currentSecond):
    self.__Hour=currentHour
    self.__Minute=currentMinute
    self.__Second=currentSecond
  def getHour(self):
      return self.__Hour
  def getMinute(self):
      return self.__Minute
  def getSecond(self):
      return self.__Second
  def getCurrentTime(self):
      return (self.__Hour," : ",self.__Minute," : ",self.__Second)
  def setTime(self,elapsedTime):
      allSecond2 = int(elapsedTime)
      currentSecond2 = allSecond2 % 60
      allMinute2 = allSecond2 // 60
      currentMinute2 = allMinute2 % 60
      allHour2 = allMinute2 // 60
      currentHour2 = allHour2 % 24
      return (currentHour2," : " ,currentMinute2, " : " ,currentSecond2)

def main():
 currentTime = time.time()
 allSecond = int(currentTime)
 currentSecond = allSecond % 60
 allMinute = allSecond // 60
 currentMinute = allMinute % 60
 allHour = allMinute // 60
 currentHour = allHour % 24
 t1=Time(currentHour,currentMinute,currentSecond)
 print(t1.getCurrentTime())
 elapsedTime=eval(input("elapsed time?"))
 t2=Time(currentHour,currentMinute,currentSecond)
 print(t2.setTime(elapsedTime))
main()






















   