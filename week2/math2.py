# This function finds the LCM of two integers
def findlcm(a, b):
    if (a > b):
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            break
        maximum = maximum + 1
    return maximum


def lcm():
    a = int(input(" Pick a Number: "))
    b = int(input(" Pick Another Number: "))
    lcm = findlcm(a, b)
    print("\n The Least Common Multiple of {0} and {1} is: {2}".format(a, b, lcm))
    print()