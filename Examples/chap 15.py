def main():
 n = eval(input("Enter a nonnegative integer: "))
 print("Factorial of", n, "is", factorial(n))

 # Return the factorial for the specified number
def factorial(n):
 if n == 0: # Base case
  return 1
 else:
  return n *factorial(n-1) # Recursive call

main()



def main():
 n = eval(input("Enter a nonnegative integer: "))
 print("exponential of", n, "is", exponential(n))

 # Return the factorial for the specified number
def exponential(n):
 if n == 0: # Base case
  return 1
 else:
  return 2*exponential(n-1) # Recursive call

main()



def main():
 x=eval(input("enter a integer"))
 n = eval(input("Enter a nonnegative integer: "))
 print("exponential of", n, "is", exponential1(x,n))

 # Return the factorial for the specified number
def exponential1(x,n):
 if n == 0:
   return 1
 else:
   return x*exponential1(x,n-1)
main()



def main():
 n = eval(input("Enter a nonnegative integer: "))
 print("sum of", n, "is", sum1(n))

 # Return the factorial for the specified number
def sum1(n):
 if n == 0:
   return 0
 else:
   return n+sum1(n-1)
main()


def f(n):
 if n == 1:
  return 1
 else:
  return n + f(n - 1)
print("Sum is", f(5))


def f(n):
 if n > 0:
  print(n % 10)
 f(n // 10)
f(1234567)


def f(n):
 if n > 0:
  print(n, end=' ')
  f(n - 1)
f(5)


def f(n):
 if n > 0:
  f(n - 1)
  print(n, end=' ')
f(5)


def f(n):
 if n != 0:
  print(n, end=' ')
  f(n / 10)
f(1234567)