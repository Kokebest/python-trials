# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 05:45:37 2021

@author: kokeb
"""

from tkinter import * # Import all definitions from tkinter

window = Tk() # Create a window
label = Label(window, text = "Welcome to Python") # Create a label
button = Button(window, text = "Click Me") # Create a button
label.pack() # Place the label in the window
button.pack() # Place the button in the window

window.mainloop() # Create an event loop



from tkinter import *

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")
window = Tk() # Create a window
btOK = Button(window, text = "OK", fg = "red", command = processOK)
btCancel = Button(window, text = "Cancel", bg = "yellow",
command = processCancel)
btOK.pack() # Place the OK button in the window
btCancel.pack()


window.mainloop()



from tkinter import *
class WidgetsDemo:
  def __init__(self):
    window = Tk() # Create a window
    window.title("Widgets Demo") # Set a title

    # Add a check button, and a radio button to frame1
    frame1 = Frame(window) # Create and add a frame to window
    frame1.pack()
    self.v1 = IntVar()
    cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, command = self.processCheckbutton)
    self.v2 = IntVar()
    rbRed = Radiobutton(frame1, text = "Red", bg = "red", variable = self.v2, value = 1,command = self.processRadiobutton)
    rbYellow = Radiobutton(frame1, text = "Yellow",bg = "yellow", variable = self.v2, value = 2, command = self.processRadiobutton)
    cbtBold.grid(row = 1, column = 1)
    rbRed.grid(row = 1, column = 2)
    rbYellow.grid(row = 1, column = 3)
    
    # Add a label, an entry, a button, and a message to frame1
    frame2 = Frame(window) # Create and add a frame to window
    frame2.pack()
    label = Label(frame2, text = "Enter your name: ")
    self.name = StringVar()
    entryName = Entry(frame2,textvariable = self.name )
    btGetName = Button(frame2, text = "Get Name",
    command = self.processButton)
    message = Message(frame2, text = "It is a widgets demo")
    label.grid(row = 1, column = 1)
    entryName.grid(row = 1, column = 2)
    btGetName.grid(row = 1, column = 3)
    message.grid(row = 1, column = 4)
    
    # Add text
    text = Text(window) # Create and add text to the window
    text.pack()
    text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
    text.insert(END, "these carefully designed examples and use them ")
    text.insert(END, "to create your applications.")
    
    window.mainloop() # Create an event loop
    
  def processCheckbutton(self):
     print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))
    
  def processRadiobutton(self):
     print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected " )
    
  def processButton(self):
     print("Your name is " + self.name.get())
    
WidgetsDemo() # Create GUI




from tkinter import * # Import all definitions from tkinter

class ChangeLabelDemo:
 def __init__(self):
    window = Tk() # Create a window
    window.title("Change Label Demo") # Set a title
    
    # Add a label to frame1
    frame1 = Frame(window) # Create and add a frame to win
    frame1.pack()
    self.lbl = Label(frame1, text = "Programming is fun")
    self.lbl.pack()
    # Add a label, entry, button, two radio buttons to frame2
    frame2 = Frame(window) # Create and add a frame to window
    frame2.pack()
    label = Label(frame2, text = "Enter text: ")
    self.msg = StringVar()
    entry = Entry(frame2, textvariable = self.msg)
    btChangeText = Button(frame2, text = "Change Text",
    command = self.processButton)
    self.v1 = StringVar()
    rbRed = Radiobutton(frame2, text = "Red", bg = "red",
    variable = self.v1, value = 'R',
    command = self.processRadiobutton)
    rbYellow = Radiobutton(frame2, text = "Yellow",
    bg = "yellow", variable = self.v1, value = 'Y',
    command = self.processRadiobutton)
    
    label.grid(row = 1, column = 1)
    entry.grid(row = 1, column = 2)
    btChangeText.grid(row = 1, column = 3)
    rbRed.grid(row = 1, column = 4)
    rbYellow.grid(row = 1, column = 5)

    window.mainloop()
 def processRadiobutton(self): 
     if self.v1.get() == 'R':
      self.lbl["fg"] = "red"   
     elif self.v1.get() == 'Y':
      self.lbl["fg"] = "yellow"
 def processButton(self):
    self.lbl["text"] = self.msg.get()
 # New text for the label

ChangeLabelDemo() # Create GUI

 

LEFT=3
print(LEFT)



from tkinter import * # Import all definitions from tkinter

class CanvasDemo:
 def __init__(self):
    window = Tk() # Create a window
    window.title("Canvas Demo") # Set title
  
  # Place canvas in the window
    self.canvas = Canvas(window, width = 200, height = 100,bg = "white") 
    self.canvas.pack()

  # Place buttons in frame
    frame = Frame(window)
    frame.pack()
    btRectangle = Button(frame, text = "Rectangle", command = self.displayRect)
    btOval = Button(frame, text = "Oval", command = self.displayOval)
    btArc = Button(frame, text = "Arc", command = self.displayArc)
    btPolygon = Button(frame, text = "Polygon", command = self.displayPolygon)
    btLine = Button(frame, text = "Line", command = self.displayLine)
    btString = Button(frame, text = "String", command = self.displayString)
    btClear = Button(frame, text = "Clear",  command = self.clearCanvas)
    btRectangle.grid(row = 1, column = 1)
    btOval.grid(row = 1, column = 2)
    btArc.grid(row = 1, column = 3)
    btPolygon.grid(row = 1, column = 4)
    btLine.grid(row = 1, column = 5)
    btString.grid(row = 1, column = 6)
    btClear.grid(row = 1, column = 7)
    
    window.mainloop() # Create an event loop
 def displayRect(self):
       self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

   # Display an oval
 def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "oval")


   # Display an arc
 def displayArc(self):
      self.canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", tags = "arc")
           

 # Display a polygon
 def displayPolygon(self):
     self.canvas.create_polygon(10, 10, 190, 90, 30, 50,tags = "polygon")

# Display a line
 def displayLine(self):
      self.canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line") 
      self.canvas.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue", tags = "line") 
    
 def displayString(self):
      self.canvas.create_text(60, 40, text = "Hi, I am a string",font = "Times 10 bold underline", tags = "string")

 # Clear drawings
 def clearCanvas(self):
      self.canvas.delete("rect", "oval", "arc", "polygon","line", "string")
CanvasDemo() # Create GUI






from tkinter import * # Import all definitions from tkinter
class LoanCalculator:
 def __init__(self):
  window = Tk() # Create a window
  window.title("Loan Calculator") # Set title

  Label(window, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W)
  Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
  Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
  Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
  Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = W)

  self.annualInterestRateVar = StringVar()
  Entry(window, textvariable = self.annualInterestRateVar,justify = RIGHT).grid(row = 1, column = 2)
  self.numberOfYearsVar = StringVar()
  Entry(window, textvariable = self.numberOfYearsVar,justify = RIGHT).grid(row = 2, column = 2)
  self.loanAmountVar = StringVar()
  Entry(window, textvariable = self.loanAmountVar,justify = RIGHT).grid(row = 3, column = 2)
  self.monthlyPaymentVar = StringVar()
  lblMonthlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)
  self.totalPaymentVar = StringVar()
  lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)
  btComputePayment = Button(window, text = "Compute Payment",command = self.computePayment).grid(row = 6, column = 2, sticky = E)
  window.mainloop() # Create an event loop


 def computePayment(self):
   monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()) / 1200,
    int(self.numberOfYearsVar.get()))
   self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
   totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
   self.totalPaymentVar.set(format(totalPayment, "10.2f"))
 def getMonthlyPayment(self,loanAmount, monthlyInterestRate, numberOfYears):
   monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
   return monthlyPayment;
LoanCalculator() # Create GUI


from tkinter import *
class Images():
 def __init__(self):
     window=Tk()
     window.title("this")
     image1=PhotoImage(file="images/yTo4Lq7jc.gif")
     image2=PhotoImage(file="images/eiMeo4Lin.gif")
     frame1=Frame(window)
     frame1.pack()
     Button(frame1,image=image1).pack(side=LEFT)
     canvas1 = Canvas(frame1)
     canvas1.create_image(90,50,image=image2)
     canvas1["width"]=200
     canvas1["height"] = 200
     canvas1.pack(side=LEFT)
     window.mainloop()
Images()



from tkinter import *
class MenuDemo:
 def __init__(self):
  window = Tk()
  window.title("Menu Demo")
  menubar = Menu(window)
  window.config(menu = menubar)
  operationMenu = Menu(menubar, tearoff = 0)
  menubar.add_cascade(label = "Operation", menu = operationMenu)
  operationMenu.add_command(label = "Add",command = self.add)
  operationMenu.add_command(label = "Subtract", command = self.subtract)
  operationMenu.add_separator()
  operationMenu.add_command(label = "Multiply", command = self.multiply)
  operationMenu.add_command(label = "Divide", command = self.divide)
  exitmenu = Menu(menubar, tearoff = 0)
  menubar.add_cascade(label = "Exit", menu = exitmenu)
  exitmenu.add_command(label = "Quit", command = window.quit)
  frame0 = Frame(window)
  frame0.grid(row = 1, column = 1, sticky = W)
  mainloop()
 def add(self):
     self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))

 def subtract(self):
  self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))

 def multiply(self):
  self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))

 def divide(self):
  self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))

MenuDemo()  





from tkinter import * # Import all definitions from tkinter
class PopupMenuDemo:
 def __init__(self):
  window = Tk() # Create a window
  window.title("Popup Menu Demo")
  self.menu = Menu(window, tearoff = 0)
  self.menu.add_command(label = "Draw a line", command = self.displayLine)
  self.menu.add_command(label = "Draw an oval",command = self.displayOval)
  self.menu.add_command(label = "Draw a rectangle",command = self.displayRect)
  self.menu.add_command(label = "Clear", command = self.clearCanvas)

 # Place canvas in window
  self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
  self.canvas.pack()

 # Bind popup to canvas
  self.canvas.bind("<Button-3>", self.popup)
  window.mainloop()
 def displayRect(self):
   self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

# Display an oval
 def displayOval(self):
   self.canvas.create_oval(10, 10, 190, 90, tags = "oval")

 # Display two lines
 def displayLine(self):
  self.canvas.create_line(10, 10, 190, 90, tags = "line")
  self.canvas.create_line(10, 90, 190, 10, tags = "line")

# Clear drawings
 def clearCanvas(self):
  self.canvas.delete("rect", "oval", "line")

 def popup(self, event):
  self.menu.post(event.x_root, event.y_root)

PopupMenuDemo()


from tkinter import * # Import all definitions from tkinter
class MouseKeyEventDemo:
 def __init__(self):
  window = Tk() # Create a window
  window.title("Event Demo") # Set a title
  canvas = Canvas(window, bg = "white", width = 200, height = 100)
  canvas.pack()
# Bind with <Button-1> event
  canvas.bind("<Button-1>", self.processMouseEvent)

# Bind with <Key> event
  canvas.bind("<Key>", self.processKeyEvent)
  canvas.focus_set()
  window.mainloop() # Create an event loop

 def processMouseEvent(self, event):
  print("clicked at", event.x, event.y)
  print("Position in the screen", event.x_root, event.y_root)
  print("Which button is clicked? ", event.num)

 def processKeyEvent(self, event):
  print("keysym?",event.keysym)
  print("char?",event.char)
  print("keycode?",event.keycode)
MouseKeyEventDemo()



from tkinter import *
class EnlargeShrinkCircle:
 def __init__(self):
  self.radius = 50
  window = Tk() # Create a window
  window.title("Control Circle Demo") # Set a title
  self.canvas = Canvas(window, bg = "white",width = 200, height = 200)
  self.canvas.pack()
  self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags = "oval")
  # Bind canvas with mouse events
  self.canvas.bind("<Button-1>", self.increaseCircle)
  self.canvas.bind("<Button-3>", self.decreaseCircle)
  window.mainloop() # Create an event loop
 def increaseCircle(self, event):
  self.canvas.delete("oval")
  if self.radius < 100:
   self.radius += 2
   self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags="oval")
   self.canvas.delete("oval")
 def decreaseCircle(self, event):
  if self.radius > 2:
   self.radius -= 2
   self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags="oval")
EnlargeShrinkCircle()



from tkinter import * # Import all definitions from tkinter
class AnimationDemo:
 def __init__(self):
  window = Tk() # Create a window
  window.title("Animation Demo") # Set a title
  width = 250 # Width of the canvas
  canvas = Canvas(window, bg="white",width = 250, height = 50)
  canvas.pack()

  x = 0 # Starting x position
  canvas.create_text(x, 30, text = "Message moving?", tags = "text")
  dx = 3
  while True:
      canvas.move("text", dx, 0)
      canvas.after(100)
      canvas.update()
      if x < width:
        x += dx  # Get the current position for string
      else:
        x = 0  # Reset string position to the beginning
        canvas.delete("text")
        canvas.create_text(x,30, text="Message moving?", tags = "text")
  window.mainloop()  # Create an event loop
AnimationDemo()





from tkinter import *
class ScrollText:
 def __init__(self):
  window = Tk() # Create a window
  window.title("Scroll Text Demo") # Set title
  frame1 = Frame(window)
  frame1.pack()
  scrollbar = Scrollbar(frame1)
  scrollbar.pack(side = RIGHT, fill = Y)
  text = Text(frame1, width = 40, height = 10, wrap = WORD,yscrollcommand = scrollbar.set)
  text.pack()
  scrollbar.config(command=text.yview)
  window.mainloop() # Create an event loop
ScrollText()


import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser
tkinter.messagebox.showinfo("showinfo", "This is an info msg")
tkinter.messagebox.showwarning("showwarning", "This is a warning")
tkinter.messagebox.showerror("showerror", "This is an error")
isYes = tkinter.messagebox.askyesno("askyesno", "Continue?")
print(isYes)
isOK = tkinter.messagebox.askokcancel("askokcancel", "OK?")
print(isOK)
isYesNoCancel = tkinter.messagebox.askyesnocancel("askyesnocancel", "Yes, No, Cancel?")
print(isYesNoCancel)
name = tkinter.simpledialog.askstring("askstring", "Enter your name")
print(name)
age = tkinter.simpledialog.askinteger("askinteger", "Enter your age")
print(age)
weight = tkinter.simpledialog.askfloat("askfloat", "Enter your weight")
print(weight)



import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser
tkinter.messagebox.showinfo("showinfo", "Welcome to python")