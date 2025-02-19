import sys


a,b,c,d = list(map(int, sys.stdin.readline().split()))


left = -10 ** 10
right = 10 ** 10
epsilon = 1e-5

func = lambda x: a * (x ** 3) + b * (x ** 2) + c * x + d

if a != 0:
    while (right - left) >= epsilon:
        mid = left + (right - left) / 2
        if func(mid) == 0:
            break
        if func(left) * func(mid) < 0:
            right = mid
        else:
            left = mid

    print("%.20f" %
          float(left + (right - left) / 2))