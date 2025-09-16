# swea 16504번 Gravity

# 두번째 제출
T = int(input())

for tc in range(1, 1+T):
    N = int(input()) # 가로 N
    arr = list(map(int, input().split()))

    distance_num = []
    for i in range(N):
        distance = 0
        for j in range(1, N-i):
            if arr[i] > arr[i+j]:
                distance += 1
        distance_num.append(distance)

    # print(result)
    answer = max(distance_num)
    print(f'#{tc} {answer}')


# 세번째 제출
T = int(input())

for tc in range(1, 1+T):
    N = int(input()) # 가로 N
    arr = list(map(int, input().split()))

    distance_num = 0
    for i in range(N):
        distance = 0
        for j in range(1, N-i):
            if arr[i] > arr[i+j]:
                distance += 1
        if distance_num < distance: 
            distance_num = distance

    print(f'#{tc} {distance_num}')