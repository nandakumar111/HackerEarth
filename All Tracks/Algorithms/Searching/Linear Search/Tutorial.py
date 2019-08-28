n,m = map(int, input().split())
lis = [int(i) for i in input().split()]

print(n-lis[::-1].index(m))