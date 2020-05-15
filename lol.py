child: bool
age: int = 8
for x in range (1,5):
    if age < 18:
        child = True
    else:
        child = False

    print(child)
    age+=5

import math

def degrees_to_radians(degrees: float) -> float:
    return math.pi * degrees / 180

n: int=90 
print(degrees_to_radians(n))

from typing import Iterator, Iterable, Optional

class IntList: # type: ignore
    def __init__(self, value: int, next: Optional['IntList']) -> None: # type: ignore
        self.value = value
        self.next = next

    def __iter__(self) -> Iterator[int]:
        current = self
        while current:
            yield current.value
            current = current.next # type: ignore

def print_numbered(items: Iterable[int]) -> None: # type: ignore
    for n, x in enumerate(items):
        print(n + 1, x)

x = IntList(3, IntList(5, None)) # type: ignore
print_numbered(x) # type: ignore
print_numbered([5, 5]) # type: ignore

from dataclasses import dataclass, field

# mypy: disallow-any-generics