import math

def find_Pythagorean(n):
    result = []

    for i in range(1, n):
        for j in range(2, n):
            c = math.sqrt(i**2 + j**2)
            if c.is_integer():
                result.append((i, j, int(c)))

    return result

print(find_Pythagorean(20))