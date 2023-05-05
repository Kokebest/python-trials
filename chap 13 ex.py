#13.1
import pickle
def main():
 f1=input("choose a file").strip()
 infile=open(f1,"r")
 word=input("to eliminate")
 outfile=open("test2.txt","w")
 lines=infile.readlines()
 for l in lines:
  if "morning" in l:
   l=l.replace(word,"")
  outfile.write(l)
 infile.close
 outfile.close
main()

#13.2
def main():
 f1=input("choose file").strip()
 infile=open(f1,"r")
 lines1=infile.readlines()
 words=0
 sentences=0
 characters=0
 for a in lines1:
  sentences+=1
  characters+=len(a)
  a2=a.split(" ")
  words+=len(a2)
 print(sentences,"sentences",words,"words and", characters,"characters")
 infile.close
main()


#13.3
def main():
 f1=input("choose file").strip()
 infile=open(f1,"r")
 lines2=infile.read()
 lines3=[]
 lines3 = lines2.split(" ")
 lines4=len(lines3)*[0]
 for b in range(0,len(lines3)):
  lines4[b]=int(lines3[b])
 print(lines4)
 noOfScore=len(lines4)
 sumOfScore=sum(lines4)
 avg=sumOfScore/noOfScore
 print("no of score",noOfScore)
 print("total score", sumOfScore)
 print("Average score", avg)
main()


#13.4
import random
import os.path
import sys
def main():
 f1=input("choose name")
 if os.path.isfile(f1):
  print("exsists")
  sys.exit()
 outfile=open(f1,"w")
 for c in range(1,101):
   d=random.randint(0,100)
   outfile.write(str(d))
   outfile.write(" ")
 outfile.close()
main()



#13.5
def main():
 f1=input("choose file")
 f2=input("choose new file")
 infile=open(f1,"r")
 outfile=open(f2,"w")
 lines5=infile.read()
 lines6=lines5.replace("fox","dog")
 outfile.write(lines6)
 infile.close()
 outfile.close()
main()


#13.6
def main():
 infile=open("President.txt","r")
 lines7=infile.read()
 lines8=[]
 lines8=lines7.split(" ")
 count1=len(lines8)
 print(count1," words.")
 infile.close()
main()




#13.10
class Rational:
 def __init__(self, numerator=1, denominator=1):
  divisor = gcd(numerator, denominator)
  self.__numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
  if denominator==0:
   raise RuntimeError("zero division")
  else:
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
 try:
  sum=Rational(0,1)
  for i in range(-1,10):
   r1=Rational(i,i+1)
   sum=sum.__add__(r1)
  print(sum.__float__())
 except RuntimeError:
  print("invalid denominator")
main()




#13.11
class GeometricObjects():
 def __init__(self, color, filled):
  self.color = color
  self.filled = filled

 def getColor(self):
  return self.color

 def setColor(self, color):
  self.color = color

 def isFilled(self):
  return self.filled

 def setFilled(self, filled):
  self.filled = filled

 def __str__(self):
  return "Color: " + self.color + "is filled:" + self.filled


class Triangle(GeometricObjects):
 def __init__(self, side1=1.0, side2=1.0, side3=1.0):
  if side1+side2<=side3 or side2+side1<=side3 or side2+side3<=side1:
   raise RuntimeError("invalid sides")
  else:
   self.side1 = side1
   self.side2 = side2
   self.side3 = side3


 def getSide1(self):
  return self.side1

 def getSide2(self):
  return self.side2

 def getSide3(self):
  return self.side3

 def getArea(self):
  s = (self.side1 + self.side2 + self.side3) / 2
  return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

 def getPerimeter(self):
  return (self.side1 + self.side2 + self.side3)

 def __str__(self):
  return "side1" + self.side1 + "side2" + self.side2 + "side3" + self.side3


def main():
 try:
  s1 = eval(input("first side"))
  s2 = eval(input("second side"))
  s3 = eval(input("third side"))
  color1 = input("color?")
  isfilled = eval(input("1 or 0 for filled"))
  tri1 = Triangle(s1, s2, s3)
  tri1.setColor(color1)
  tri1.setFilled(isfilled)
  print("area is", tri1.getArea())
  print("perimeter is", tri1.getPerimeter())
  print("color is", tri1.getColor(), "and isfilled", tri1.isFilled())
 except RuntimeError:
  print("invalid sides")
main()



#13.12
class TriangleError(RuntimeError):
 def __init__(self,side1,side2,side3):
  if side1+side2<=side3 or side2+side3<=side1 or side1+side3<=side2:
   raise RuntimeError("invalid sides")
  else:
   self.__side1=side1
   self.__side2=side2
   self.__side3=side3
 def getSide1(self):
  return self.__side1
 def getSide2(self):
  return self.__side2
 def getSide3(self):
  return self.__side3
 def getPerimeter(self):
  return self.__side1+self.__side2+self.__side3
def main():
 try:
   s1 = eval(input("first side"))
   s2 = eval(input("second side"))
   s3 = eval(input("third side"))
   tri1 = TriangleError(s1, s2, s3)
   print("perimeter: " ,tri1.getPerimeter())
 except RuntimeError:
   print("invalid side")
main()



#13.13 error
from tkinter import *
import pickle
import os.path
class Points():
 def __init__(self,u,x,y,v1,v2):
  self.u=u
  self.x=x
  self.y=y
  self.v1=v1
  self.v2=v2


class Graph():
 def __init__(self):
  window=Tk()
  window.title("graph")
  canvas1=Canvas(window,width=400,height=400)
  canvas1.pack()
  for i in range (0,len(self.pointsList)):
   for j in range(0, len(self.pointsList[i])):
    k=self.pointsList[i][3]
    l=self.pointsList[i][4]
    canvas1.create_line(self.pointsList[i][1],self.pointsList[i][2],self.pointsList[k][1],self.pointsList[k][2])
    canvas1.create_line(self.pointsList[i][1],self.pointsList[i][2],self.pointsList[l][1],self.pointsList[l][2])
  window.mainloop()
 def getPoints(self):
  outfile=open("points.dat","wb")
  pickle.dump(self.points)
  outfile.close
 def loadPoints(self):
  try:
   infile=open("points.dat","rb")
   self.pointsList=pickle.load(infile)
  except EOFError:
   self.pointsList=[]
  infile.close()
  return self.pointsList
def main():
  points=[]
  while True:
   u,x,y,v1,v2=eval(input("insert u,x,y,v1,v2; if 0 is inserted it terminates"))
   p1 = Points(u, x, y, v1, v2)
   points.append(p1)
   if u==0 and x==0 and y==0 and v1==0 and v2==0:
    break
main()
Graph()




#13.15
