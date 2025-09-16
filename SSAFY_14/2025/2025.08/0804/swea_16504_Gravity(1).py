# swea 16504번 Gravity

# 첫번째 제출

T = int(input())

for tc in range(1, 1+T):
    N = int(input()) # 가로 N

    arr = list(map(int, input().split()))

    # for i in range(N):
    #     abs(arr[i] - arr[N-1])
   
    result = []
    for i in range(N):
        big = 0
        for j in range(1, N-i):
            if arr[i] > arr[i+j]:
                big += 1
        result.append(big)

    # print(result)
    answer = max(result)
    print(f'#{tc} {answer}')