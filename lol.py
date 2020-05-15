child: bool
age: int = 18
if age < 18:
    child = True
else:
    child = False

print(child)

import math

def degrees_to_radians(degrees: float) -> float:
    return math.pi * degrees / 180

n: int=90 
print(degrees_to_radians(n))