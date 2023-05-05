#10.1
list1=[]
scores=0
while scores>=0:
    scores=eval(input("scores?, put in a negative number at the end to indicate u r finished "))
    list1.append(scores)
maxScore=max(list1)
for i in range(0,len(list1)-1):
 if list1[i]>=maxScore-10:
     print ("Student",i," has scored A")
 elif list1[i]>=maxScore-20:
     print ("Student",i, " has scored B")
 elif list1[i]>=maxScore-30:
     print ("Student",i," has scored C")
 elif list1[i]>=maxScore-40:
     print ("Student",i," has scored D")
 else:
     print ("Student",i, "has scored F")



#10.2 (I could have used reverse()) ^^
list2=[]
inputInteger=0
while inputInteger>=0:
    inputInteger=eval(input("numbers?, put in a negative number at the end to indicate u r finished "))
    list2.append(inputInteger)
list3=[]
for i in range (len(list2)-2,-1,-1):
    k=list2[i]
    list3.append(k)
list3


#10.3
count=100*[0]
list5=[]
integers=0
while integers>=0:
    integers=eval(input("integers?, put in a negative number at the end to indicate u r finished "))
    list5.append(integers)
for l in range (0,len(list5)):
    for m in range(0,100):
        if m==list5[l]:
         count[m]=count[m]+1
for n in range(0,len(count)-1):
 if count[n]==0:
   continue
 elif count[n]==1:
     print(n, "appears", count[n], "time")
 else:
  print(n, "appears", count[n],"times")

#10.4
scoresOfExams=input("insert the numbers separated by one space")
list6=(scoresOfExams.split(" "))
list7=[]
for o in range(0,len(list6)):
   list7.append(int(list6[o]))
averageNum=sum(list7)/len(list7)
count1,count2=0,0
for p in range(0,len(list7)):
    if list7[p]>=averageNum:
        count1+=1
    else:
        count2+=1
print(count1," students have above average scores while",count2,"students have less than average.")


#10.5
num=input("insert num")
listnew=num.split(" ")
listnew2=[]
listnew2.append(listnew[0])
for i in range (1,len(listnew)):
 isDuplicate = False
 for j in range (0,len(listnew2)):
     if listnew[i]==listnew2[j]:
         isDuplicate=True
         continue
 if isDuplicate == False:
  listnew2.append(listnew[i])
listnew2


#10.6 error
list11=[]
list12=[]
count3=0
while count3<50:
   for i in range(2,1000):
     for j in range (2,i**0.5):
        if i%list12[i-1]==0:
            break
        else:
            list12.append()
            count+=1

   if count==50:
       break



#10.7
import random
list13=[]
list14=10*[0]
for u in range(0,1000):
    h=random.randint(0,9)
    list13.append(h)
for v in range(0,len(list13)):
    for w in range (0,len(list14)):
        if list13[v]==w:
            list14[w]+=1
            break

list14


#10.8
def indexOfSmallestNumber(lst):
    x=(min(lst))
    z=lst.index(x)
    return x,z
def main():
  list15=[]
  list16=[]
  acceptedNum=(input("insert num separated by comma"))
  list15=acceptedNum.split(" ")
  for y in range (0,len(list15)):
      list16.append(list15[y])
  print(indexOfSmallestNumber(list15))
main()


#10.9
def mean(lst):
    avg=sum(lst)/len(lst)
    return avg
def deviation(lst2):
    sum2=0
    for z in range (0,len(lst2)):
      diff=(lst2[z]-mean(lst2))**2
      sum2=sum2+diff
    return (sum2/(len(lst2)-1))**0.5

def main():
    list17 = []
    list18=[]
    acceptedNum2 = (input("insert num separated by comma"))
    list17 = acceptedNum2.split(" ")
    for y in range(0, len(list17)):
        list18.append(eval(list17[y]))
    print(deviation(list18))
main()


#10.10
def reverseFunction(lst):
    lst.reverse()
    return lst
def main():
    list19=[]
    acceptedNum3=(input("insert number separated by comma"))
    list19 = acceptedNum3.split(" ")
    print(reverseFunction(list19))
main()


#10.11 error
import random
def shuffle(lst):
    for a in range(0,len(lst)+1):
        b=random.randint(0,len(lst))
        lst[a]=lst[b]
    return lst

def main():
    list20=[]
    acceptedNum4=input("insert number separated by comma")
    list20=acceptedNum4.split(" ")
    print(shuffle(list20))

main()

#10.12
def gcd(numbers):
    n1,n2,n3,n4,n5=numbers[0],numbers[1],numbers[2],numbers[3],numbers[4]
    k=1
    while k<=min(numbers):
        if n1%k==0 and n2%k==0 and n3%k==0 and n4%k==0 and n5%k==0:
            gcd=k
        k+=1
    return gcd
def main():
    list21=[]
    list22=[]
    acceptedNum5 = input("insert 5 numbers separated by comma")
    list21 = acceptedNum5.split(" ")
    for i in range(0,len(list21)):
     d1=int(list21[i])
     list22.append(d1)
    print(gcd(list22))
main()

#10.13
def eliminateDuplicates(lst):
    lst1 = []
    lst1.append(lst[0])
    for i in range(1,len(lst)):
        isDuplicate = False
        for j in range(0, len(lst1)):
            if lst[i] == lst1[j]:
                isDuplicate = True
                continue
        if isDuplicate == False:
            lst1.append(lst[i])
    return lst1
def main():
    list23=[]
    list24=[]
    acceptedNum6 = input("insert numbers separated by comma")
    list23 = acceptedNum6.split(" ")
    for i in range(0,len(list23)):
     d1=int(list23[i])
     list24.append(d1)
    print(eliminateDuplicates(list24))
main()




#10.14

#10.15
def isSorted(lst):
   lst2=[]
   for i in range (0,len(lst)):
       lst2.append(lst[i])
   lst.sort()
   if lst==lst2:
       return True
   else:
       return False

def main():
    list27=[]
    acceptedNum7=input("enter the number separated by spaces")
    list27=acceptedNum7.split(" ")
    if isSorted(list27) == True:
        print("sorted")
    else:
        print("not sorted")
main()


#10.16 error
def BubbleSort(lst):
 for i in range(0,len(lst)):
  for j in range(0,i):
   if lst[i]<lst[j]:
     k=i
     lst[i]=lst[j]
     lst[j]=lst[k]
   else:
     continue
 print(lst)
 return lst
def main():
 list27=[]
 acceptedNum7 = input("enter the number separated by spaces")
 list27 = acceptedNum7.split(" ")
 print(BubbleSort(list27))
main()




#10.17
def Anagram(s1,s2):
 if s1==s2:
  return ("yes, anagrams")
 else:
  return ("not anagrams")
def main():
 string1=input("string1")
 string2=input("string2")
 list28,list29=[],[]
 for i in range(0,len(string1)):
  list28.append(string1[i])
  list29.append(string2[i])
 list28.sort()
 list29.sort()
 print(Anagram(list28,list29))
main()





#10.21
locker=100*[False]
for i in range(0,len(locker)):
    locker[i]=True
for j in range(1,len(locker),2):
    locker[j]=False
for k in range(2,len(locker),3):
    if locker[k]==True:
      locker[k]=False
    else:
      locker[k]=True
for l in range(4,101):
    for m in range(l-1,len(locker),l):
        if locker[m] == True:
            locker[m] = False
        else:
            locker[m] = True
count10=0
for n in range(0,len(locker)):
 if locker[n]==True:
    count10+=1
count10

#10.22

#10.23
def solveQuadratic(eqn):
    a,b,c=eqn[0],eqn[1],eqn[2]
    if b**2-4*a*c>0:
        root1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        root2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        roots=[]
        roots.append(root1)
        roots.append(root2)
        return (roots,len(roots))
    elif b**2-4*a*c==0:
        root1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        roots=[]
        roots.append(root1)
        return (roots,len(roots))
    elif b**2-4*a*c<0:
        roots=[]
        return (roots,len(roots))
def main():
    a,b,c=eval(input("coefficent?"))
    eqn1=[]
    eqn1.append(a)
    eqn1.append(b)
    eqn1.append(c)
    print(solveQuadratic(eqn1))
main()

#10.24
def combination(lst):
 for t in range (0,len(lst)):
  for u in range (0,len(lst)):
   print((lst[t],lst[u]),end="")
def main():
   list30=[]
   acceptedNum8=input("enter number separted by comma")
   list30=acceptedNum8.split(",")
   combination(list30)
main()

#10.25
def sumOfCards():
 import random
 card=4*[0]
 for y in range(1,28562):
  for t in range(0,4):
   i=random.randint(1,13)
   card[t]=i
  sum1=sum(card)
  if sum1==24:
    print(card)

sumOfCards()


#10.26
def merge(list1,list2):
    for y in range (0,len(list2)):
        list1.append(list2[y])
    for m in range (0,len(list1)):
        list1[m]=int(list1[m])
    list1.sort()
    return list1
def main():
    acceptedNumbers9=(input("number separated by space"))
    list31=acceptedNumbers9.split(" ")
    acceptedNumbers10=input("number separated by space")
    list32=acceptedNumbers10.split(" ")
    print(merge(list31,list32))
main()

#10.27 error
def isConsecutiveFour(values):
   for i in range(0,len(values)):
       if values[i]==values[i-1]:
        if values[i-1] == values[i-2]:
         if values[i-2] == values[i - 3]:
             return("yes",values[i])
       else:
           return("no")
def main():
    acceptedNum11=input("number?")
    list33=acceptedNum11.split(" ")
    print(isConsecutiveFour(list33))
main()

#10.28






#10.29






#10.30
year=eval(input("year?"))
zodiacYear=year%12
ChineseZodiac=["monkey","rooster","dog","pig","rat","ox","tiger","rabbit","dragon","snake","horse","sheep"]
for i in range (0,len(ChineseZodiac)):
  if zodiacYear==i:
      print(ChineseZodiac[i])




#10.31
def counts(s):
  list98=[]
  count6=10*[0]
  for i in range (0,len(s)):
      list98.append(int(s[i]))
  for j in range (0,len(list98)):
      for k in range (0,len(count6)):
          if list98[j]==k:
              count6[k]+=1
  for l in range (0,len(count6)):
     if count6[l]==0:
         continue
     else:
      print(l,"appears",count6[l],"times")
def main():
 acceptedString=input("enter number")
 counts(acceptedString)
main()


#10.32
def drawLine(p1,p2):
 import turtle
 turtle.penup()
 turtle.goto(p1)
 turtle.pendown()
 turtle.goto(p2)
 turtle.done()
def main():
    x1,y1=eval(input("first point"))
    x2,y2=eval(input("second point"))
    p1=(x1,y1)
    p2=(x2,y2)
    drawLine(p1,p2)
main()


#10.33
from tkinter import *
import random
class histogram():
 def __init__(self):
  window=Tk()
  window.title("Histogram")
  self.canvas1 = Canvas(window, width=400, height=400, bg="white")
  self.canvas1.pack()
  frame1=Frame()
  frame1.pack()
  Button(frame1,text="Display Histogram", command=self.drawHistogram).pack()
  window.mainloop()
 def createLetters(self):
   list100 = []
   list101 = []
   self.alphabetsCount = []
   count5 = 26 * [0]
   for h in range(97, 123):
    self.alphabetsCount.append(chr(h))
   for i in range(0, 1000):
    list100.append(random.randint(97, 122))
    list101.append(chr(list100[i]))
   for j in range(0, len(list101)):
    for k in range(0, len(self.alphabetsCount)):
     if list101[j] == self.alphabetsCount[k]:
      count5[k]+=1
   return count5
 def drawHistogram(self):
   x=10
   y=300
   lst=self.createLetters()
   for r in range (0,len(lst)):
    self.canvas1.create_rectangle(x,y,x+10,y-lst[r],tags="rect1")
    self.canvas1.create_text(x+7,y+10,text=self.alphabetsCount[r])
    x+=10
histogram()


#10.34
#10.35



#10.36
from tkinter import *
import random
class LinearSearch():
 def __init__(self):
  window=Tk()
  window.title("linear search")
  frame1=Frame(window)
  frame1.pack()
  self.canvas3=Canvas(frame1,height=400,width=400,bg="white")
  self.canvas3.pack()
  Label(frame1, text="Enter a key").pack(side=LEFT)
  self.search = StringVar()
  Entry(frame1, textvariable=self.search, justify=RIGHT).pack(side=LEFT)
  btStep = Button(frame1, text="Step", command=self.LinearSearch).pack(side=LEFT)
  btReset=Button(frame1, text="Reset", command=self.Reset).pack(side=LEFT)
  self.lst1 = []
  for i in range(0, 21):
    self.lst1.append(i)
  random.shuffle(self.lst1)
  x = 10
  y = 100
  for r in range(0, len(self.lst1)):
      self.canvas3.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1")
      self.canvas3.create_text(x + 7, y + 10, text=self.lst1[r],tags="text")
      x += 13
  window.mainloop()
 def LinearSearch(self):
  for i in range(0,len(self.lst1)):
   if int(self.search.get())==self.lst1[i]:
    self.canvas3.delete("rect1","text")
    x = 10
    y = 100
    for r in range(0, len(self.lst1)):
        if r==i:
         self.canvas3.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1",fill="black")
         self.canvas3.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
         x += 13
        else:
         self.canvas3.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1")
         self.canvas3.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
         x += 13
 def Reset(self):
     self.canvas3.delete("rect1", "text")
     self.lst1 = []
     for i in range(0, 21):
         self.lst1.append(i)
     random.shuffle(self.lst1)
     x = 10
     y = 100
     for r in range(0, len(self.lst1)):
         self.canvas3.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1")
         self.canvas3.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
         x += 13
LinearSearch()




#10.37 error
from tkinter import *
class BinarySearch():
 def __init__(self):
  window=Tk()
  window.title("Binary Search")
  frame1=Frame(window)
  frame1.pack()
  self.canvas4=Canvas(frame1,height=400,width=400,bg="white")
  self.canvas4.pack()
  Label(frame1, text="Enter a key").pack(side=LEFT)
  self.search = StringVar()
  Entry(frame1, textvariable=self.search, justify=RIGHT).pack(side=LEFT)
  btStep = Button(frame1, text="Step", command=self.BinarySearch).pack(side=LEFT)
  btReset=Button(frame1, text="Reset", command=self.Reset).pack(side=LEFT)
  self.lst1 = []
  for i in range(1,19):
    self.lst1.append(i)
  x = 10
  y = 100
  for r in range(0, len(self.lst1)):
      self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1")
      self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
      x += 13
  window.mainloop()
 def BinarySearch(self):
  min, max = self.lst1[0],self.lst1[len(self.lst1)-1]
  mid=(min+max)//2
  while min<max:
   if int (self.search.get())<self.lst1[mid]:
    self.canvas4.delete("rect1", "text")
    x = 10
    y = 100
    for r in range(min,max):
     if r == mid:
      self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1", fill="black")
      self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
      x += 13
     else:
      self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1",fill="grey")
      self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
      x += 13
    max = mid - 1
   elif int (self.search.get())>self.lst1[mid]:
    self.canvas4.delete("rect1", "text")
    x = 10
    y = 100
    for r in range(min,max):
     if r == mid:
      self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1", fill="black")
      self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
      x += 13
     else:
      self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1",fill="grey")
      self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
      x += 13
    min = mid
   elif int(self.search.get()) == self.lst1[mid]:
    self.canvas4.delete("rect1", "text")
    x = 10
    y = 100
    for r in range(min,mid):
        if r == mid:
            self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1", fill="black")
            self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
            x += 13
        else:
            self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1", fill="grey")
            self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
            x += 13
    min = mid
 def Reset(self):
     self.canvas4.delete("rect1", "text")
     self.lst1 = []
     for i in range(0, 21):
         self.lst1.append(i)
     x = 10
     y = 100
     for r in range(0, len(self.lst1)):
         self.canvas4.create_rectangle(x, y, x + 10, y - self.lst1[r], tags="rect1")
         self.canvas4.create_text(x + 7, y + 10, text=self.lst1[r], tags="text")
         x += 13
BinarySearch()




































