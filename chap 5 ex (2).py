#5.12 error
number=100
for count in range(100,1000):
   if number%5==0 and number%6==0:
     print(number,end=' ')
     if count%10==0:
      print()
   number+=1

#5.13
   if number%5==0 and number%6==0:
     print(number,end=' ')

#5.23
loanAmount=eval(input("loan amount"))
loanPeriod=eval(input("loan period"))
print("Interest Rate","  ","Monthly Pay","  ","Total Pay")
monthlyInterest =5
while monthlyInterest<=8:
      monthlyPay=((monthlyInterest/1200)*loanAmount)/(1-1/((1+(monthlyInterest/1200))**(loanPeriod*12)))
      totalPay=monthlyPay*loanPeriod*12
      print(format(monthlyInterest,".3f"),"   ",format(monthlyPay,".2f"),"   ",format(totalPay,".2f"))
      monthlyInterest+=1/8

#5.24
loanAmount=eval(input("loan amount"))
loanPeriod=eval(input("loan period"))
annualInterestRate=eval(input("annual Interest"))
print("payment","\t\t","interest","\t\t","principal","\t\t","Balance")
monthlyPay=((annualInterestRate/1200)*loanAmount)/(1-1/((1+(annualInterestRate/1200))**(loanPeriod*12)))
balance=loanAmount
for month in range(1,loanPeriod*12+1):
  monthlyInterest=annualInterestRate*balance/1200
  principal=monthlyPay-monthlyInterest
  balance=balance-principal
  print(month,"\t\t\t\t", format(monthlyInterest,".2f"),"\t\t\t",format(principal, ".2f"),"\t\t",format(balance,".2f"))


#5.25
sum=0
sum2=1/50000
for n in range(1,50000,1):
  sum=sum+1/n
print(sum)
for m in range(500000-1,1,-1):
  sum2=sum2+1/m
print(sum2)

#5.26
sum=0
for n in range(1,97,2):
    sum=sum+n/(n+2)
    print(sum)

#5.27
sum=0
for i in range(1,10000):
    sum=sum+(((-1)**(i+1))/(2*i-1))
pi=4*sum
print (pi)
sum2=0
for i in range(1,20000):
    sum2=sum2+(((-1)**(i+1))/(2*i-1))
pi2=4*sum2
print (pi2)
sum3 = 0
for i in range(1,100000):
    sum3=sum3+(((-1)**(i+1))/(2*i-1))
pi3=4*sum3
print (pi3)

#5.28
sum=1
for i in range(1,1000,1):
    product = 1
    for j in range (i,0,-1):
        product=product*j
    sum=sum+1/product
print("e=",sum)
sum2=1
for o in range(1,2000,1):
    product2 = 1
    for p in range (o,0,-1):
        product2=product2*p
    sum2=sum2+1/product2
print("e=",sum2)
sum3=1
for q in range(1,10000,1):
    product3 = 1
    for w in range (q,0,-1):
        product3=product3*w
    sum3=sum3+1/product3
print("e=",sum3)

#5.29
count=0
for year in range (2001,2100,1):
    if ((year%4==0 and year%100!=0) or (year%400==0)):
        print(year,end= " ")
        count+=1
        if count%10==0:
            print()

#5.30

year=eval(input("year?"))
firstDay=eval(input("day?"))
num=firstDay
for i in range(2,13,1):
 if i==1:
    month='Jan'
    num=num+0
 if i == 2:
     month='Feb'
     num = num + 31 % 7
 if i == 3:
     month='March'
     num = num + 28 % 7
 if i == 4:
     month='April'
     num = num + 31 % 7
 if i == 5:
     month='May'
     num = num + 30 % 7
 if i == 6:
     month='June'
     num = num + 31 % 7
 if i == 7:
     month='July'
     num = num + 30 % 7
 if i == 8:
     month='August'
     num = num + 31 % 7
 if i == 9:
     month='Sept'
     num = num + 31 % 7
 if i == 10:
     month='Oct'
     num = num + 30 % 7
 if i == 11:
     month='Nov'
     num = num + 31 % 7
 if i == 12:
     month='Dec'
     num = num + 30 % 7
 if num==1 or num==8 or num==15 or num==22:
    day='Monday'
 if num==2 or num==9 or num==16 or num==23:
    day='Tuesday'
 if num==3 or num==10 or num==17 or num==24:
    day='Wedensday'
 if num==4 or num==11 or num==18 or num==25:
    day='Thursday'
 if num==5 or num==12 or num==19 or num==26:
    day='Friday'
 if num==6 or num==13 or num==20 or num==27:
    day='Saturday'
 if num==7 or num==14 or num==21 or num==28:
    day='Sunday'
 print("the first day of",month, "is on",day)

