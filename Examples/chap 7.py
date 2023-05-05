# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:28:25 2021

@author: kokeb
"""
import math
class Circle:
    def __init__(self,radius=1):
        self.radius=radius
    def everythingElse(self):
        area=math.pi*self.radius**2
        perimeter=2*math.pi*self.radius
        return area,perimeter

import Circle
def main():
    c1=Circle()
    print(c1.everythingElse())
    c2=Circle(25)
    print(c2.everythingElse())
    c3=Circle(125)
    print(c3.everythingElse())
main()   

class A:
 def __init__(self, i):
  self.i = i
def main():
 a = A(3)
 print(a.i)
main()


class Count:
 def __init__(self, count = 0):
  self.count = count
def main():
 c = Count()
 times = 0
 for i in range(100):
  increment(c, times)
 print("count is", c.count)
 print("times is", times)
def increment(c, times):
 c.count += 1
 times += 1
main()


class Count:
 def __init__(self, count = 0):
  self.count = count
def main():
 c = Count()
 n = 1
 m(c, n)
 print("count is", c.count)
 print("n is", n)
def m(c, n):
 c = Count(5)
 n = 3
main()

class A:
 def __init__(self, i):
  self.__i = i
def main():
 a = A(5)
 print(a.__i)
main()


def main():
 a = A()
 a.print()
class A:
 def __init__(self, newS = "Welcome"):
  self.__s = newS
 def print(self):
  print(self.__s)

main()

class A:
 def __init__(self, on):
  self.__on = not on
def main():
 a = A(False)
 print(a.on)
main() 