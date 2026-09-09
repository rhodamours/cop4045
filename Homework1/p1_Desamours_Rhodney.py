import math
import matplotlib.pyplot as plt
#import numpy as np

a = 0
b = 0
c = 0

xs = [x for x in range(150)]

a = input("Enter coefficient a: ")

while a != "":
    a = float(a)
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b**2 - 4 * a * c
    vertex = (-b)/(2 * a)
    
    # Get a list of 150 values for the domain centered at the vertex
    xs = [x for x in range(int(vertex - 75), int(vertex + 75))]

    if discrim < 0:
        print("no real solutions\n")
        
    elif discrim == 0:
        x1 = vertex
        print("one solution:", x1, "\n")
    elif discrim > 0:
        x1 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
        x2 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
        print("two solutions:", x1, ",", x2, "\n")
        
        # Check if x1 and x2 are within the bounds of the 150 value domain
        # centered around the vertex.
        if not ((vertex - 75) <= x1 <= (vertex + 75) and
                (vertex - 75) <= x2 <= (vertex + 75)):
            # Create a new domain that evenly spreads 150 values between a min
            # and max 10 points away from x1 and x2.
            n = int((x2 + 10) - (x1 - 10) / 150)
            xs = [x for x in range(int(x1 - 10), int(x2 + 10), n)]

    fig, ax = plt.subplots()
    ax.plot(xs, [(a * (x**2) + b * x + c) for x in xs])
    plt.show()
    
    a = input("Enter coefficient a: ")
