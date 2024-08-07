n=int(input())
ar = list(map(int, input().split()))

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

def calculate(n, value):
    if n == 0:
        return lcm(ar[0], value)

    return calculate(n - 1, lcm(ar[n], value))


print(calculate(n - 1, 1))