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