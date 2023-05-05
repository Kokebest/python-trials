#Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

radius=1
print(radius>0)

print(int(True))

print(bool(0))

print(bool(4))
u=int(True)
u

j=int(False)
j

b1=bool(4)
b1

import random
random.random()


i=random.randrange(0,20)
i

i=random.randrange(10,20)
i

i=random.randrange(10,20)
i

i=random.randint(10,50)
i

i=random.randint(0,1)
i

i=random.randint(0,1)
i

import math
if radius>=0:
 area=radius*radius*math.pi
 print("The area", area )



number=6
if number%2==0:
    print("even")
else:
    print("odd")
    
    
import random
num1=random.randint(0,9)
num2=random.randint(0,9)
if num1<num2:
    num1,num2=num2,num1
answer=eval(input("difference of"+str(num1)+"-"+str(num2)+"?")) 
if num1-num2==answer:
    print("correct")
else: 
    print("wrong")


score,pay=10,30
if score>90:
    pay=pay+3*pay/100
else:
    pay=pay+pay/100    
    
if number%2==0:
   print("even")
print("odd")    


score=93
if score>=85:
    grade="A"
elif score>=80:
        grade="B"
elif score>=70:
        grade="C"
elif score>=60:
        grade="D"
else:
        grade="F"
        
year=1997     
z=year%12
if z==0:
    print("monkey")
elif z==1:
    print("rooster")
elif z==2:
    print("dog")
elif z==3:
    print("pig")
elif z==4:
    print("rat")
elif z==5:
    print("ox")
elif z==6:
    print("tiger")
elif z==7:
    print("rabbit")
elif z==8:
    print("dragon")
elif z==9:
    print("snake")
elif z==10:
    print("horse")  
else:
    print("sheep")
        
x,y=3,2

if x > 2:
 if y > 2:
    z = x + y
    print("z is", z)
 else:
  print("x is", x)        

x,y=3,3
if x > 2:
  if y > 2:
     z = x + y
     print("z is", z)
else:
   print("x is", x)

score=50
if score >= 60.0:
 grade = 'D'
elif score >= 70.0:
 grade = 'C'
elif score >= 80.0:
 grade = 'B'
elif score >= 90.0:
 grade = 'A'
else:
 grade = 'F'  
 
 
i=5
if i > 0:
  x = 0
  y = 1
else:
   y = 0
   z = 0



weight,height=eval(input("enter weight and height"))
weightInKilo=weight*0.45
heightInMeter=height*0.0254
BMI=weightInKilo/(heightInMeter)**2
if BMI<18.5:
    print ("underweight")
elif BMI<25:
    print ("Normal")
elif BMI<30:
    print("overweight")
else:
    print("obese")
    
status=eval(input("single,married,married but separately, head of household")) 
income=eval(input("income"))
tax=0
if status==0:
   if income<=8350:
        tax=10*income/100
   elif income<=33950:
        tax=10*8350/100+15*(income-8350)/100
   elif income<=82250:
        tax=10*8350/100+(33950-8350)*15/100+25*(income-33950)/100
   elif income<=171550:
        tax=10*8350/100+(33950-8350)*15/100+25*(82250-33950)/100+28*(income-82250)/100
   elif income<=372950:
        tax=10*8350/100+(33950-8350)*15/100+25*(82250-33950)/100+28*(171550-82250)/100+0.33*(income-171550)
   else: 
        tax=10*8350/100+(33950-8350)*15/100+25*(82250-33950)/100+28*(171550-82250)/100+0.33*(372950-171550)+0.35*(income-372950)
elif status==1:
   if income<16700:
        tax=10*income/100
   elif income<67900:
        tax=10*16700/100+15*(income-16700)/100
   elif income<137050:
        tax=10*16700/100+(67900-16700)*15/100+25*(income-67900)/100
   elif income<208850:
        tax=10*16700/100+(67900-16700)*15/100+25*(137050-67900)/100+28*(income-137050)/100
   elif income<372950:
        tax=10*16700/100+(67900-16700)*15/100+25*(137050-67900)/100+28*(208850-137050)/100+0.33*(income-208850)
   else: 
        tax=10*16700/100+(67900-16700)*15/100+25*(137050-67900)/100+28*(208850-137050)/100+0.33*(372950-208850)+0.35*(income-372950)
elif status==2:
   if income<8350:
        tax=10*income/100
   elif income<33950:
        tax=10*8350/100+15*(income-8350)/100
   elif income<68525:
        tax=10*8350/100+(33950-8350)*15/100+25*(income-33950)/100
   elif income<104425:
        tax=10*8350/100+(33950-8350)*15/100+25*(68525-33950)/100+28*(income-68525)/100
   elif income<186475:
        tax=10*8350/100+(33950-8350)*15/100+25*(68525-33950)/100+28*(104425-68525)/100+0.33*(income-104426)
   else: 
        tax=10*8350/100+(33950-8350)*15/100+25*(68525-33950)/100+28*(104425-68525)/100+0.33*(186475-171550)+0.35*(income-186476)    
elif status==3:
   if income<11950:
        tax=10*income/100
   elif income<45500:
        tax=10*11950/100+15*(income-11950)/100
   elif income<117450:
        tax=10*11950/100+(45500-11950)*15/100+25*(income-45500)/100
   elif income<190200:
        tax=10*11950/100+(45500-11950)*15/100+25*(117450-45500)/100+28*(income-117450)/100
   elif income<372950:
        tax=10*11950/100+(45500-11950)*15/100+25*(117450-45500)/100+28*(190200-117450)/100+0.33*(income-190200)
   else: 
        tax=10*11950/100+(45500-11950)*15/100+25*(117450-45500)/100+28*(190200-117450)/100+0.33*(372950-190200)+0.35*(income-372950)    
        
print(tax)

number=eval(input("Enter an integer"))
if number%2==0 and number%3==0:
  print ("divisible by both")
if number%2==0 or number%3==0:
  print("divisible only by one")
if (number%2==0 or number%3==0) and not(number%2==0 and number%3 == 0): 
  print ("not by both")

x >= y >= 0
x <= y >= 0
x != y == 5
(x != 0) or (x == 0)         


year=eval(input("year?"))
isyear=(year%4==0 and year%100!=0)or(year%400==0)
print (isyear)

import random 
randomnum=random.randrange(10,100)
rand2=eval(input("enter a 2 digit number"))
rdigit1=randomnum//10
rdigit2=randomnum%10
digit1=rand2//10
digit2=rand2%10
if (rand2==randomnum):
    print ("u won $10000")
elif (digit2==rdigit1 and digit1==rdigit2):
    print("3000")
elif (digit1==rdigit1 or digit1==rdigit2 or digit2==rdigit1 or digit2==rdigit2):
    print("1000")
else: 
    print("no match")
    
    
 
import turtle
x1,y1=eval(input("center of circle"))
r=eval(input("radius"))
x2,y2=eval(input("enter a point"))
turtle.penup()
turtle.goto(x1,y1-r)    
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(3)
turtle.end_fill() 
turtle.penup()
turtle.goto(x1-70, y1-r-20)
turtle.pendown() 
d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
if d<=r:
    turtle.write("inside")
else:
    turtle.write("outside")
turtle.done()    
    
    
	 