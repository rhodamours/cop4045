import math

def plot_function(fun_str, domain, ns):
    xs = []

    interval = abs(abs(domain[1]) - abs(domain[0]))

    for i in range(domain[0], domain[1], interval):
        xs.append(i)