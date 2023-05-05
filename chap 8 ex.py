# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 05:14:30 2021

@author: kokeb
"""

#8.1
SSN=input("enter social security number")
if len(SSN)==9:
    print ("valid")
else:
    print ("invalid")
    
#8.2
s1=input("smaller string")
s2=input("bigger string")
if s2.find(s1) !=-1:
    print("yes")
if s2.find(s1) ==-1:
    print("no") 
    
#8.3
password=input("password?")
if len(password)>=8:
  if password.isalnum():
      count=0
      for t in range (0,len(password)):
        l=password[t]
        if str(0)<=l<=str(9):
         count+=1
      if count>=2:
          print("valid")
      else:
          print("invalid")
  else:
          print("invalid")
else:
          print("invalid")


#8.4
def count(s,ch):
 count=0
 for g in range(0,len(s)):
     h=s[g]
     if h==ch:
       count+=1
 return count

def main():
 s1=input("string")
 ch1=input("character")
 print(count(s1,ch1))

main() 



#8.5
def countString(s1,s2):
 y=s1.count(s2)
 return y

def main():
 s1=input("string1")
 s2=input("string2")
 print(countString(s1,s2))

main()

#8.6
def countLetters(s): 
 count=0
 for u in range (0,len(s)):
    j=s[u]
    if "A"<=j<="Z" or "a"<=j<="z":
      count+=1
      
 return count       

def main():
 s1=input("string?")
 print(countLetters(s1))

main()


#8.7
def getNumber(uppercaseLetter):
   if uppercaseLetter == "A" or uppercaseLetter=="B" or uppercaseLetter=="C":
       return 2
   elif uppercaseLetter == "D" or uppercaseLetter=="E" or uppercaseLetter== "F":
       return 3
   elif uppercaseLetter == "G" or uppercaseLetter == "H" or uppercaseLetter == "I":
       return 4
   elif uppercaseLetter == "J" or uppercaseLetter =="K" or uppercaseLetter == "L":
       return 5
   elif uppercaseLetter == "M" or uppercaseLetter == "N" or uppercaseLetter =="O":
       return 6
   elif uppercaseLetter == "P" or uppercaseLetter =="Q" or uppercaseLetter =="R" or uppercaseLetter =="S":
       return 7
   elif uppercaseLetter == "T" or uppercaseLetter =="U" or uppercaseLetter =="V":
       return 8
   elif uppercaseLetter == "W" or uppercaseLetter == "X" or uppercaseLetter == "Y" or uppercaseLetter == "Z":
       return 9

def upperCase(st1):
 return st1.upper()

def main():
   s1=input("number?") 
   f=""
   for i in range (0,len(s1)):
     r=s1[i]
     if "A"<=r<="Z" or "a"<=r<="z":
         f=f+str(getNumber(upperCase(r)))
     if "0"<=r<="9":
         f=f+r    
         
   print (f) 
    

main() 


#8.8
def binaryToDecimal(binaryString):
   q=0 
   for i in range (0,len(binaryString)): 
     q=q*2+(int(binaryString[i]))
   return(q)
def main():
    d=input("binary number?")
    print(binaryToDecimal(d))
main()


#8.9
def binaryToDecimal(binaryString):
   q=0 
   for i in range (0,len(binaryString)): 
     q=q*2+(int(binaryString[i]))
   return q

def DecimalToHex(Value):
    g=""
    while Value !=0:
      rem=Value%16
      Value=Value//16
      g=str(rem)+g
    return(g)  

def main():
    num=(input("binarynum"))
    print(DecimalToHex(binaryToDecimal(num)))
    
main()  

#8.10
def decimalToBinary(value):  
    m=""
    while value != 0:
      rem=value%2
      value=value//2
      m=str(rem)+m
    return(m)  

def main1():
    num1=eval(input("decimal"))
    print(decimalToBinary(num1))
    
main1() 

#8.11
def reverse(s):     
    rev=""
    for i in range (0,len(s)):
        o=s[i]
        rev=o+rev
    return rev
def main():
    f=input("string?")
    print(reverse(f))
main()    


#8.15
def checkSum(num):
    checkSum=0
    for i in range (9,0,-1):
     d1=num%10
     num=num//10
     checkSum+=d1*i
    checkSum=checkSum%11
    return checkSum

def main():
    nineDigitNoStr=(input("the fist nine digits?"))
    nineDigitNo=int(nineDigitNoStr)
    if checkSum(nineDigitNo) == 10:
        print(str(nineDigitNo).rjust(9,"0"),"X")
    else:
        print(str(nineDigitNo),str(checkSum(nineDigitNo)))
main()

#8.16
def checkSum(num):
    checkSumOdd,checkSumEven=0,0
    count=0
    for i in range (12,0,-1):
     d1=num%10
     num=num//10
     count+=1
     if count%2==0:
      checkSumEven+=d1
     elif count%2!=0:
      checkSumEven+=d1*3
    checkSum=10-((checkSumOdd+checkSumEven)%10)
    return checkSum

def main():
    twelveDigitNoStr=eval(input("the fist twelve digits?"))
    twelveDigitNo = int(twelveDigitNoStr)
    if checkSum(twelveDigitNo) == 10:
        print(str(twelveDigitNo).rjust(12,"0"),"0")
    else:
        print(str(twelveDigitNo).rjust(12,"0"),str(checkSum(twelveDigitNo)))
main()


#8.17
class Point():
  def __init__(self,x=0,y=0):
      self.__x=x
      self.__y=y

  def __getitem__(self, index):
      if index==0:
          return self.__x
      else:
          return self.__y
  def distance(self,secondPoint):
      return ((self.__x-secondPoint[0])**2+(self.__y-secondPoint[1])**2)**0.5
  def isNearby(self,secondPoint):
      if ((self.__x-secondPoint[0])**2+(self.__y-secondPoint[1])**2)**0.5<=5:
          return "near by"
  def __str__(self):
      return (self.__x,self.__y)

def main():
    x1,y1,x2,y2=eval(input("the two points?"))
    point1=Point(x1,y1)
    point2=Point(x2,y2)
    print(point1.distance(point2))
main()




#8.18
import math
class Circle2D():
 def __init__(self,x=0,y=0,radius=0):
     self.__x=x
     self.__y=y
     self.__radius=radius
 def getX(self):
     return self.__x
 def getY(self):
     return self.__y
 def getArea(self):
     return math.pi*(self.__radius)**2
 def getPerimeter(self):
     return 2*math.pi*(self.__radius)
 def containsPoint(self,a,b):
     if self.__x-self.__radius<=a<=self.__x+self.__radius and self.__y-self.__radius<=b<=self.__y+self.__radius:
         return True
     else:
         return False
 def contains(self,circle2D):
     if self.__radius>circle2D.__radius and self.__x<=circle2D.__x<=self.__x and self.__y<=circle2D.__y<=self.__y:
         return True
     else:
         return False
 def overlaps(self,circle2D):
     if self.__radius+circle2D.__radius>((self.__x-circle2D.__x)**2+(self.__y-circle2D.__y)**2)**0.5:
         return True
     else:
         return False
def main():
    x1,y1,radius1=eval(input("point 1 and radius"))
    x2,y2,radius2=eval(input("point 2 and radius"))
    c1=Circle2D(x1,y1,radius1)
    c2=Circle2D(x2,y2,radius2)
    print("circle 1 has area ",c1.getArea(),"and perimeter",c1.getPerimeter())
    print("circle 2 has area ",c2.getArea(), "and perimeter",c2.getPerimeter())
    if c1.containsPoint(c2.getX(),c2.getY())==True:
        print("it contains")
    elif c1.containsPoint(c2.getX(),c2.getY())==False:
        print("it does not contain")
    print("c1 contains c2? ", c1.contains(c2))
    print("c1 overlaps c2? ", c1.overlaps(c2))
main()




#8.19
class Rectangle2D():
    def __init__(self,x=0,y=0,width=0,height=0):
        self.__x=x
        self.__y=y
        self.__width=width
        self.__height=height
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getArea(self):
        return self.__height*self.__width
    def getPerimeter(self):
        return (self.__height+self.__width)*2
    def containsPoint(self,a,b):
        if (self.__x-(self.__width/2))<=a<=(self.__x+(self.__width/2)) and (self.__y-(self.__height/2))<=b<=(self.__y+self.__height/2):
            return True
        else:
            return False
    def contains(self,rectangle):
        if self.__x+self.__width/2>rectangle.__x+rectangle.__width/2 and self.__y+self.__height/2>rectangle.__y+rectangle.__height/2 and \
          self.__x-self.__width/2<rectangle.__x<self.__x+self.__width/2 and self.__y-self.__height/2<rectangle.__y<self.__y+self.__height/2:
           return True
        else:
            return False
    def overlaps(self,rectangle):
        if self.__width/2+rectangle.__width/2>((self.__x-rectangle.__x)**2+(self.__y-rectangle.__y)**2)**0.5:
            return True
        else:
            return False
def main():
     x1,y1,width1,height1=eval(input("the first rectangle"))
     x2,y2,width2,height2=eval(input("the second rectangle"))
     r1=Rectangle2D(x1,y1,width1,height1)
     r2=Rectangle2D(x2,y2,width2,height2)
     print("area of rectangle 1 is ",r1.getArea(),"and perimeter",r1.getPerimeter())
     print("area of rectangle 2 is ", r2.getArea(), "and perimeter", r2.getPerimeter())
     print("does r1 contain r2 center?",r1.containsPoint(r2.getX(),r2.getY()))
     print("r1 contains r2",r1.contains(r2))
     print("r1 overlaps with r2",r1.overlaps(r2))
main()


#8.20
class Rational:
 def __init__(self, numerator=1, denominator=0):
  divisor = gcd(numerator, denominator)
  self.__numerator = (1 if denominator > 0 else -1)*int(numerator / divisor)
  self.__denominator = int(abs(denominator) / divisor)
 def __add__(self, secondRational):
  n= self.__numerator * secondRational[1] + self.__denominator * secondRational[0]
  d = self.__denominator * secondRational[1]
  return Rational(n, d)
 def __sub__(self, secondRational):
  n = self.__numerator * secondRational[1] - self.__denominator * secondRational[0]
  d = self.__denominator * secondRational[1]
  return Rational(n, d)
 def __mul__(self, secondRational):
  n = self.__numerator * secondRational[0]
  d = self.__denominator * secondRational[1]
  return Rational(n, d)

 def __truediv__(self, secondRational):
  n = self.__numerator * secondRational[1]
  d = self.__denominator * secondRational[0]
  return Rational(n, d)

 def __float__(self):
  return self.__numerator / self.__denominator

 def __int__(self):
  return int(self.__float__())

 def __str__(self):
  if self.__denominator == 1:
   return str(self.__numerator)
  else:
   return str(self.__numerator) + "/"+ str(self.__denominator)

 def __lt__(self, secondRational):
  return self.__cmp__(secondRational) < 0
 def __le__(self, secondRational):
  return self.__cmp__(secondRational) <= 0
 def __gt__(self, secondRational):
  return self.__cmp__(secondRational) > 0
 def __ge__(self, secondRational):
  return self.__cmp__(secondRational) >= 0

 def __cmp__(self, secondRational):
  temp = self.__sub__(secondRational)
  if temp[0] > 0:
   return 1
  elif temp[0] < 0:
   return -1
  else:
   return 0
 def __getitem__(self, index):
  if index == 0:
   return self.__numerator
  else:
   return self.__denominator

def gcd(n, d):
 n1 = abs(n)
 n2 = abs(d)
 gcd = 1
 k = 1
 while k <= n1 and k <= n2:
  if n1 % k == 0 and n2 % k == 0:
   gcd = k
  k += 1
 return gcd

def main():
 sum=Rational(0,1)
 for i in range(1,10):
   r1=Rational(i,i+1)
   sum=sum.__add__(r1)
 print(sum.__float__())
main()




#8.21
class Complex():
 def __init__(self,a=0,b=0):
  self.realPart=a
  self.imaginaryPart=b
 def __getitem__(self,index):
     if index == 0:
         return self.realPart
     else:
         return self.imaginaryPart
 def __add__(self,c2):
  return (str(self.realPart+c2[0])+"+"+str(self.imaginaryPart+c2[1])+"i")
 def __subtract__(self,c2):
  return (str(self.realPart-c2[0])+"+"+str(self.imaginaryPart-c2[1])+"i")
 def __multiply__(self,c2):
  return (str(self.realPart*c2[0]-self.imaginaryPart*c2[1])+"+"+str(self.imaginaryPart*c2[0]+self.realPart*c2[1])+"i")
 def __divide__(self,c2):
  return (str((self.realPart*c2[0]+self.imaginaryPart*c2[1])/((c2[0])**2+(c2[1])**2))+"+"+str((self.imaginaryPart*c2[0]-self.realPart*c2[1])/((c2[0])**2+(c2[1])**2))+"i")
 def __absolute__(self):
  return (self.realPart**2+self.imaginaryPart**2)**0.5

def main():
 x1,y1=eval(input("point1?"))
 x2,y2=eval(input("point2?"))
 c1=Complex(x1,y1)
 c2=Complex(x2,y2)
 print("sum",c1.__add__(c2))
 print("subtract", c1.__subtract__(c2))
 print("multiply", c1.__multiply__(c2))
 print("divide", c1.__divide__(c2))
 print("absolute", c1.__absolute__())

main()