
#2.13
digit=eval(input("enter an integer"))
digit1=digit%10
digit=digit//10
digit2=digit%10
digit=digit//10
digit3=digit%10
digit=digit//10
digit4=digit%10
print(digit4,"\n",digit3,"\n",digit2,"\n",digit1)

#2.14
x1,y1,x2,y2,x3,y3=eval(input("enter 3 points"))
side1=((x2-x1)**2+(y2-y1)**2)**0.5
side2=((x3-x2)**2+(y3-y2)**2)**0.5
side3=((x3-x1)**2+(y3-y1)**2)**0.5
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
area

#2.15
s=eval(input("the side?"))
area=(3*0.5*((3)**0.5))*s**2
area

#2.16
v0,v1,t=eval(input("average accelaration"))
a=(v1-v0)/t
a


#2.17
weightInPound=eval(input("weight in pound?"))
weightInKilogram=weightInPound*0.45359237
heightInInch=eval(input("height in meters"))
heightInMeter=heightInInch*0.0254
BMI=(weightInKilogram)/(heightInMeter)**2
BMI

#2.18
import time
currentTime=time.time()
totalSeconds=int(currentTime)
currentSecond=totalSeconds%60
currentMinute=totalSeconds//60
totalMinute=totalSeconds//60
currentMinute=totalMinute%60
totalHour=totalMinute//60
currentHour=totalHour%24
currentHour=totalHour%24
offset=eval(input("offset"))
currentHour=currentHour+offset+12

#2.19 
investmentAmount,annualInterest,n=eval(input("investmentAmount,annualInterest,n"))
futureInvestment=investmentAmount*(1+annualInterest/1200)**(n*12)
futureInvestment

#2.20
balance,interestRate=eval(input("balance,interestRate"))
interest=balance*(interestRate/1200)
interest


#2.21
monthly=eval(input("monthly"))
monthly=(monthly)*(1+0.00417)
monthly
monthly=(monthly+100)*(1+0.00417)
monthly=(monthly+100)*(1+0.00417)
monthly=(monthly+100)*(1+0.00417)
monthly=(monthly+100)*(1+0.00417)
monthly=(monthly+100)*(1+0.00417)
monthly

#2.22
popl1=312032486+((365*24*3600)//7)-(365*24*3600//13)+((365*24*3600//45))
popl1
popl2=popl1
change=((365*24*3600)//7)-(365*24*3600//13)+((365*24*3600//45))
popl2=popl1+change
popl3=popl2+change
popl4=popl3+change
popl5=popl4+change
num=eval(input("enter n of year"))
popl5=popl1+(num-1)*change
popl5

#2.23
import turtle
turtle.penup()
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.pendown()
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(100,0)
turtle.goto(100,-50)
turtle.circle(50)
turtle.pendown()
turtle.circle(50)
turtle.undo()
turtle.penup()
turtle.goto(100,-100)
turtle.circle(50)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(-100,-100)
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(50)
turtle.done()

#2.24


#2.25
x1,y1,width,height=eval(input("center,width,height"))
import turtle
turtle.penup()
turtle.goto(x1,y1)
turtle.goto(x1,y1+height/2)
turtle.pendown()
turtle.goto(x1+width/2,y1+height/2)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width/2)
turtle.done()



#2.26
x1,y1,radius=eval(input("center,radius"))
pi=3.14
area=pi*radius**2
import turtle
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(radius)
turtle.write(area)
turtle.done()
  