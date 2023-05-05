#14.1
import os.path
import sys
def main():
 keyWords={"and","as","assert","break","class","continue","def","del","elif","else","except","False","finally","for","from"
        ,"global","if","import","in","is","lambda","None","nonlocal","not","or","pass","raise","return","True","try","while","with","yield"}
 file=input("filename?").strip()
 if not os.path.isfile(file):
  print("doesnt exist")
  sys.exit()
 infile=open(file,"r")
 text=infile.read().split()
 count=0
 for e in text:
  if e in keyWords:
   print(e,end=" ")
   count+=1
 print(count)
main()



#14.2
def main():
 infile=open("scores.txt","r")
 num=infile.read().split()
 count1={}
 for i in num:
  if i not in count1:
   count1[i]=1
  elif i in count1:
   count1[i]+=1
 t1=tuple(count1.values())
 t2=tuple(count1.keys())
 maxnum=max(t1)
 index1=t1.index(maxnum)
 value1=t2[index1]
 print(value1)
main()



#14.3
import os.path
import sys
def main():
 keyWords=["and","as","assert","break","class","continue","def","del","elif","else","except","False","finally","for","from"
        ,"global","if","import","in","is","lambda","None","nonlocal","not","or","pass","raise","return","True","try","while","with","yield"]
 file=input("filename?").strip()
 if not os.path.isfile(file):
  print("doesnt exist")
  sys.exit()
 infile = open(file, "r")
 text = infile.read().split()
 count2 = (len(keyWords))*[0]
 for d in range(0,len(keyWords)):
  for e in range(0,len(text)):
   if keyWords[d]==text[e]:
    count2[d] += 1
 for f in range(0, len(keyWords)):
  print(keyWords[f],count2[f])
main()



#14.4
from tkinter import *
from tkinter.filedialog import askopenfilename
class Occurance():
 def __init__(self):
  window=Tk()
  window.title("Occurance")
  frame1=Frame(window)
  frame1.pack()
  self.canvas1=Canvas(frame1,width=400,height=400,scrollregion=(0,0,600,600))
  scrollbar = Scrollbar(frame1)
  scrollbar.pack(side=RIGHT, fill=Y)
  scrollbar.config(command=self.canvas1.yview)
  self.canvas1.config(yscrollcommand=scrollbar.set)
  self.canvas1.pack()
  lblFile=Label(frame1,text = "Enter FileName").pack(side=LEFT)
  self.fileName=StringVar()
  Entry(frame1,textvariable = self.fileName).pack(side=LEFT)
  btBrowse=Button(frame1,text="Browse",command=self.Browse).pack(side=LEFT)
  btShow= Button(frame1, text="Show Result", command=self.ShowResult).pack(side=LEFT)
  window.mainloop()
 def ShowResult(self):
  pureFile=(self.fileName.get()).strip()
  infile=open(pureFile,"r")
  text=infile.read().split()
  alphabet=[]
  count1=26*[0]
  for g in range(97,123):
   alphabet.append(chr(g))
  for h in range (0,len(alphabet)):
   for i in range (0,len(text)):
    for j in range(0,len(text[i])):
     if alphabet[h]==text[i][j]:
      count1[h]+=1
  x,y=10,10
  for k in range (0,len(count1)):
   self.canvas1.create_text(x,y,text=alphabet[k],tags="string")
   self.canvas1.create_text(x+20,y,text=count1[k],tags="string")
   y+=20
 def Browse(self):
  filename=askopenfilename()
  self.fileName.set(filename)
Occurance()


#14.5
from tkinter import *
import tkinter.messagebox
import os.path
class OccuranceHist():
 def __init__(self):
  window=Tk()
  window.title("Occurance")
  frame1=Frame(window)
  frame1.pack()
  self.canvas1=Canvas(frame1,width=600,height=600)
  self.canvas1.pack()
  lblFile=Label(frame1,text = "Enter FileName").pack(side=LEFT)
  self.fileName=StringVar()
  Entry(frame1,textvariable = self.fileName).pack(side=LEFT)
  btShow= Button(frame1, text="Show Result", command=self.ShowResult).pack(side=LEFT)
  window.mainloop()
 def ShowResult(self):
  if not os.path.isfile(self.fileName.get()):
   tkinter.messagebox.showwarning("showwarning", "The file doesn't exist")
   sys.exit()
  pureFile=(self.fileName.get()).strip()
  infile=open(pureFile,"r")
  text=infile.read().split()
  alphabet=[]
  count1=26*[0]
  for g in range(97,123):
   alphabet.append(chr(g))
  for h in range (0,len(alphabet)):
   for i in range (0,len(text)):
    for j in range(0,len(text[i])):
     if alphabet[h]==text[i][j]:
      count1[h]+=1
  self.canvas1.delete("rect","string")
  x,y=100,400
  for k in range (0,len(count1)):
   self.canvas1.create_rectangle(x,y,x+10,y-count1[k],tags="rect")
   self.canvas1.create_text(x+5,y+10,text=alphabet[k],tags="string")
   x+=10
OccuranceHist()



#14.6
from tkinter import *
import urllib.request
class Occurance():
 def __init__(self):
  window=Tk()
  window.title("Occurance")
  frame1=Frame(window)
  frame1.pack()
  self.canvas1=Canvas(frame1,width=400,height=400,scrollregion=(0,0,600,600))
  scrollbar = Scrollbar(frame1)
  scrollbar.pack(side=RIGHT, fill=Y)
  scrollbar.config(command=self.canvas1.yview)
  self.canvas1.config(yscrollcommand = scrollbar.set)
  self.canvas1.pack()
  lblFile=Label(frame1,text = "Enter URL").pack(side=LEFT)
  self.urlName=StringVar()
  Entry(frame1,textvariable = self.urlName).pack(side=LEFT)
  btShow= Button(frame1, text="Show Result", command=self.ShowResult).pack(side=LEFT)
  window.mainloop()
 def ShowResult(self):
  pureURL=(self.urlName.get()).strip()
  infile=urllib.request.urlopen(pureURL)
  text=infile.read().decode()
  alphabet=[]
  count1=26*[0]
  for g in range(97,123):
   alphabet.append(chr(g))
  for h in range (0,len(alphabet)):
   for i in range (0,len(text)):
    for j in range(0,len(text[i])):
     if alphabet[h]==text[i][j]:
      count1[h]+=1
  x,y=10,10
  for k in range (0,len(count1)):
   self.canvas1.create_text(x,y,text=alphabet[k],tags="string")
   self.canvas1.create_text(x+20,y,text=count1[k],tags="string")
   y+=20
Occurance()



#14.7
from tkinter import *
import tkinter.messagebox
import urllib.request
import os.path
class OccuranceHist():
 def __init__(self):
  window=Tk()
  window.title("Occurance")
  frame1=Frame(window)
  frame1.pack()
  self.canvas1=Canvas(frame1,width=600,height=600)
  self.canvas1.pack()
  lblFile=Label(frame1,text = "Enter URL").pack(side=LEFT)
  self.URLName=StringVar()
  Entry(frame1,textvariable = self.URLName).pack(side=LEFT)
  btShow= Button(frame1, text="Show Result", command=self.ShowResult).pack(side=LEFT)
  window.mainloop()
 def ShowResult(self):
  '''if not os.path.isfile(self.URLName.get()):
   tkinter.messagebox.showwarning("showwarning", "The URL doesn't exist")
   sys.exit()'''
  pureURL = (self.URLName.get()).strip()
  infile = urllib.request.urlopen(pureURL)
  text = infile.read().decode()
  alphabet=[]
  count1=26*[0]
  for g in range(97,123):
   alphabet.append(chr(g))
  for h in range (0,len(alphabet)):
   for i in range (0,len(text)):
    for j in range(0,len(text[i])):
     if alphabet[h]==text[i][j]:
      count1[h]+=1
  self.canvas1.delete("rect","string")
  x,y=100,400
  for k in range (0,len(count1)):
   self.canvas1.create_rectangle(x,y,x+10,y-count1[k],tags="rect")
   self.canvas1.create_text(x+5,y+10,text=alphabet[k],tags="string")
   x+=10
OccuranceHist()

   

#14.8
def main():
 file=input("filename?").strip()
 infile=open(file,"r")
 text=infile.read().split()
 words=set()
 wordlist=[]
 for i in range(0,len(text)):
  j=text[i].strip()
  words.add(j)
 wordlist=sorted(words)
 print(wordlist)
main()



#14.9




#14.10







#14.11
def main():
 file=input("filename?").strip()
 infile=open(file,"r")
 text = infile.read().split()
 alphabetset =set()
 alphabet=[]
 count3=26*[0]
 vowel=[]
 consonant=[]
 for i in range(97,123):
  alphabet.append(chr(i))
 alphabetset=set(alphabet)
 for j in range(0,len(alphabet)):
  for k in range(0,len(text)):
   for m in range(0,len(text[k])):
    if alphabet[j]==text[k][m]:
     count3[j]+=1
 for l in range(0, len(count3)):
  if l==0 or l==4 or l==7 or l==14 or l==21:
   vowel.append(count3[l])
  else:
   consonant.append(count3[l])
 print(vowel)
main()

