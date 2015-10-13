__author__ = 'lelik'

import math

func = input("Choose function (cos, sin, sum, pow): ")

if func == "cos":
    x = input("Enter x: ")
    print("cos of x = " + str(math.cos(float(x))))
elif func == "sin":
    x = input("Enter x: ")
    print("sin of x = " + str(math.sin(float(x))))
elif func == "sum":
    a = input("Enter a: ")
    b = input("Enter b: ")
    print("sum of 'a' and 'b' = " + str(float(a)+float(b)))
elif func == "pow":
    a = input("Enter a: ")
    b = input("Enter b: ")
    print("pow of 'a' and 'b' = " + str(math.pow(int(a), int(b))))
else:
    print("incorrect input")


