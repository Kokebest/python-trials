from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
filenameforReading = askopenfilename()
print("You can read from " + filenameforReading)
filenameforWriting = asksaveasfilename()
print("You can write data to " + filenameforWriting)




def main():
 try:
  f()
  print("After the function call")
 except ZeroDivisionError:
  print("Divided by zero!")
 except:
  print("Exception")
def f():
 print(1 / 0)
main()


def main():
 try:
  f()
  print("After the function call")
 except IndexError:
  print("Index out of bound")
 except:
  print("Exception in main")
def f():
 try:
  s ="abc"
  print(s[3])
 except ZeroDivisionError:
  print("Divided by zero!")
main()


try:
 lst = 10 * [0]
 x = lst[9]
 print("Done")
except IndexError:
 print("Index out of bound")
else:
 print("Nothing is wrong")
finally:
 print("Finally we are here")
print("Continue")



try:
 lst = 10 * [0]
 x = lst[10]
 print("Done ")
except IndexError:
 print("Index out of bound")
else:
 print("Nothing is wrong")
finally:
 print("Finally we are here")
print("Continue")


try:
 # Some code here
 lst = 10 * [0]
 x = lst[9]
 print("Done")
except ArithmeticError:
 print("ArithmeticError")
except ZeroDivisionError:
 print("ZeroDivisionError")
 print("Continue")



import pickle
def main():
 # Open file for writing binary
 outfile = open("numbers.dat", "wb")
 data = eval(input("Enter an integer (the input exits " +"if the input is 0): "))
 while data != 0:
   pickle.dump(data, outfile)
   data = eval(input("Enter an integer (the input exits " +"if the input is 0): "))

 outfile.close() # Close the output file
 infile = open("numbers.dat", "rb")
 # Open file for reading binary
 end_of_file = False
 while not end_of_file:
  try:
   print(pickle.load(infile), end = " ")
  except EOFError:
   end_of_file = True
 infile.close() # Close the input file
 print("\nAll objects are read")
main() # Call the main function









import pickle
def main():
 # Open file for writing binary
 outfile = open("numbers.dat", "wb")
 data = eval(input("Enter an integer (the input exits " +"if the input is 0): "))
 while data != 0:
   pickle.dump(data, outfile)
   data = eval(input("Enter an integer (the input exits " +"if the input is 0): "))

 outfile.close() # Close the output file
 infile = open("numbers.dat", "rb")
 # Open file for reading binary
 end_of_file = False
 while not end_of_file:
  try:
   print(pickle.load(infile), end=" ")
  except EOFError:
   end_of_file = True
  finally:
   infile.close()
  print("\nAll objects are read")
main() # Call the main function


import pickle
def main():
 # Open file for writing binary
 outfile = open("numbers.dat", "wb")
 data = eval(input("Enter an integer (the input exits " +"if the input is 0): "))
 while data != 0:
   pickle.dump(data, outfile)
   data = eval(input("Enter an integer (the input exits " +"if the input is 0): "))

 outfile.close() # Close the output file
 infile = open("numbers.dat", "rb")
 # Open file for reading binary
 end_of_file = False
 try:
  while not end_of_file:
   print(pickle.load(infile), end=" ")
 except EOFError:
  print("\nAll objects are read")
 finally:
  infile.close()
 print("\nAll objects are read")
main() # Call the main function