# review questions
#3.1
length=eval(input("length from center to vertex"))
import math
side=2*length*math.sin(math.pi/5)
area=(3*(3**0.5)/2)*side**2
area

#3.2
x1,y1=eval(input("latitude and longtiude"))
x2,y2=eval(input("latitude and longtiude"))
distance=6371.01*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+ math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y2-y1)))
distance


#3.4
side=eval(input("enter the side of pentagon"))
area=(5*side**2)/(4*math.tan(math.pi/5))
area

#3.5
side=eval(input("enter the side of polygon"))
n=int(input("no of side"))
area=(n*side**2)/(4*math.tan(math.pi/n))
area

#3.6
asci=eval(input("ASCII code?"))
string_val=str(asci)
print("the character is",chr(asci))


#3.7
import time
l=time.time()
l=int(time.time())
l=l//10000000
m=chr(int(l/2))
k=m.upper
k
k=m.lower()
k
'q'
  
#3.9
noOfHours,hourlyPayRate,federalTax,stateTax=eval(input("noOfHours,hourlyPayRate,federalTax,stateTax"))
name=input("name")
payroll=noOfHours*hourlyPayRate
deduction=federalTax*payroll+stateTax*payroll
netPay=payroll-deduction
netPay

#3.10
import turtle
turtle.write("\u03b1,\u03b2,\u03b3,\u03b4,\u03b5,\u03b6,\u03b6,\u03b7,\u03b8")
turtle.done

#3.11
e=eval(input("enter a number"))
digit1=e//10
digit1=e%10
remain1=e//10
digit2=remain1%10
remain2=remain1//10
digit3=remain2%10
remain3=remain2//10
digit4=remain3%10
remain4=remain3//10
print(digit1,digit2,digit3,digit4)

#3.12
import turtle
turtle.forward(100)
turtle.right(-36)
turtle.right(180)
turtle.forward(100)
turtle.right(36)
turtle.right(36)
turtle.right(36)
turtle.right(36)
turtle.forward(100)
turtle.right(4*36)
turtle.forward(100)
turtle.right(4*36)
turtle.forward(100)
turtle.done()

#3.13
import turtle
turtle.begin_fill()
turtle.color("red")
turtle.circle(100,steps=6)
turtle.end_fill()
turtle.goto(0,0)
turtle.goto(100,100)
turtle.goto(0,100)

turtle.begin_fill()
turtle.color("white")
turtle.write("STOP",font=("Times",18,"bold"))
turtle.end_fill()
turtle.done()



#3.14
radius=int(input("radius?"))
import turtle
turtle.penup()
turtle.goto(-100,100)
turtle.begin_fill()
turtle.undo()
turtle.pendown()
turtle.color("blue")
turtle.circle(radius)
turtle.penup()
turtle.goto(0,100)
turtle.color("black")
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.color("red")
turtle.goto(100,100)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(50,50)
turtle.color("yellow")
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(-50,50)
turtle.color("green")
turtle.pendown()
turtle.circle(radius)
turtle.done()

#3.15 not finished
import turtle
turtle.penup()
turtle.goto(-20,80)
turtle.goto(-20,160)
turtle.goto(-20,140)
turtle.goto(-35,140)
turtle.pendown()
turtle.dot(20,"black")
turtle.penup()
turtle.goto(165,140)
turtle.goto(65,140)
turtle.pendown()
turtle.dot(20,"black")
turtle.penup()
turtle.goto(-35,20)
turtle.goto(-35,40)
turtle.goto(-35,50)
turtle.right(36)
turtle.pendown()
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.down()
turtle.done()
  
  