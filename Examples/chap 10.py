list1=[2,2,'l',56]
len(list1)
import random
random.shuffle(list1)

lst = [] # Create a list
print("Enter 10 numbers: ")
for i in range(10):
  lst.append(eval(input())

s = input("Enter 10 numbers separated by spaces from one line: ")
items = s.split()  # Extract items from the string
lst = [eval(x) for x in items]

list1 = [30, 1, 2, 1, 0]
list2 = [1, 21, 13]
list1 + list2

s1="Welcome"
s1.split('o')

l1=[]
for i in range [0,101]:
 l1[i]=False
l1

lst2 = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
   lst2[i] = lst2[i - 1]
print(lst2)


def main():
  lst = [1, 2, 3, 4, 5]
  reverse(lst)
  for value in lst:
      print(value, end=' ')
def reverse(lst):
  newLst = len(lst) * [0]
  for i in range(len(lst)):
      newLst[i] = lst[len(lst) - 1 - i]
  lst = newLst
main()

def main():
 list1 = m(1)
 print(list1)
 list2 = m(1)
 print(list2)
def m(x, lst = [1, 1, 2, 3]):
 if x in lst:
  lst.remove(x)
 return lst
main()


def main():
 list1 = m(1)
 print(list1)
 list2 = m(1)
 print(list2)
def m(x, lst = None):
 if lst == None:
  lst = [1, 1, 2, 3]
 if x in lst:
  lst.remove(x)
 return lst
main()
