T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 양수의 개수

    arr = list(map(int, input().split()))

    max_num = arr[0]
    min_num = arr[0]
    for i in range (1, N):
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]

    answer = max_num - min_num
    print(f'#{tc} {answer}')