# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:46:35 2021

@author: kokeb
"""

def grades(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"   
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"    
    else:
        return "F"    

print(grades(86)) 


def sum(a,b):
 s1=a+b
 return

print(sum(1,2))  


def max(a1,b1):
 if a1>b1: 
     return a1
 else:
     return b1

max(5,9)  

def xFunction(x, y):
 print(x + y)
 return 

def function1(n, m):
 function2(3.4)

def function2(n):
 if n > 0:
  return 1
 elif n == 0:
  return 0
 elif n < 0:
  return -1
function1(2, 3)




def main():
 print(min(5, 6))

def min(n1, n2):
 smallest = n1
 if n2 < smallest:
  smallest = n2

main()



def main():
 print(min(min(3,4),(51, 6)))
def min(n1, n2):
 smallest = n1
 if n2 < smallest:
  smallest = n2
  return smallest
main() 


def huhu(b):
    print ("huhu")
    
huhu(3)



def main():
 max = 0
 getMax(1, 2, max)
 print(max)
def getMax(value1, value2, max):
 if value1 > value2:
  max = value1
 else:
  max = value2
main()  



def main():
 i = 1
 while i <= 6:
  print(function1(i, 2))
  i += 1
def function1(i, num):
 line = "" 
 for j in range(1, i):
  line += str(num) + " "
  num *= 2
 return line
main() 




def main():
 # Initialize times
 times = 3
 print("Before the call, variable","times is", times)
 # Invoke nPrintln and display times
 nPrint("Welcome to CS!", times)
 print("After the call, variable","times is", times)
 # Print the message n times
def nPrint(message, n):
 while n > 0:
  print("n = ", n)
  print(message)
  n -= 1
main() 


def main():
 i = 0
 while i <= 4:
  function1(i)
  i += 1
  print("i is", i)
def function1(i):
 line = " "
 while i >= 1:
  if i % 3 != 0:
   line += str(i) + " "
   i -= 1
 print(line)
main()




from GCD import gcd
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisor for", n1, "and", n2, "is", gcd(n1, n2))


# Convert a decimal to a hex as a string
def decimalToHex(decimalValue):
 hex = " "
 while decimalValue != 0:
  hexValue = decimalValue % 16
  hex = toHexChar(hexValue) + hex
  decimalValue = decimalValue // 16

 return hex

# Convert an integer to a single hex digit as a character
def toHexChar(hexValue): 
 if 0 <= hexValue <= 9:
  return chr(hexValue + ord('0'))
 else: # 10 <= hexValue <= 15
  return chr(hexValue - 10 + ord('A'))

def main():
 # Prompt the user to enter a decimal integer
 decimalValue = eval(input("Enter a decimal number: "))

 print("The hex number for decimal", decimalValue, "is", decimalToHex(decimalValue))

main() # Call the main function








def sum(i1, i2):
 result = 0
 for i in range(i1, i2 + 1):
  result += i

 return result

print("Sum from 1 to 10 is", sum(20, 37))
print("Sum from 20 to 37 is", sum(20, 37))
print("Sum from 35 to 49 is", sum(35, 49))




def function(x):
 print(x)
 x = 4.5
 y = 3.4
 print(y)
x = 2
y = 4
function(x)
print(x)
print(y)


def f(x, y = 1, z = 2):
 return x + y + z
print(f(1, 1, 1))
print(f(y = 1, x = 2, z = 3))
print(f(1, z = 3))


def function():
 x = 4.5
 y = 3.4
 print(x)
 print(y)
function()
print(x)
print(y)


x = 10
if x < 0:
 y = -1
else:
 y = 1
print("y is", y)



def f(w = 1, h = 2):
 print(w, h)
f()
f(w = 5)
f(h = 24)
f(4, 5)


def main():
 nPrintln(5)

def nPrintln(n,message = "Welcome to Python!"):
 for i in range(n):
  print(message)

def main():
 nPrintln(5)  
main()




def f(x, y):
  return x + y, x - y, x * y, x / y

t1, t2, t3, t4 = f(9, 5)
print(t1, t2, t3, t4)