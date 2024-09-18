import numpy as np
import random
from time import time

def rand(n: int) -> NDArray[float]:
    """Creates a numpy array with 'n' random elements, which sum is equals to 42"""
    a: NDArray[float] = np.random.random(n)
    r: float = np.sum(a)
    a: NDArray[float] = np.subtract(a, (r - 42) / n)
    return a

def avglist(n: int, m: int) -> float:
    """Calculates the average of the elements in a list with 'n' rows and 'm' columns, which is filled with random numbers using python's internal math"""
    l: list[list[float]] = [[random.random() for i in range(0, m)] for i in range(0, n)]
    sum: float = 0.0
    for i in l:
        for j in i:
            sum += j
    return sum / (n * m)

def avgarray(n: int, m: int) -> float:
    """Calculates the average of the elements in a list with 'n' rows and 'm' columns, which is filled with random numbers using numpy's math"""
    a: NDArray[float] = np.random.random((n, m))
    return np.divide(np.sum(a), np.multiply(n, m))


if __name__ == "__main__":
    array: NDArray[float] = rand(10)
    r: int = int(np.sum(array))
    print(array)
    print(r)
    print()
    t: float = time()
    print(avglist(10000, 10000))
    print(f"Finished in: {time() - t}s")
    t: float = time()
    print(avgarray(10000, 10000))
    print(f"Finished in: {time() - t}s")
