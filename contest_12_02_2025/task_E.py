import sys

a, b, c, d = map(int, sys.stdin.readline().split())

func = lambda x: a * (x ** 3) + b * (x ** 2) + c * x + d

left = -1000.0
right = 1000.0

epsilon = 1e-20

if a != 0:
    while (right - left) / 2 > epsilon:
        mid = (left + right) / 2
        if func(mid) == 0:
            print(f"{mid:.20f}")
            break
        elif func(left) * func(mid) < 0:
            right = mid
        else:
            left = mid