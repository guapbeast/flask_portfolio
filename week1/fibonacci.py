def FibonacciFunc(n):
    if n <= 1:
        return n
    else:
        return (FibonacciFunc(n - 2) + FibonacciFunc(n - 1))

# Factorial used for the sequence
def tester():
    try:
        num = int(input("Enter a number... "))
        if num > 0:
            print("Fibonacci sequence:")
            for i in range(num):
                print(FibonacciFunc(i))
        else:
            print("Positive Number Por Favor")
    except ValueError:
        print("Error in fibonacci Value")
