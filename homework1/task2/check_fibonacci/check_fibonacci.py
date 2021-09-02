from math import sqrt
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    length = len(data)
    fib1 = 0
    fib2 = 1
    if length == 0 or length == 1:
        return False
    if data[0] == 0 and data[1] == 1:
        for i in range(2, length):
            fib1, fib2 = fib2, fib1 + fib2
            if not fib2 == data[i]:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_fibonacci([0, 1, 1, 2]))
