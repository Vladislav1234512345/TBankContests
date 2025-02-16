import math


C = float(input().strip())


def f(x: float) -> float:
    return x**2 + math.sqrt(x + 1) - C


low = 0.0
high = C

while high - low > 1e-7:
    mid = (low + high) / 2
    if f(mid) < 0:
        low = mid
    else:
        high = mid

result = (low + high) / 2
print(f"{result:.6f}")