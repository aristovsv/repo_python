from itertools import count
from math import factorial


def fact_gen():
    for el in count(1):
        yield factorial(el)



x = 0
for i in fact_gen():
    if x == 5:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")
