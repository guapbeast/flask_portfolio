# the factorial class acts as a blueprint for the creation of objects within python.

class factorial:
  def __init__(self):
    self.facSeq = [0, 1]

  def __call__ (self,n):
    if n == 1 or n==0:
      return 1
    else:
      return n * self(n-1)


def tester():
  fibonacci_func = factorial()
  print("the Factorial of 7 is...", fibonacci_func(7))

  # The python tester allows the function to run online.