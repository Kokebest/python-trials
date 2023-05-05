#11.1
def sumColumn(m, columnIndex):
 sumColumn=(len(m[0]))*[0]
 for a in range (0,columnIndex):
  for b in range(0,len(m[a])):
    sumColumn[b]+=m[a][b]
 print("Sum of each column is",sumColumn)
def main():
 matrix1=[4*[0],4*[0],4*[0]]
 row1=input("enter the rows")
 matrix1[0]=row1.split(" ")
 row2=input("enter the rows")
 matrix1[1]=row2.split(" ")
 row3=input("enter the rows")
 matrix1[2]=row3.split(" ")
 for i in range (0,3):
  for j in range(0,4):
   matrix1[i][j]=eval(matrix1[i][j])
 sumColumn(matrix1,3)
main()


#11.2
def sumMajorColumn(m):
 sum=0
 for d in range (0,len(m)):
  for e in range(0,len(m[0])):
   if d==e:
    sum=sum+m[d][e]
 return sum
def main():
 rows1=eval(input("how many rows?"))
 matrix2, matrix3=rows1*[[0]],rows1*[[0]]
 for e in range (0,rows1):
  rows2=input("insert row")
  matrix2[e]=rows2.split(" ")
 for c in range(0,len(matrix2)):
  for d in range (0,len(matrix2[c])):
   matrix2[c][d]=eval(matrix2[c][d])
 print(sumMajorColumn(matrix2))
main()

#11.3
def main():
 correctAnswers=[]
 correctAnswer=0
 answers=[['A','B','A','C','C','D','E','E','A','D'],['D','B','A','B','C','A','E','E','A','D'],['E','D','D','A','C','B','E','E','A','D'],['C','B','A','E','D','C','E','E','A','D'],['A','B','D','C','C','D','E','E','A','D'],['B','B','E','C','C','D','E','E','A','D'],['B','B','A','C','C','D','E','E','A','D'],['E','B','E','C','C','D','E','E','A','D']]
 keys=['D','B','D','C','C','D','A','E','A','D']
 for f in range(0,len(answers)):
  correctAnswer = 0
  for g in range(0,len(answers[f])):
   if answers[f][g]==keys[g]:
     correctAnswer+=1
  correctAnswers.append(correctAnswer)
 for h in range(0,len(correctAnswers)):
   maxnum = max(correctAnswers)
   print("rank ",h+1,"goes to student ",(correctAnswers.index(maxnum)))
   i=correctAnswers.index(maxnum)
   correctAnswers[i]=0
main()

#11.4 error
def main():
 rows3=eval(input("num of employees?"))
 matrix4=rows3*[7*[0]]
 matrix5=rows3*[7*[0]]
 sumOfHours=rows3*[0]
 for i in range(0,len(matrix4)):
   rows4=input("enter the number of hours that the employees worked")
   matrix4[i]=rows4.split(" ")
 for k in range(0,len(matrix4)):
  for l in range(0,len(matrix4[k])):
   matrix5[k][l] = eval(matrix4[k][l])
 for m in range(0, len(matrix5)):
  for n in range(0, len(matrix5[m])):
   sumOfHours[m]+=matrix5[m][n]
 for o in range(0, len(sumOfHours)):
   maxnum = max(sumOfHours)
   print("employee",(sumOfHours.index(maxnum),"worked",sumOfHours[sumOfHours.index(maxnum)]))
   i = sumOfHours.index(maxnum)
   sumOfHours[i] = 0
main()



#11.5 error
def addMatrix(a,b):
 row1=len(a)
 column1=len(a[0])
 matrix9=row1*[column1*[0]]
 for p in range(0,(len(matrix9))):
  for q in range(0,len(matrix9[p])):
   matrix9[p][q]=a[p][q]+b[p][q]
 return matrix9
def main():
 rowNo=eval(input("number of rows?"))
 columnNo=eval(input("number of columns?"))
 matrix7=rowNo*[columnNo*[0]]
 matrix8=rowNo*[columnNo*[0]]
 rows1=input("the first matrix?")
 rows2 = input("the second matrix?")
 matrix5 = rows1.split(" ")
 matrix6 = rows2.split(" ")
 for t in range (0,rowNo):
  matrix7[t]=matrix5[rowNo*t:rowNo*(t+1)]
  matrix8[t]=matrix6[rowNo*t:rowNo*(t+1)]
 for r in range(0,len(matrix7)):
  for s in range (0,len(matrix8[r])):
   matrix7[r][s]=eval(matrix7[r][s])
   matrix8[r][s]=eval(matrix8[r][s])
 print(addMatrix(matrix7,matrix8))
main()



#11.6







#11.30
def LinearEqn(a,b):
 if a[0][0]*a[1][1]-a[0][1]*a[1][0]==0:
  return "none"
 else :
  x=(b[0][0]*a[1][1]-b[1][0]*a[0][1])/(a[0][0]*a[1][1]-a[0][1]*a[1][0])
  y=(b[1][0] * a[0][0] - b[0][0] * a[1][0]) / (a[0][0] * a[1][1] - a[0][1] * a[1][0])
  return (x,y)

def main():
 a=[[0,0],[0,0]]
 a00,a01,a10,a11=eval(input("enter a00,a01,a10,a11"))
 a[0][0],a[0][1],a[1][0],a[1][1]=a00,a01,a10,a11
 b=[[0],[0]]
 b00,b10 = eval(input("enter b00,b10"))
 b[0][0], b[1][0] = b00,b10
 print("soln: ",LinearEqn(a,b))
main()




#11.31 error
def getIntersectingPoints(points):
 if (((points[2][1]-points[3][1])*(points[0][0]-points[1][0]))-(points[0][1]-points[1][1]*(points[2][0]-points[3][0])))==0:
  return("none")
 else:
  x=(((points[0][1]-points[1][1])*points[0][0]-(points[0][0]-points[1][0])*points[0][1])*(points[3][0]-points[2][0]))+((points[0][0]-points[1][0])*((points[2][1]-points[3][1])*points[2][0])-(points[2][0]-points[3][0])*points[2][1])/(((points[2][1]-points[3][1])*(points[0][0]-points[1][0]))-(points[0][1]-points[1][1]*(points[2][0]-points[3][0])))
  y=((((points[2][1]-points[3][1])*points[2][0]-(points[2][0]-points[3][0])*points[2][1])*(points[0][1]-points[1][1]))-((points[0][1]-points[1][1])*points[0][0]-(points[0][0]-points[1][0])*points[0][1])*(points[2][1]-points[3][1]))/(((points[2][1] - points[3][1]) * (points[0][0] - points[1][0])) - (points[0][1] - points[1][1] * (points[2][0] - points[3][0])))
  return (x,y)
def main():
 points=[]
 for i in range(0,4):
  point=2*[0]
  point[0],point[1]=eval(input("point?"))
  points.append(point)
 print("soln:",getIntersectingPoints(points))
main()



#11.32
def getTriangleArea(points):
 side1=((points[1][0]-points[0][0])**2+((points[1][1]-points[0][1])**2))**0.5
 side2=((points[2][0]-points[0][0])**2+((points[2][1]-points[0][1])**2))**0.5
 side3=((points[2][0]-points[1][0])**2+((points[2][1]-points[1][1])**2))**0.5
 s=(side1+side2+side3)/2
 area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
 return (area)

def main():
 points=[]
 for i in range(0,3):
  point=2*[0]
  point[0],point[1]=eval(input("point?"))
  points.append(point)
 print("area ", getTriangleArea(points))
main()




#11.33


#11.34 error

def getRightmostPoint(points):
 for j in range(1,len(points)):
  maxy=points[0][1]
  maxx=points[0][0]
  if abs(points[j][1])>abs(maxy):
     maxy = points[j][1]
     if abs(points[j][0])>maxx:
      maxx = points[j][0]
 return (maxx,maxy)
def main():
 points=[]
 for i in range(0,6):
  point=2*[0]
  point[0],point[1]=eval(input("point?"))
  points.append(point)
 print("rightmost point",getRightmostPoint(points))
main()







#11.42 erroe
from tkinter import *
import math
class Sine():
 def __init__(self):
  window=Tk()
  window.title("Sine")
  canvas1=Canvas(window,width=400,height=400)
  canvas1.pack()
  p=[]
  for x in range(-175,176):
   p.append([x,-50*math.sin((x/100)*2*math.pi)])
  canvas1.create_line(p)
  window.mainloop()
Sine()

from tkinter import *
import math
root = Tk()
root.title("Simple plot using canvas and line")
width = 400
height = 300
center = height//2
x_increment = 1
# width stretch
x_factor = 0.04
# height stretch
y_amplitude = 80
c = Canvas(width=width, height=height, bg='white')
c.pack()
str1 = "sin(x)=blue"
c.create_text(10, 20, anchor=SW, text=str1)
center_line = c.create_line(0, center, width, center, fill='green')
# create the coordinate list for the sin() curve, have to be integers
xy1 = []
for x in range(400):
 # x coordinates
 xy1.append(x * x_increment)
 # y coordinates
 xy1.append(int(math.sin(x * x_factor) * y_amplitude) + center)

sin_line = c.create_line(xy1, fill='blue')
root.mainloop()





















#11.46
from tkinter import *
class Stop():
 def __init__(self):
  window=Tk()
  window.title("Stop Sign")
  canvas1=Canvas(window,width=400,height=400)
  canvas1.pack()
  canvas1.create_polygon(0,110,25,10,125,10,150,110,125,210,25,210,fill="red")
  canvas1.create_text(75,110,text="STOP",font = "Times 40 bold", tags = "string")
  window.mainloop()
Stop()

#11.47

#11.48
from tkinter import *
class BoundingRectangle():
 def __init__(self):
  window=Tk()
  window.title("bounding rectangle")
  self.canvas3=Canvas(window,width=400,height=400)
  self.canvas3.pack()
  self.x = []
  self.y = []
  self.z=0
  self.canvas3.bind("<Button-1>",self.addCircle)
  self.canvas3.bind("<Button-3>", self.removeCircle)
  window.mainloop()
 def addCircle(self,event):
  self.z += 1
  self.canvas3.create_oval(event.x,event.y,event.x+10,event.y+10,tags="circ"+str(self.z))
  self.x.append(event.x)
  self.y.append(event.y)
  self.canvas3.delete("rect1")
  minx=min(self.x)
  miny=min(self.y)
  maxx=max(self.x)
  maxy=max(self.y)
  self.canvas3.create_rectangle(minx,miny,maxx+10,maxy+10, tags="rect1")
 def removeCircle(self,event):
  self.canvas3.delete("circ"+str(self.z))
  self.z-=1
  self.canvas3.delete("rect1")
  self.x.pop()
  self.y.pop()
  minx = min(self.x)
  miny = min(self.y)
  maxx = max(self.x)
  maxy = max(self.y)
  self.canvas3.create_rectangle(minx, miny, maxx + 10, maxy + 10, tags="rect1")
BoundingRectangle()


#11.49
from tkinter import *
import random
class TicTacToeboard():
 def __init__(self):
  window=Tk()
  window.title("Tic Tac Toe Board")
  self.frame1=Frame(window)
  self.frame1.pack()
  self.img1 = PhotoImage(file="images/yTo4Lq7jc.gif")
  self.img2 = PhotoImage(file="images/eiMeo4Lin.gif")
  Button(self.frame1, text="Refresh",command=self.refresh).grid(row=4,column=2)
  window.mainloop()
 def refresh(self):
  for i in range(1,4):
   for j in range(1,4):
    t=random.randint(0,1)
    if t==0:
     self.canvas4 = Canvas(self.frame1, width=100, height=100, bg="white")
     self.canvas4.grid(row=i,column=j)
     self.canvas4.create_image(i*10, j*10, image=self.img1,tags="img1")
    elif t==1:
     self.canvas4 = Canvas(self.frame1, width=100, height=100, bg="white")
     self.canvas4.grid(row=i, column=j)
     self.canvas4.create_image(i*10, j*10, image=self.img2,tags="img1")
TicTacToeboard()


#11.50
