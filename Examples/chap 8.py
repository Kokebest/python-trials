# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:15:25 2021

@author: kokeb
"""

"green">"arenguade"
f="hujykgsn"
for ch in f:
    print(ch)
    
s1 = "Welcome to Python"
s2 = s1
s3 = "Welcome to Python"
s4 = "to"  


s1 == s2
s2.count('o')
id(s1) == id(s2)
id(s1) == id(s3)
s1 <= s4
s2 >= s4
s1 != s4
s1.upper()
s1.find(s4)
s1[4]
s1[4 : 8]
4* s4
len(s1)
max(s1)
min(s1)
s1[-4]
s1.lower()
s1.rfind('o')
s1.startswith("o")
s1.endswith("o")
s1.isalpha()
s1 + s1




s1 = "programming 101"
s2 = "programming is fun"
s3 = s1 + s2
s3 = s1 - s2
s1 == s2
s1 >= s2
i = len(s1)
c = s1[0]
t = s1[ : 5]
t = s1[5 : ]





s1 = "Welcome to Python"
s2 = s1.replace("o","abc")
print(s1)
print(s2)


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
   return str(self.__numerator + "/"+ self.__denominator)

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

