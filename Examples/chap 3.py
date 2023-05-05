Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> exp(2)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    exp(2)
NameError: name 'exp' is not defined
>>> math.exp(2)
7.38905609893065
>>> math.sqrt(4)
2.0
>>> math.sin(math.pi)
1.2246467991473532e-16
>>> math.sin(math.pi/2)
1.0
>>> x1,y,,x2,y2,x3,y3=eval(input("enter three points" ))
SyntaxError: invalid syntax
>>> x1,y1,x2,y2,x3,y3=eval(input("enter three points" ))
enter three points3,5,5,7,6,8
>>> A=math.degrees(math.acos(a*a-b*b-c*c))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    A=math.degrees(math.acos(a*a-b*b-c*c))
NameError: name 'a' is not defined
>>> a=math.sqrt((x2-x3)**2+(y2-y3)**2)
>>> b=math.sqrt((x3-x1)**2+(y3-y1)**2)
>>> c=math.sqrt((x3-x1)**2+(y3-y1)**2)
>>> A=math.degrees(math.acos(a*a-b*b-c*c)/(-2*b*c))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    A=math.degrees(math.acos(a*a-b*b-c*c)/(-2*b*c))
ValueError: math domain error
>>> A= math.degrees(math.acos(a*a-b*b-c*c)/(-2*b*c))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    A= math.degrees(math.acos(a*a-b*b-c*c)/(-2*b*c))
ValueError: math domain error
>>> B= math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
>>> A= math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
>>> 
>>> B= math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
>>> C= math.degrees(math.acos((c*c-a*a-b*b)/(-2*a*b)))
>>> A
19.18813645372093
>>> B
80.40593177313954
>>> C
80.40593177313954
>>> math.sqrt(4)
2.0
>>> math.sin(1*math.pi)
1.2246467991473532e-16
>>> math.sin(2*math.pi)
-2.4492935982947064e-16
>>> math.cos(2*math.pi)
1.0
>>> min(2,2,1)
1
>>> math.log(math.e)
1.0
>>> math.exp(1)
2.718281828459045
>>> max(2,3,4)
4
>>> abs(-2.5)
2.5
>>> math.ceil(-2.5)
-2
>>> math.floor(-2.5)
-3
>>> round(3.5)
4
>>> round(-2.5)
-2
>>> math.fabs(2.5)
2.5
>>> math.ceil(2.5)
3
>>> math.floor(2.5)
2
>>> round(-2.5)
-2
>>> round(2.6)
3
>>> round(math.fabs(-2.5))
2
>>> math.sin(90)
0.8939966636005579
>>> math.sin(math.degrees(90))
-0.9540914674728181
>>> math.sin((math.pi)/2)
1.0
>>> math.sin(math.degrees(math.pi/2))
0.8939966636005579
>>> math.pi/2
1.5707963267948966
>>> math.sin(math.radians(90))
1.0
>>> var=math.radians(47)
>>> var
0.8203047484373349
>>> var=math.degrees(math.pi/7)
>>> var
25.714285714285715
>>> import turtle
>>> turtle.write("\u6B22\u8FCE\u03b2\u03b3")
>>> turtle.done()
>>> chr(98)
'b'
>>> ord("k")
107
>>> ord("K")
75
>>> ord("K")-ord("k")
-32
>>> print("He said,\"I am coming.\"")
He said,"I am coming."
>>> print("AAA",end=' ')
AAA 
>>> 1 print("AAA", end = ' ')
2 print("BBB", end = '')
3 print("CCC", end = '***')
4 print("DDD", end = '***')
SyntaxError: invalid syntax
>>> print("AAA", end = ' ')
print("BBB", end = '')
print("CCC", end = '***')
print("DDD", end = '***')
SyntaxError: multiple statements found while compiling a single statement
>>> print("AAA", end = ' '),print("BBB", end = ''), print("CCC", end = '***'),print("DDD", end = '***')
AAA BBBCCC***DDD***(None, None, None, None)
>>> print("AAA"),print("BBB"), print("CCC"),print("DDD")
AAA
BBB
CCC
DDD
(None, None, None, None)
>>> print("AAA"),print("BBB"), print("CCC"),print("DDD")
AAA
BBB
CCC
DDD
(None, None, None, None)
>>> print("AAA",end=''),print("BBB",,end=''), print("CCC",end=''),print("DDD",end='')
SyntaxError: invalid syntax
>>> print("AAA",end=''),print("BBB",end=''), print("CCC",end=''),print("DDD",end='')
AAABBBCCCDDD(None, None, None, None)
>>> z=str(4)
>>> z
'4'
>>> s="chapter"+str("4")
>>> s
'chapter4'
>>> s="chapter "+str("4")
>>> s
'chapter 4'
>>> message="Welcome to python"
>>> message+="its really fun"
>>> message
'Welcome to pythonits really fun'
>>> message="Welcome to python "
>>> message+="its really fun"
>>> message
'Welcome to python its really fun'
>>> s1=input("insert a string")
insert a stringk
>>> s1
'k'
>>> s1=input("insert a string")
insert a string4
>>> s1
'4'
>>> print()

>>> 
>>> print("the string is "+s1)
the string is 4
>>> print()

>>> ord(1)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
>>> ord("1")
49
>>> ord("A")
65
>>> ord("B")
66
>>> ord("a")
97
>>> ord("b")
98
>>> chr(40)
'('
>>> chr(59)
';'
>>> chr(79)
'O'
>>> chr(85)
'U'
>>> chr(90)
'Z'
>>> chr(68)
'D'
>>> ch=(ord(A)+3)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    ch=(ord(A)+3)
TypeError: ord() expected string of length 1, but float found
>>> ch=chr(ord(A)+3)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    ch=chr(ord(A)+3)
TypeError: ord() expected string of length 1, but float found
>>> ch=chr(ord('A')+3)
>>> ch
'D'
>>> ord("Z")-ord("A")
25
>>> title="chapter"+1
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    title="chapter"+1
TypeError: can only concatenate str (not "int") to str
>>> title="chapter"+"1"
>>> sum=2+3,print(sum),s="2"+"3",print(s)
SyntaxError: can't assign to operator
>>> sum=2+3
>>> s="2"+"3"
>>> print(sum),print(s)
5
23
(None, None)
>>> money=print("enter the money")
enter the money
>>> 11.56
11.56
>>> moneyInCents=money*100
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    moneyInCents=money*100
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> money=eval(input("enter the money"))
enter the money11.56
>>> moneyInCents=money*100
>>> numOfDollars=mneyInCents%100
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    numOfDollars=mneyInCents%100
NameError: name 'mneyInCents' is not defined
>>> numOfDollars=moneyInCents%100
>>> numOfDollars=moneyInCents//100
>>> remainingCent=moneyInCents%100
>>> numofQuarter=remainingCent//25
>>> remainingQuarter=remainingCent%25
>>> numofDime=remainingQarter//25
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    numofDime=remainingQarter//25
NameError: name 'remainingQarter' is not defined
>>> numofDime=remainingQuarter//25
>>> remainingDime=remainingQuarter%25
>>> numofnickel=remainingDime//25
>>> remainingNickel=remainingDime%25
>>> numofDime=remainingQuarter//10
>>> remainingDime=remainingQuarter%10
>>> numofnickel=remainingDime//10
>>> numofnickel=remainingDime//5
>>> remainingDime=remainingQuarter%5
>>> pennies=remainingDime%5
>>> print(numOfDollars,"dollar",numofQuarter,"Quarters",numofDime,"dime",numofnickel,"nickel",pennies,"pennies")
11.0 dollar 2.0 Quarters 0.0 dime 1.0 nickel 1.0 pennies
>>> id(money)
1687120451384
>>> type(money)
<class 'float'>
>>> myName=Kokeb
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    myName=Kokeb
NameError: name 'Kokeb' is not defined
>>> myName="Kokeb"
>>> up=myName.lower()
>>> up
'kokeb'
>>> down=myName.upper()
>>> down
'KOKEB'
>>> myName="Kokeb/n"
>>> myName
'Kokeb/n'
>>> s1=myName.strip()
>>> s1
'Kokeb/n'
>>> myName="Kokeb\n"
>>> myName
'Kokeb\n'
>>> s1=myName.strip()
>>> s1
'Kokeb'
>>> s="\tGeorgia\n"
>>> s1=s.lower()
>>> s1
'\tgeorgia\n'
>>> s1=s.upper()
>>> 
>>> s1
'\tGEORGIA\n'
>>> s="\tGeor\tgia\n"
>>> s1=s.strip()
>>> s1
'Geor\tgia'
>>> interest=100/3
>>> v=round(interest,2)
>>> v
33.33
>>> v=format(interest,".2f")
>>> v
'33.33'
>>> print(format(57.467657,"10.2f"))
     57.47
>>> print(format(12345678.923,"10.2f"))
12345678.92
>>> print(format(57,"10.2f"))
     57.00
>>> print(format(57.4,"10.2f"))
     57.40
>>> print(format(57.4,"1.2f"))
57.40
>>> print(format(57.4,"0.2f"))
57.40
>>> print(format(57.4,"2.2f"))
57.40
>>> print(format(57.4,"10.2f"))
     57.40
>>> print(format(57.4,"3.2f"))
57.40
>>> print(format(57.4,"4.2f"))
57.40
>>> print(format(57.4,"5.2f"))
57.40
>>> print(format(57.4,"6.2f"))
 57.40
>>> print(format(57.4,"6.2e"))
5.74e+01
>>> print(format(57.4,"10.2e"))
  5.74e+01
>>> print(format(57.4,"2.2e"))
5.74e+01
>>> print(format(57.4,"0.2e"))
5.74e+01
>>> print(format(57.4,"10.2%"))
  5740.00%
>>> print(format(57.4,"<10.2%"))
5740.00%  
>>> print(format(578956463,"<10d"))
578956463 
>>> print(format(578956463,"<10x"))
22822caf  
>>> print(format(578956463,"<10o"))
4240426257
>>> print(format(578956463,"<10b"))
100010100000100010110010101111
>>> print(format("welcome","10s"))
welcome   
>>> #3.19
>>> print(format(57.467657,"9.3f")),print(format(12345678.923,"9.1f")),print(format(57.4,".2f")),print(format(57.4,"10.2f"))
   57.468
12345678.9
57.40
     57.40
(None, None, None, None)
>>> print(format(57.467657,"9.3e")),print(format(12345678.923,"9.1e")),print(format(57.4,".2e")),print(format(57.4,"10.2e"))
5.747e+01
  1.2e+07
5.74e+01
  5.74e+01
(None, None, None, None)
>>> print(format(5789.467657,"9.3f")),print(format(5789.467657,"<9.3f")),print(format(5789.4,".2f")),print(format(5789.4,"<.2f")),print(format(5789.4,">9.2f"))
 5789.468
5789.468 
5789.40
5789.40
  5789.40
(None, None, None, None, None)
>>> print(format(0.457467657,"9.3%")),print(format(0.457467657,"<9.3%"))
  45.747%
45.747%  
(None, None)
>>> print(format(45,"5d")),print(format(45,"<5d")),print(format(45,"5x")),print(format(45,"<5x"))
   45
45   
   2d
2d   
(None, None, None, None)
>>> print(format("programming is fun","25s")),print(format("programming is fun","<25s")),print(format("programming is fun",">25s"))
programming is fun       
programming is fun       
       programming is fun
(None, None, None)
>>> import turtle
>>> turtle.speed(5)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    turtle.speed(5)
  File "<string>", line 5, in speed
turtle.Terminator
>>> turtle.circle(50,1,3)
>>> turtle.circle(50)
>>> turtle.circle(50,0,3)
>>> turtle.circle(50,steps=3)
>>> turtle.circle(50,steps=4)
>>> turtle.circle(50,steps=5)
>>> turtle.dot(3,red)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    turtle.dot(3,red)
NameError: name 'red' is not defined
>>> turtle.dot(3,"red")
>>> turtle.reset()
>>> turtle.penup()
>>> turtle.goto(-200,0)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("red")
>>> turtle.circle(50,steps=3)
>>> turtle.end_fill()
>>> turtle.penup()
>>> turtle.goto(-100,0)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("yellow")
>>> turtle.circle(50,steps=4)
>>> turtle.end_fill()
>>> turtle.penup()
>>> turtle.goto(0,0)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("green")
>>> turtle.circle(50,steps=5)
>>> turtle.end_fill()
>>> turtle.penup()
>>> turtle.goto(100,0)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("purple")
>>> turtle.circle(50,steps=6)
>>> turtle.end_fill()
>>> turtle.penup()
>>> turtle.goto(200,0)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.color("purple")
>>> turtle.circle(50)
>>> turtle.end_fill()
>>> turtle.penup()
>>> turtle.goto(100,100)
>>> turtle.goto(-100,150)
>>> turtle.pendown()
>>> turtle.begin_fill()
>>> turtle.write("Cool colorful shapes",font=("Times",18,"bold"))
>>> turtle.done()
>>> 
