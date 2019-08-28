n = int(input())
lis = [int(i) for i in input().split()]

maxVal, sumEle, count = 0, 0, 0
for i in lis:
    if sumEle < 0:
        sumEle = 0
    sumEle += i

    if maxVal <= sumEle:
        if maxVal == sumEle:
            count += 1
        else:
            maxVal = sumEle
            count = 1
print(maxVal, count)