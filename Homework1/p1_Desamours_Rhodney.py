import math
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 0
c = 0

while a != "":
    a = input("Enter coefficient a: ")
    a = float(a)
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b**2 - 4 * a * c

    if discrim < 0:
        print("no real solutions\n")
    elif discrim == 0:
        x1 = (-b)/(2 * a)
        print("one solution:", x1, "\n")
    elif discrim > 0:
        x1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
        x2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
        print("two solutions:", x1, ",", x2, "\n")

    # show graph
    fig = plt.figure()
    plt.show()
