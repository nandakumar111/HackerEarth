def solution(pol, the, k):
    count = 0
    for p in pol:
        for t in the:
            if abs(p - t) <= k:
                count += 1
                the.remove(t)
                break
    return count


t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    police, thief, A = [], [], []
    res = 0
    for i in range(N):
        A.append(input().split())
        police = [i for i, x in enumerate(A[i]) if x == 'P']
        thief = [i for i, x in enumerate(A[i]) if x == 'T']
        res += solution(police, thief, K)
    print(res)
