#12.1
class GeometricObjects():
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    def isFilled(self):
        return self.filled
    def setFilled(self,filled):
        self.filled=filled
    def __str__(self):
        return "Color: "+self.color+"is filled:"+self.filled
class Triangle(GeometricObjects):
    def __init__(self,side1=1.0,side2=1.0,side3=1.0):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def getArea(self):
        s=(self.side1+self.side2+self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    def getPerimeter(self):
        return (self.side1+self.side2+self.side3)
    def __str__(self):
        return "side1"+self.side1+"side2"+self.side2+"side3"+self.side3
def main():
    s1=eval(input("first side"))
    s2=eval(input("second side"))
    s3=eval(input("third side"))
    color1=input("color?")
    isfilled=eval(input("1 or 0 for filled"))
    tri1=Triangle(s1, s2, s3)
    tri1.setColor(color1)
    tri1.setFilled(isfilled)
    print("area is",tri1.getArea())
    print("perimeter is", tri1.getPerimeter())
    print("color is", tri1.getColor(),"and isfilled",tri1.isFilled())
main()



#12.2 error
class Location():
 def __init__(self,row,column):
     self.row=row
     self.column=column
 def locateLargest(self,matrix):
     maxValue=max(matrix)
     maxindex=matrix.index(maxValue)
     return ("max is",maxValue,"which is at",maxindex)
def main():
 rows,columns=eval(input("row and column"))
 a=rows*[columns*[0]]
 b=rows*[columns*[0]]
 for i in range (0,len(a)):
     rowi=input("enter the rows")
     a[i]=rowi.split(" ")
 u=Location(rows,columns)
 print(u.locateLargest(a))
main()



#12.3 error
class Account():
 def __init__(self,id=0,Balance=100,annualInterestRate=0):
     self.__id=id
     self.__annualInterstRate=annualInterestRate
     self.__Balance=Balance
 def getId(self):
    return self.__id
 def getBalance(self):
    return self.__Balance
 def getAnnualInterestRate(self):
    return self.__annualInterestRate
 def setId(self,ID):
     self.__id=ID
 def setBalance(self,Balance):
     self.__Balance=Balance
 def setId(self,annualInterestRate):
     self.__annualInterstRate=annualInterestRate
 def getMonthlyInterestRate(self):
     return self.__annualInterstRate/1200
 def getMonthlyInterest(self):
     return self.__annualInterstRate*self.__Balance/1200
 def withdraw(self,amount):
     self.__Balance=self.__Balance-amount
     return self.__Balance
 def deposit(self,amount):
     self.__Balance=self.__Balance+amount
     return self.__Balance


def main():
 acceptId = eval(input('ID of account?'))
 z=Account(acceptId,100,4.25)
 num=eval(input("Main Menu:""\n""1: check balance""\n""2: withdraw""\n""3: deposit""\n""4: exit"))
 while True:
  if num==1:
    print(z.getBalance())
    continue
  elif num==2:
    withdraw1=eval(input("how much do u wanna withdraw"))
    z.withdraw(withdraw1)
    continue
  elif num==3:
    deposit1=eval(input("how much do u wanna deposit"))
    z.deposit(deposit1)
    continue
  elif num == 4:
    acceptId = eval(input('ID of account?'))
    z = Account(acceptId, 100, 4.25)
    continue
 num = input("Main Menu:""\n""1: check balance""\n""2: withdraw""\n""3: deposit""\n""4: exit")
main()


#12.4
'''class Rectangle2D():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def getX(self):
        return self.x
    def setX(self,x1):
        self.x=x1
    def getY(self):
        return self.y
    def setX(self, y1):
        self.y=y1
    def getWidth(self):
        return self.width
    def setWidth(self, width1):
        self.width=width1
    def getHeight(self):
        return self.height
    def setHeight(self, height1):
        self.height=height1
    def containsPoint(self,a,b):
        if self.x-self.width/2<=a<=self.x+self.width/2 and self.y-self.height/2<=b<=self.y+self.height/2:
            return True
        else:
            return False'''

def getRectangle(x,y):
    x.sort()
    y.sort()
    centerx=(max(x)+min(x))/2
    centery=(max(y)+min(y))/2
    width=(max(x)-centerx)*2
    height=(max(y)-centery)*2
    return ("center of rec is",(centerx,centery),"with width ",width," and height",height)

def main():
 row1=input("Enter points")
 points=row1.split(" ")
 xPoints,yPoints=[],[]
 for i in range(0,len(points)):
    if i%2==0:
     xPoints.append(eval(points[i]))
    else:
     yPoints.append(eval(points[i]))
 print(getRectangle(xPoints,yPoints))

main()


#12.5

