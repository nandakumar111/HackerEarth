n = int(input())

for i in range(n):
    pot, a, b = map(int, input().split())
    if a < b:
        s, l = a, b
    else:
        s, l = b, a
    x = int(((s * pot) / (s + l)) + 0.5)
    print(l * x ** 2 + (s * (pot - x) ** 2))
