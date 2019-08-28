n,m,g = map(int, input().split())

t = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

isTrue = [False for i in range(m)]
count = 0
for i in range(n-1):
    temp = t[i+1] - t[i]
    for j in range(m):
        if a[j] <= temp and isTrue[j] == False:
            isTrue[j] = True
            count+=1
print(count)