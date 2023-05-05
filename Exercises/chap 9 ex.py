# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 06:15:25 2021

@author: kokeb
"""

#9.1
from tkinter import *
class Moveball():
    def __init__(self):
     window=Tk()
     window.title("Move the ball")
     self.c1=Canvas(window,width=400,height=400,bg="white")
     self.c1.pack()
     frame1=Frame(window)
     frame1.pack()
     self.x,self.y=10,10
     self.c1.create_oval(self.x, self.y, self.x+10, self.y+10, fill="red", tags="oval")
     Button(frame1,text="Left",command=self.goLeft).pack(side=LEFT)
     Button(frame1,text="Up",command=self.goUp).pack(side=LEFT)
     Button(frame1,text="Down",command=self.goDown).pack(side=LEFT)
     Button(frame1,text="Right",command=self.goRight).pack(side=LEFT)
     window.mainloop()
    def goLeft(self):
     if self.x>0:
      self.c1.delete("oval")
      self.x-=25
      self.c1.create_oval(self.x, self.y, self.x+10, self.y+10, fill="red", tags="oval")
     else:
      self.c1.delete("oval")
      self.c1.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="oval")
    def goUp(self):
     if self.y>0:
      self.c1.delete("oval")
      self.y-=25
      self.c1.create_oval(self.x, self.y, self.x+10, self.y+10, fill="red", tags="oval")
     else:
      self.c1.delete("oval")
      self.c1.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="oval")
    def goDown(self):
      if self.y<400:
       self.c1.delete("oval")
       self.y+=25
       self.c1.create_oval(self.x,self.y,self.x+10, self.y+10, fill="red", tags="oval")
      else:
       self.c1.delete("oval")
       self.c1.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="oval")
    def goRight(self):
     if self.x<400:
      self.c1.delete("oval")
      self.x+=25
      self.c1.create_oval(self.x, self.y, self.x+10, self.y+10, fill="red", tags="oval")
     else:
      self.c1.delete("oval")
      self.c1.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red", tags="oval")
Moveball()


#9.2
from tkinter import *
class investmentCalculator:
    def __init__(self):
     window=Tk()
     window.title("Investment Calculator")
     Label(window,text="Investment Amount").grid(row=1,column=1,sticky=W)
     Label(window,text="Years").grid(row=2,column=1,sticky=W)
     Label(window,text="Annual Interest Rate").grid(row=3,column=1,sticky=W)
     Label(window,text="Future Value").grid(row=4,column=1,sticky=W)
     self.investmentAmount=StringVar()
     Entry(window,textvariable=self.investmentAmount).grid(row=1,column=2)
     self.Years=StringVar()
     Entry(window,textvariable=self.Years).grid(row=2,column=2)
     self.annualInterestRate=StringVar()
     Entry(window,textvariable=self.annualInterestRate).grid(row=3,column=2)
     self.futureVar=StringVar()
     futureVar=Label(window,textvariable=self.futureVar).grid(row=4,column=2)
     Button(window,text="compute pay",command=self.computePay).grid(row=5,column=2,sticky=E)
     window.mainloop()
     
    def computePay(self):
        futureValue=float(self.investmentAmount.get())*((1+float(self.annualInterestRate.get())/1200)**(12*int(self.Years.get())))
        self.futureVar.set(format(futureValue,".2f")) 
investmentCalculator()   

#9.3 error on fill
from tkinter import *
class RecOrOval():
   def __init__(self): 
    window=Tk()
    window.title("Draw")
    self.canvas=Canvas(window,width=400,height=400,bg="white")
    self.canvas.pack()
    frame1=Frame(window).pack()
    self.var1=IntVar()
    rbRec=Radiobutton(frame1,text="Rectangle",variable=self.var1,value=1,command=self.drawStaff).pack(side=LEFT)
    rbOval=Radiobutton(frame1,text="Oval",variable=self.var1,value=2,command=self.drawStaff).pack(side=LEFT)
    self.var2=IntVar()
    cbt1=Checkbutton(frame1,text="Fill",variable=self.var2,command=self.fillStaff).pack(side=LEFT)
    window.mainloop()
   def drawStaff(self):
    if self.var1.get()==1:
       self.canvas.delete("oval")
       self.canvas.create_rectangle(10,10,100,100,tags="rect1")
    elif self.var1.get()==2:
       self.canvas.delete("rect1")
       self.canvas.create_oval(10,10,100,100,tags="oval")   
   def fillStaff(self):
       self.canvas.delete("rect1","oval")
       if self.var1.get()==1:
        self.canvas.create_rectangle(10,10,100,100,tags="rect1",fill="red")
       elif self.var1.get()==2:
        self.canvas.create_oval(10,10,100,100,tags="oval",fill="red")
RecOrOval()     



#9.4
from tkinter import *
class Recs():
   def __init__(self): 
    window=Tk()
    window.title("Russian nesting recs")
    self.canvas=Canvas(window,width=400,height=400,bg="white")
    self.canvas.pack()  
    j=10   
    for i in range (20,0,-1):
     self.canvas.create_rectangle(j,j,400-j,400-j)
     j+=10
    window.mainloop()
      
Recs()   
     
#9.5
from tkinter import *
class Checkboard():
   def __init__(self): 
    window=Tk()
    window.title("Checkboard")
    for i in range(1,9):
     for j in range (1,9):
      if i%2==0: 
        if j%2==0:   
         self.canvas=Canvas(window,width=20,height=20,bg="white").grid(row=i,column=j)
        else:
         self.canvas=Canvas(window,width=20,height=20,bg="black").grid(row=i,column=j)
      else: 
        if j%2==0:   
         self.canvas=Canvas(window,width=20,height=20,bg="black").grid(row=i,column=j)
        else:
         self.canvas=Canvas(window,width=20,height=20,bg="white").grid(row=i,column=j) 
    window.mainloop()  
Checkboard()    


#9.6
from tkinter import *
import random
class TicTacToe():
 def __init__(self):
  window=Tk()
  window.title("tictactoe")
  img1=PhotoImage(file="images/yTo4Lq7jc.gif")
  img2=PhotoImage(file="images/eiMeo4Lin.gif")
  frame1=Frame(window)
  frame1.pack()
  for k in range(1,4):
   for l in range(1,4):
      m=random.randint(0,1)
      if m==0:
       canvas1=Canvas(frame1)
       canvas1.create_image(k*10,l*10,image=img1)
       canvas1["width"] = 100
       canvas1["height"] = 100
       canvas1.grid(row=k,column=l)
      elif m==1:
       canvas1 = Canvas(frame1)
       canvas1.create_image(k*10,l*10,image=img2)
       canvas1["width"] = 100
       canvas1["height"] = 100
       canvas1.grid(row=k, column=l)
  window.mainloop()
TicTacToe()


#9.7
from tkinter import *
class Grid1():
   def __init__(self): 
    window=Tk()
    window.title("grid")
    self.can1=Canvas(window,width=200,height=200,bg="white")
    self.can1.pack()
    j=20
    for i in range(1,9):
     self.can1.create_line(10,j,100,j,fill="red")
     j+=10
    k=20
    for h in range (1,9):
     self.can1.create_line(k,10,k,100,fill="blue")    
     k+=10
    window.mainloop()     
Grid1()    


#9.8 not finished
from tkinter import *
class Cascade():
    def __init__(self):
        window=Tk()
        window.title("Pyramid")
        self.canvas2=Canvas(window,width=1000,height=1000,bg="white")
        self.canvas2.pack()
        x=100
        y=10
        for i in range (1,10):
         x=100-y/2   
         for j in range(1,i):   
          self.canvas2.create_text(x,y,text=str(j))
          x+=10
         y+=10 
        window.mainloop()
Cascade()
        
#9.9
from tkinter import *
class BarChart():
    def __init__(self):
        window=Tk()
        window.title("Bar Chart")
        self.canvas3=Canvas(window,width=500,height=500,bg="white")
        self.canvas3.pack()
        self.canvas3.create_rectangle(10,300,30,500,fill="red")
        self.canvas3.create_text(10,290,text="Project")
        self.canvas3.create_rectangle(40,400,60,500,fill="blue")
        self.canvas3.create_text(40,390,text="Quiz")
        self.canvas3.create_rectangle(70,200,90,500,fill="green")
        self.canvas3.create_text(70,190,text="Midterm")   
        self.canvas3.create_rectangle(100,100,120,500,fill="orange")
        self.canvas3.create_text(100,90,text="Final") 
        window.mainloop()
BarChart()  

#9.10
from tkinter import *
class PieChart():
 def __init__(self):
   window=Tk()
   window.title("pie Chart")
   self.canvas4=Canvas(window,width=400,height=400)
   self.canvas4.pack()
   self.canvas4.create_arc(10,10,200,100,start=0,extent=72,fill="red")
   self.canvas4.create_arc(10,10,200,100,start=72,extent=36,fill="blue")
   self.canvas4.create_arc(10,10,200,100,start=108,extent=108,fill="green")
   self.canvas4.create_arc(10,10,200,100,start=216,extent=144,fill="orange")
   window.mainloop()
PieChart()   

#9.11 error
import time
import math
from tkinter import *
class CurrentTime():
  def __init__(self):
      window=Tk()
      window.title("Time")
      self.canvas5=Canvas(window,width=400,height=400)
      self.canvas5.pack()
      self.canvas5.create_oval(10,10,200,200,fill="white")
      self.setTime()
      window.mainloop()
      
  def getTime(self):
      allSeconds=time.time()
      currentSecond=allSeconds%60
      allMinutes=allSeconds//60
      currentMinute=allMinutes%60
      allhours=allMinutes//24
      currentHour=allhours%24
      return (currentHour,currentMinute,currentSecond)
  def setTime(self):
      currentHour=getTime()
      if currentHour==3:
          self.canvas5.create_line(100,100,200,100)
      else:
          self.canvas5.create_line(100,100,200-100*math.cos(currentHour*30),100+100*math.sin(currentHour*30))
CurrentTime()    

#9.12 
from tkinter import *
class Rotating():
    def __init__(self):
        window=Tk()
        window.title("Rotating Message")
        self.canvas6=Canvas(window,width=400,height=400,bg="white")
        self.canvas6.pack()
        self.canvas6.create_text(100, 100,text="programming is fun",tags="text1")
        self.j=0
        self.canvas6.bind("<Button-1>",self.messages)
        window.mainloop()

    def messages(self,event):
      if self.j %2==0:
       self.canvas6.delete("text1","text2")
       self.canvas6.create_text(event.x, event.y,text="It is fun to program",tags="text1")
      elif self.j %2 != 0:
       self.canvas6.delete("text1","text2")
       self.canvas6.create_text(event.x,event.y,text="programming is fun",tags="text2")
      self.j+=1
Rotating()

#9.13
from tkinter import *
class Position(): 
    def __init__(self):
     window=Tk()
     window.title("position")
     self.canvas7=Canvas(window,width=400,height=400,bg="white")
     self.canvas7.pack()
     self.canvas7.bind("<Button-1>",self.positionFinder)
     window.mainloop() 
    def positionFinder(self,event):
      self.canvas7.delete("text")  
      self.canvas7.create_text(event.x,event.y,text=event.x,tags="text")
      self.canvas7.create_text(event.x_root, event.y_root,text=event.y, tags="text")
Position()

#9.14 error
from tkinter import *
class Keys():
  def __init__(self):
        window=Tk()
        window.title("maze")
        self.canvas8=Canvas(window,width=400,height=400,bg="white")
        self.canvas8.pack()
        self.i, self.j = 100, 100
        self.dx,self.dy=50,50
        self.canvas8.create_line(self.i,self.j,self.i+self.dx,self.j)
        self.i, self.j =self.i+self.dx,self.j
        self.canvas8.bind("<Left>",self.goLeft)
        self.canvas8.bind("<Down>", self.goDown)
        self.canvas8.bind("<Right>",self.goRight)
        self.canvas8.bind("<Up>", self.goUp)
        self.canvas8.focus_set()
        window.mainloop()
  def goLeft(self,event):
        self.canvas8.create_line(self.i,self.j,self.i-self.dx,self.j)
        self.i, self.j = self.i-self.dx, self.j
  def goDown(self,event):
       self.canvas8.create_line(self.i,self.j,self.i,self.j+self.dy)
       self.i, self.j = self.i, self.j+2*self.dy
  def goRight(self, event):
        self.canvas8.create_line(self.i, self.j, self.i+self.dx, self.j)
        self.i, self.j = self.i+2*self.dx, self.j
  def goUp(self, event):
        self.canvas8.create_line(self.i, self.j, self.i, self.j-self.dy)
        self.i, self.j = self.i, self.j-self.dy
Keys()

#9.15
from tkinter import *
class stillFan():
    def __init__(self):
        window=Tk()
        window.title("fan")
        canvas9=Canvas(window,width=400,height=400,bg="white")
        canvas9.pack()
        canvas9.create_arc(10,10,200,200,start=0,extent=30,fill="black")
        canvas9.create_arc(10, 10, 200, 200,start=30, extent=60, fill="white")
        canvas9.create_arc(10, 10, 200, 200, start=90, extent=30, fill="black")
        canvas9.create_arc(10, 10, 200, 200, start=120, extent=60, fill="white")
        canvas9.create_arc(10, 10, 200, 200, start=180, extent=30, fill="black")
        canvas9.create_arc(10, 10, 200, 200, start=210, extent=60, fill="white")
        canvas9.create_arc(10, 10, 200, 200, start=270, extent=30, fill="black")
        canvas9.create_arc(10, 10, 200, 200, start=300, extent=60, fill="white")
        window.mainloop()
stillFan()

#9.16






#9.18
from tkinter import *
import random
class FlashingText():
 def __init__(self):
  window=Tk()
  window.title("Flashing Text")
  frame1=Frame(window)
  frame1.pack()
  canvas11=Canvas(window,width=400,height=400,bg="white")
  canvas11.pack()
  while True:
   x=random.randint(0,400)
   y=random.randint(0,400)
   canvas11.create_text(x,y,text="Welcome",tags="text")
   canvas11.move("text",x,y)
   canvas11.after(100)
   canvas11.update()
   canvas11.delete("text")
   canvas11.create_text(x, y, text="Welcome", tags="text")
  window.mainloop()
FlashingText()



#9.19
from tkinter import *
class MovingCircle():
 def __init__(self):
  window=Tk()
  window.title("Moving Circle")
  frame1=Frame(window)
  frame1.pack()
  self.canvas12=Canvas(window,width=400,height=400,bg="white")
  self.canvas12.pack()
  self.canvas12.create_oval(20,20,40,40,tag="circle")
  self.x,self.y=20,20
  self.canvas12.bind("<Up>",self.goUp)
  self.canvas12.bind("<Down>", self.goDown)
  self.canvas12.bind("<Left>", self.goLeft)
  self.canvas12.bind("<Right>", self.goRight)
  self.canvas12.focus_set()
  window.mainloop()
 def goUp(self,event):
  self.canvas12.delete("circle")
  self.y-=50
  self.canvas12.create_oval(self.x, self.y, self.x+20, self.y+20, tag="circle")
 def goDown(self,event):
  self.canvas12.delete("circle")
  self.y+=50
  self.canvas12.create_oval(self.x, self.y, self.x+20, self.y+20, tag="circle")
 def goLeft(self,event):
  self.canvas12.delete("circle")
  self.x-=50
  self.canvas12.create_oval(self.x, self.y, self.x+20, self.y+20, tag="circle")
 def goRight(self,event):
  self.canvas12.delete("circle")
  self.x+=50
  self.canvas12.create_oval(self.x, self.y, self.x+20, self.y+20, tag="circle")
MovingCircle()




#9.20
from tkinter import *
class InsideCircle():
 def __init__(self):
  window=Tk()
  window.title("Inside or Outside")
  frame1=Frame(window)
  frame1.pack()
  self.canvas13=Canvas(window,width=400,height=400,bg="white")
  self.canvas13.pack()
  self.canvas13.create_oval(100,60,150,110,tags="circle")
  self.canvas13.bind("<B1-Motion>",self.inOrOut)
  window.mainloop()
 def inOrOut(self,event):
  x=event.x
  y=event.y
  if 100<=x<=150 and 60<=y<=110:
   self.canvas13.delete("text")
   self.canvas13.create_text(x,y,text="Inside",tags="text")
  else:
   self.canvas13.delete("text")
   self.canvas13.create_text(x,y,text="Outside",tags="text")
InsideCircle()



#9.21
from tkinter import *
class InsideRectangle():
 def __init__(self):
  window=Tk()
  window.title("Inside or Outside")
  frame1=Frame(window)
  frame1.pack()
  self.canvas13=Canvas(window,width=400,height=400,bg="white")
  self.canvas13.pack()
  self.canvas13.create_rectangle(100,60,200,100,tags="rec")
  self.canvas13.bind("<B1-Motion>",self.inOrOut)
  window.mainloop()
 def inOrOut(self,event):
  x=event.x
  y=event.y
  if 100<=x<=200 and 60<=y<=100:
   self.canvas13.delete("text")
   self.canvas13.create_text(x,y,text="Inside",tags="text")
  else:
   self.canvas13.delete("text")
   self.canvas13.create_text(x,y,text="Outside",tags="text")
InsideRectangle()


#9.22 small errors
from tkinter import *
class Pendulum():
 def __init__(self):
  window=Tk()
  window.title("pendulum")
  self.canvas14=Canvas(window,width=400,height=400,bg="white")
  self.canvas14.pack()
  x,y=100,100
  self.canvas14.create_line(100,10,x,y,tags="line")
  self.canvas14.create_oval(90,90,110,110,fill="black",tags="ball")
  self.dx=100
  self.isStopped=False
  #self.animate()
  while True:
   if x<200:
    self.canvas14.delete("line")
    self.canvas14.delete("ball")
    x+=10
    y-=10
    self.canvas14.create_line(100, 10, x, y, tags="line")
    self.canvas14.create_oval(x-10, y-10, x+10, y+10, fill="black", tags="ball")
    self.canvas14.after(self.dx)
    self.canvas14.update()
   elif x ==200 and y==0:
    while x>=100:
     self.canvas14.delete("line")
     self.canvas14.delete("ball")
     x-=10
     y+=10
     self.canvas14.create_line(100, 10, x, y, tags="line")
     self.canvas14.create_oval(x-10,y-10,x+10,y+10,fill="black",tags="ball")
     self.canvas14.after(self.dx)
     self.canvas14.update()
  self.canvas14.bind("<Up>",self.speedUp)
  self.canvas14.bind("<Down>", self.speedDown)
  self.canvas14.bind("<S>", self.stop)
  #self.canvas14.bind("<R>", self.resume)
  self.canvas14.focus_set()
  window.mainloop()
 def speedUp(self,event):
   self.dx-=500
 def speedDown(self,event):
   self.dx+=500
 def stop(self,event):
   self.isStopped=True
 '''def resume(self,event):
   self.isStopped=True'''
Pendulum()



#9.23
from tkinter import *
class RadioButtons():
 def __init__(self):
  window=Tk()
  window.title("Radio buttons and Buttons")
  frame1=Frame(window)
  frame1.pack()
  self.x,self.y=100,100
  self.v1=StringVar()
  rbRed = Radiobutton(frame1, text="Red", bg="white", variable=self.v1, value='R', command=self.changeColor).pack(side=LEFT)
  rbYellow = Radiobutton(frame1, text="Yellow", bg="white", variable=self.v1, value='Y', command=self.changeColor).pack(side=LEFT)
  rbWhite = Radiobutton(frame1, text="White", bg="white", variable=self.v1, value='W', command=self.changeColor).pack(side=LEFT)
  rbRed = Radiobutton(frame1, text="Gray", bg="white", variable=self.v1, value='A', command=self.changeColor).pack(side=LEFT)
  rbGreen = Radiobutton(frame1, text="Green", bg="white", variable=self.v1, value='G', command=self.changeColor).pack(side=LEFT)
  self.canvas15=Canvas(frame1,width=400,height=400)
  self.canvas15.pack()
  self.canvas15.create_text(self.x,self.y,text="Welcome",fill="black",tags="text1")
  frame2=Frame(window)
  frame2.pack()
  btLeft=Button(frame2,text="<=",command=self.goLeft).pack(side=LEFT)
  btRight=Button(frame2,text="=>", command=self.goRight).pack(side=LEFT)
  window.mainloop()
 def changeColor(self):
  if self.v1.get()=='R':
   self.canvas15.delete("text1")
   self.canvas15.create_text(self.x,self.y, text="Welcome", fill="red", tags="text1")
  elif self.v1.get() == 'Y':
      self.canvas15.delete("text1")
      self.canvas15.create_text(self.x,self.y, text="Welcome", fill="yellow", tags="text1")
  elif self.v1.get() == 'W':
      self.canvas15.delete("text1")
      self.canvas15.create_text(self.x,self.y, text="Welcome", fill="white", tags="text1")
  elif self.v1.get() == 'G':
      self.canvas15.delete("text1")
      self.canvas15.create_text(self.x,self.y, text="Welcome", fill="green", tags="text1")
  elif self.v1.get() == 'A':
      self.canvas15.delete("text1")
      self.canvas15.create_text(self.x,self.y, text="Welcome", fill="gray", tags="text1")
 def goLeft(self):
     self.canvas15.delete("text1")
     self.x-=20
     self.canvas15.create_text(self.x,self.y,text="Welcome", tags="text1")
 def goRight(self):
     self.canvas15.delete("text1")
     self.x+=20
     self.canvas15.create_text(self.x,self.y,text="Welcome", tags="text1")
RadioButtons()


#9.24
from tkinter import *
class DynamicCircle():
 def __init__(self):
  window=Tk()
  window.title("Dynamic Circle")
  self.x,self.y=400,400
  self.dx=25
  self.label1=1
  self.name="circle"+str(self.label1)
  self.canvas16=Canvas(window,width=800,height=800)
  self.canvas16.pack()
  self.canvas16.create_oval(self.x-self.dx,self.y-self.dx,self.x+self.dx,self.y+self.dx,tags=self.name)
  self.canvas16.bind("<Button-1>",self.enlarge)
  self.canvas16.bind("<Button-3>",self.reduce)
  window.mainloop()
 def enlarge(self,event):
  self.dx+=25
  self.label1+=1
  self.name="circle"+str(self.label1)
  self.canvas16.create_oval(self.x-self.dx,self.y-self.dx,self.x+self.dx,self.y+self.dx,tags=self.name)
 def reduce(self,event):
  self.label1 -= 1
  self.name="circle"+str(self.label1)
  self.canvas16.delete(self.name)
DynamicCircle()



#9.25
from tkinter import *
class TrafficLights():
 def __init__(self):
  window=Tk()
  window.title("Traffic Lights")
  frame1 = Frame(window)
  frame1.pack()
  self.canvas17=Canvas(frame1,width=400,height=400)
  self.canvas17.pack()
  self.canvas17.create_rectangle(100,10,150,160,tags="rect")
  self.canvas17.create_oval(100, 10, 150,60, tags="circ1")
  self.canvas17.create_oval(100, 60, 150, 110, tags="circ2")
  self.canvas17.create_oval(100, 110, 150, 160, tags="circ3")
  self.var1=StringVar()
  rbRed=Radiobutton(frame1,text="Red", bg="white", variable=self.var1, value='R', command=self.changeColor).pack(side=LEFT)
  rbYellow=Radiobutton(frame1,text="Yellow", bg="white", variable=self.var1,value='Y',command=self.changeColor).pack(side=LEFT)
  rbGreen=Radiobutton(frame1, text="Green", bg="white",variable=self.var1, value='G', command=self.changeColor).pack(side=LEFT)
  window.mainloop()
 def changeColor(self):
  if self.var1.get() == 'R':
   self.canvas17.delete("circ1","circ2","circ3")
   self.canvas17.create_oval(100, 10, 150, 60,fill="red", tags="circ1")
   self.canvas17.create_oval(100, 60, 150, 110, tags="circ2")
   self.canvas17.create_oval(100, 110, 150, 160, tags="circ3")
  elif self.var1.get() == 'Y':
   self.canvas17.delete("circ1","circ2","circ3")
   self.canvas17.create_oval(100, 10, 150, 60, tags="circ1")
   self.canvas17.create_oval(100, 60, 150, 110,fill="yellow", tags="circ2")
   self.canvas17.create_oval(100, 110, 150, 160, tags="circ3")
  elif self.var1.get() == 'G':
   self.canvas17.delete("circ1","circ2","circ3")
   self.canvas17.create_oval(100, 10, 150, 60, tags="circ1")
   self.canvas17.create_oval(100, 60, 150, 110, tags="circ2")
   self.canvas17.create_oval(100, 110, 150, 160,fill="green", tags="circ3")
TrafficLights()



#9.26
from tkinter import *
import random
class RandomBalls():
 def __init__(self):
  window=Tk()
  window.title("Random Balls")
  frame1 = Frame(window)
  frame1.pack()
  self.canvas18=Canvas(frame1,width=400,height=400)
  self.canvas18.pack()
  btDisplay = Button(frame1, text="Display", command=self.display).pack()
  window.mainloop()
 def display(self):
   colors=["red","yellow","white","black","purple","green","gray","blue"]
   for i in range (1,11):
     x=random.randint(0,400)
     y=random.randint(0,400)
     c=random.randint(0,8)
     self.canvas18.create_oval(x,y,x+10,y+10,fill=colors[c])
RandomBalls()



#9.27
from tkinter import *
class CompareInterest():
 def __init__(self):
  window=Tk()
  window.title("compare interest rate")
  frame1=Frame(window)
  frame1.pack()
  self.canvas19=Canvas(window,height=700,width=500)
  self.canvas19.pack()
  Label(frame1,text="Loan Amount").pack(side=LEFT)
  self.loanVar=StringVar()
  Entry(frame1,textvariable=self.loanVar).pack(side=LEFT)
  Label(frame1,text="Years").pack(side=LEFT)
  self.years=StringVar()
  Entry(frame1,textvariable=self.years).pack(side=LEFT)
  btCalculate = Button(frame1,text="Calculate", command=self.computeInterest).pack(side=LEFT)
  window.mainloop()
 def computeInterest(self):
  j=20
  i=5
  while i<=8:
   monthlyPayment = float(self.loanVar.get()) * i/1200 / (1-1/(1 + i/1200)**(int(self.years.get()) * 12))
   totalPayment = float(monthlyPayment)*12*int(self.years.get())
   format(monthlyPayment, "10.2f")
   format(totalPayment, "10.2f")
   self.canvas19.create_text(125,10,text="Interest         Monthly Pay         Total Pay")
   self.canvas19.create_text(20,j, text=str(i))
   self.canvas19.create_text(100,j, text=format((monthlyPayment),".2f"))
   self.canvas19.create_text(200, j, text=format((totalPayment),".2f"))
   j+=20
   i=i+(1/8)
CompareInterest()




#9.28















#9.30
import tkinter
class Rectangoid():
 def __init__(self):
  window=Tk()
  window.title("rectangoid")
  canvas20=Canvas(window,height=500,width=500)
  canvas20.pack()
  canvas20.create_rectangle(100,100,300,200)
  canvas20.create_rectangle(120,80,320,180)
  canvas20.create_line(100,100,120,80)
  canvas20.create_line(100,200,120,180)
  canvas20.create_line(300,100,320,80)
  canvas20.create_line(300,200,320,180)
  window.mainloop()
Rectangoid()


#9.31






#9.32
from tkinter import *
class CircleLine():
 def __init__(self):
  window=Tk()
  window.title("two circles")
  self.canvas10=Canvas(window,width=400,height=400)
  self.canvas10.pack()
  self.c1x,self.c1y=20,20
  self.c2x,self.c2y=120,50
  self.distance=((self.c1x-self.c2x)**2+(self.c1y-self.c2y)**2)**0.5
  self.canvas10.create_oval(self.c1x-15,self.c1y-15,self.c1x+15,self.c1y+15,fill='purple',tags="oval1")
  self.canvas10.create_oval(self.c2x-15,self.c2y-15,self.c2x+15,self.c2y+15,fill='purple',tags="oval2")
  self.canvas10.create_line(self.c1x,self.c1y,self.c2x,self.c2y,tags="line")
  self.canvas10.bind("<B1-Motion>",self.processEvent)
  self.canvas10.create_text((self.c1x+self.c2x)/2,(self.c1y+self.c2y)/2,text=format(self.distance,".2f"),tags="text")
  window.mainloop()
 def processEvent(self,event):
  x=event.x
  y=event.y
  if self.distance>=70:
   self.canvas10.delete("oval2", "text", "line")
   self.canvas10.create_oval(x-15,y-15,x+15,y+15,fill='purple',tags="oval2")
   self.distance=((self.c1x-x)**2+(self.c1y-y)**2)**0.5
   self.canvas10.create_line(self.c1x, self.c1y,x,y, tags="line")
   self.canvas10.create_text((self.c1x+x)/2,(self.c1y+y)/2,text=format(self.distance,".2f"), tags="text")
  else:
   self.canvas10.delete("text")
   self.canvas10.create_text((self.c1x + x) / 2, (self.c1y + y)/2,text="too close",tags="text")
CircleLine()



#9.33
from tkinter import *
import random
class RandomArrows():
 def __init__(self):
  window=Tk()
  window.title("random arrow")
  frame1=Frame(window)
  frame1.pack()
  self.canvas11=Canvas(frame1,height=400,width=400,bg="white")
  self.canvas11.pack()
  x = random.randint(0, 400)
  y = random.randint(0, 400)
  z, a = x + 100, y + 100
  self.canvas11.create_line(x, y, z, a, tags="arrow")
  self.canvas11.create_polygon(z, a, z, a + 20, z + 20, a, z, a - 20, fill="black", tags="arrow")
  btArrow=Button(frame1,text="Draw Random Arrow",command=self.RandomArrow).pack()
  window.mainloop()
 def RandomArrow(self):
  self.canvas11.delete("arrow")
  x=random.randint(0,400)
  y=random.randint(0,400)
  z,a=x+100,y+100
  self.canvas11.create_line(x,y,z,a,tags="arrow")
  self.canvas11.create_polygon(z,a,z,a+5,z+10,a,z,a-5,fill="black",tags="arrow")
RandomArrows()









#9.34
from tkinter import *
class AddressBook():
 def __init__(self):
  window=Tk()
  window.title("Address Book")
  lblName = Label(window, text="Name").grid(row=1, column=1)
  lblStreet = Label(window, text="StreetName").grid(row=2,column=1)
  lblCity = Label(window, text="City").grid(row=3, column=1)
  lblState = Label(window, text="State").grid(row=3, column=3)
  lblZIP = Label(window, text="ZIP").grid(row=3, column=5)
  self.Name = StringVar()
  Entry(window, text=self.Name, justify=RIGHT).grid(row=1, column=2, sticky=E)
  self.StreetName = StringVar()
  Entry(window, textvariable=self.StreetName, justify=RIGHT).grid(row=2,column=2,sticky=E)
  self.City = StringVar()
  Entry(window, textvariable=self.City, justify=RIGHT).grid(row=3,column=2,sticky=E)
  self.State = StringVar()
  Entry(window, textvariable=self.State, justify=RIGHT).grid(row=3,column=4,sticky=E)
  self.ZIP = StringVar()
  Entry(window, textvariable=self.ZIP, justify=RIGHT).grid(row=3,column=6,sticky=E)
  self.lst1=[]
  self.lst2=[]
  btAdd=Button(window, text = "Add",command = self.Add).grid(row=4,column=2,sticky=E)
  btFirst=Button(window, text="First", command=self.First).grid(row=4,column=3,sticky=E)
  btNext=Button(window,text="Next",command=self.Next).grid(row=4,column=4,sticky=E)
  btPrevious=Button(window, text="Previous",command=self.Previous).grid(row=4, column=5, sticky=E)
  btLast = Button(window,text="Last",command=self.Last).grid(row=4, column=6,sticky=E)
  window.mainloop()
 def Add(self):
  self.lst1=[self.Name.get(),self.StreetName.get(),self.City.get(),self.State.get(),self.ZIP.get()]
  self.lst2.append(self.lst1)
 def First(self):
  self.Name.set(self.lst2[0][0])
  self.StreetName.set(self.lst2[0][1])
  self.City.set(self.lst2[0][2])
  self.State.set(self.lst2[0][3])
  self.ZIP.set(self.lst2[0][4])
 def Next(self):
  i=[self.Name.get(),self.StreetName.get(),self.City.get(),self.State.get(),self.ZIP.get()]
  j=self.lst2.index(i)+1
  if j < len(self.lst2):
   self.Name.set(self.lst2[j][0])
   self.StreetName.set(self.lst2[j][1])
   self.City.set(self.lst2[j][2])
   self.State.set(self.lst2[j][3])
   self.ZIP.set(self.lst2[j][4])
 def Previous(self):
  i=[self.Name.get(),self.StreetName.get(),self.City.get(),self.State.get(),self.ZIP.get()]
  j=self.lst2.index(i)-1
  if j >=0:
   self.Name.set(self.lst2[j][0])
   self.StreetName.set(self.lst2[j][1])
   self.City.set(self.lst2[j][2])
   self.State.set(self.lst2[j][3])
   self.ZIP.set(self.lst2[j][4])
 def Last(self):
  self.Name.set(self.lst2[len(self.lst2)-1][0])
  self.StreetName.set(self.lst2[len(self.lst2)-1][1])
  self.City.set(self.lst2[len(self.lst2)-1][2])
  self.State.set(self.lst2[len(self.lst2)-1][3])
  self.ZIP.set(self.lst2[len(self.lst2)-1][4])
AddressBook()