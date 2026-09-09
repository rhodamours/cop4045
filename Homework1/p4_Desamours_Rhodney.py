#import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    xs = []
    ys = []

    interval = abs(domain[1] - domain[0])/(ns - 1)
    
    i = domain[0]

    while i <= domain[1]:
        xs.append(i)
        
        i += interval
    
    for x in xs:
        ys.append(eval(fun_str))
    
    print(f"{'x':>10} {'y':>10}")
    print("-"*22)
    
    for i in range(len(xs)):
        print(f"{xs[i]:>+10.4f} {ys[i]:>+10.4f}")
        
    fig, ax = plt.subplots()
    ax.plot(xs, ys, 'o-')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.show()
    
fun = input("Enter function with variable x: ")

while fun != "":
    n = int(input("Enter number of samples: "))
    xmin = float(input("Enter xmin: "))
    xmax = float(input("Enter xmax: "))
    
    plot_function(fun, (xmin, xmax), n)
    
    fun = input("\nEnter function with variable x: ")