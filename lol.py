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

from typing import Iterator, Iterable, Optional

class IntList:
    def __init__(self, value: int, next: Optional['IntList']) -> None:
        self.value = value
        self.next = next

    def __iter__(self) -> Iterator[int]:
        current = self
        while current:
            yield current.value
            current = current.next

def print_numbered(items: Iterable[int]) -> None:
    for n, x in enumerate(items):
        print(n + 1, x)

x = IntList(3, IntList(5, None))
print_numbered(x) 
print_numbered([5, 5]) 

