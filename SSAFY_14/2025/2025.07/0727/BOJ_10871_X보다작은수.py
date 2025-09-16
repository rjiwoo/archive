# 10871번 X보다 작은 수

N, X = list(map(int, input().split()))

A = list(map(int, input().split()))

for i in range(len(A)):
    if A[i] < X:
        print(A[i], end=' ')
