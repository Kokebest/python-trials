Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 4/2
2.0
>>> 2/4
0.5
>>> 2//4
0
>>> 4//2
2
>>> 2.3**3.5
18.45216910555504
>>> (-2.5)**2
6.25
>>> 3%7
3
>>> 16%7
2
>>> seconds=eval(input("Enter an integer for seconds"))
Enter an integer for seconds500
>>> minutes=seconds//60
>>> remainingSecond=seconds%60
>>> print(seconds,"seconds is", minutes,"minutes and", remainingSeconds,"seconds)
      
SyntaxError: EOL while scanning string literal
>>> print(seconds,"seconds is", minutes,"minutes and", remainingSecond,"seconds)
      
SyntaxError: EOL while scanning string literal
>>> print(seconds,"seconds is", minutes,"minutes and",remainingSecond,"seconds)
      
SyntaxError: EOL while scanning string literal
>>> print(seconds,"seconds is", minutes,"minutes and",remainingSecond,"seconds")
500 seconds is 8 minutes and 20 seconds
>>> 1.23e-2
0.0123
>>> 1.23E-2
0.0123
>>> 42/5
8.4
>>> 42//5
8
>>> 42%5
2
>>> 40%5
0
>>> 1%2
1
>>> 2%1
0
>>> 45+4*4-2
59
>>> 45+43%5*(23*3%2)
48
>>> 5**2
25
>>> 5.1**2
26.009999999999998
>>> 2+(100%7)
4
>>> (2+100)%7
4
>>> 25/4
6.25
>>> 25//4
6
>>> i//=8
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    i//=8
NameError: name 'i' is not defined
>>> i=1
>>> i//=8
>>> i
0
>>> a=1
>>> a+=4
>>> a-=4
>>> a*=4
>>> a/=4
>>> a//=4
>>> a%=4
>>> a=56*a+6
>>> a
6.0
>>> int(a)
6
>>> eval(003)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> eval(3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    eval(3)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval("003")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    eval("003")
  File "<string>", line 1
    003
      ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> eval("3+4")
7
>>> purchaseamt=eval(input("purchse amount?"))
purchse amount?23600
>>> tax=purchseamt*0.06
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    tax=purchseamt*0.06
NameError: name 'purchseamt' is not defined
>>> tax=purchaseamt*0.06
>>> tax
1416.0
>>> purchaseamt=eval(input("purchse amount?"))197.555
SyntaxError: invalid syntax
>>> purchaseamt=eval(input("purchse amount?"))
purchse amount?197
>>> purchaseamt=eval(input("purchse amount?"))
purchse amount?197.55
>>> tax
1416.0
>>> tax=purchaseamt*0.06
>>> tax
11.853
>>> int(tax)
11
>>> value=4.6
>>> print(int(value))
4
>>> print(round(value))
5
>>> print(eval("4+*5+2"))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(eval("4+*5+2"))
  File "<string>", line 1
    4+*5+2
      ^
SyntaxError: invalid syntax
>>> print(eval("4*5+2"))
22
>>> print(int("04"))
4
>>> print(int("4.5"))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(int("4.5"))
ValueError: invalid literal for int() with base 10: '4.5'
>>> print(eval("04"))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(eval("04"))
  File "<string>", line 1
    04
     ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> time.time()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    time.time()
NameError: name 'time' is not defined
>>> import time
>>> time.time()
1627830931.0110579
>>> currentTime=time.time()
>>> totalSeconds=int(currentTime)
>>> totalMinutes=totalSeconds%60
>>> totalMinutes=totalSeconds//60
>>> currentSecond=total%60
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    currentSecond=total%60
NameError: name 'total' is not defined
>>> currentSecond=totalSeconds%60
>>> currentMinutes=totalSeconds%60
>>> totalHour=totalMinutes//60
>>> currentHour=totalHour%60
>>> currentMinutes=totalMinutes%60
>>> print(currentHour,":",currentMinutes,":",currentSeconds)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(currentHour,":",currentMinutes,":",currentSeconds)
NameError: name 'currentSeconds' is not defined
>>> print(currentHour,":",currentMinutes,":",currentSecond)
15 : 17 : 52
>>> annualInterestRate=eval(input("Enter annual Interest"))
Enter annual Interest5.75
>>> n=eval(input("Enter num of year"))
Enter num of year15
>>> loan=eval(iput("Enter loan"))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    loan=eval(iput("Enter loan"))
NameError: name 'iput' is not defined
>>> loan=eval(input("Enter loan"))
Enter loan250000
>>> monthlyPay=loan*monthlyInterestRate/(1-1/(1+(annualInterestRate/1200))**(n*12))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    monthlyPay=loan*monthlyInterestRate/(1-1/(1+(annualInterestRate/1200))**(n*12))
NameError: name 'monthlyInterestRate' is not defined
>>> monthlyPay=(loan*(annualInterestRate/1200))/(1-1/(1+(annualInterestRate/1200))**(n*12))
>>> monthlyPay
2076.025217549142
>>> x1,y1=eval(input("enter 2 points"))
enter 2 points3,4
>>> x2,y2=eval(input("enter 2 points"))
enter 2 points4,6
>>> distance=((x2-x1)**2+(y2-y1)**2)**0.5
>>> distance
2.23606797749979
>>> x1,y1=eval(input("enter 2 points"))
enter 2 points1.5,-3.4
>>> x2,y2=eval(input("enter 2 points"))
enter 2 points4,5
>>> distance=((x2-x1)**2+(y2-y1)**2)**0.5
>>> distance
8.764131445842194
>>> import turtle
>>> turtle penup()
SyntaxError: invalid syntax
>>> turtle.penup()
>>> turtle.goto(x1,y1)
>>> turtle.pendown()
>>> turtle.write("Point 1")
>>> turtle.goto(x2,y2)
>>> turtle.write("Point 2")
>>> turtl.penup()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    turtl.penup()
NameError: name 'turtl' is not defined
>>> x1,y1=eval(input("enter 2 points"))
enter 2 points-50,
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    x1,y1=eval(input("enter 2 points"))
ValueError: not enough values to unpack (expected 2, got 1)
>>> x1,y1=eval(input("enter 2 points"))
enter 2 points-50,34
>>> x2,y2=eval(input("enter 2 points"))
enter 2 points49,-85
>>> turtle.penup()
>>> turtle.goto(x1,y1)
>>> turtle.pendown()
>>> turtle.write("Point 1")
>>> turtle.goto(x2,y2)
>>> turtle.write("Point 2")
>>> turtle.penup()
>>> turtle.goto((x1+x2)/2,(y1+y2)/2)
>>> turtle.write(distance)
>>> turtle.done()
