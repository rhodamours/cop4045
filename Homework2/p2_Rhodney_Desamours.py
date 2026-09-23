digits = [x for x in range(1, 11)]

a2 = [(a, b, c, d) for a in digits for b in digits for c in digits
      for d in digits if len(set((a, b, c, d))) == 4
      and a**2 + b**2 == c**2 + c**2]

numbers = ['One', 'SEVEN', 'three', 'two', 'Ten']

b2 = [(x.lower(), len(x)) for x in numbers if len(x) < 5]

names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']

c2 = [f"{x.split()[0]} {x.split()[1][0]}. {x.split()[2]}" for x in names]

lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

d2 = [(w1, w2) for w1 in lst1 for w2 in lst2
      if sorted(w1.lower()) == sorted(w2.lower())]

s = ['one', 'two', 'three']

e2 = {x: len(x) for x in s}

text = "Hello world"

f2 = {x: y for x, y in enumerate(text) if y.lower() in 'aeiou'}

print('a)', a2)
print('b)', b2)
print('c)', c2)
print('d)', d2)
print('e)', e2)
print('f)', f2)