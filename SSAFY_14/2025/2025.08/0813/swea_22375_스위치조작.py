# SWEA 22375번 스위치 조작

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0

    for i in range(N):
        if A[i] != B [i]:
            for j in range(i, N):
                A[j] = 1 - A[j]
            count += 1

    print(f'#{tc} {count}')