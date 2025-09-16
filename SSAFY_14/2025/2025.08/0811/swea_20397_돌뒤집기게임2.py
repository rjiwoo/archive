# swea 20397번 돌 뒤집기 게임 2

T = int(input()) # 게임의 개수

for tc in range(1, T+1):
    # 돌의 수 N, 뒤집기 횟수 M
    N, M = map(int, input().split())

    #  N개 돌의 초기상태 
    arr = list(map(int, input().split()))

    # M개의 줄에 걸쳐 i, j가 주어진다
    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(1, j+1):
            if 0 <= i-1-k and i-1+k < N:
                if arr[i-1-k] == arr[i-1+k]:
                    arr[i-1-k] = 1 - arr[i-1-k] 
                    arr[i-1+k] = 1 - arr[i-1+k]


    print(f'#{tc}', *arr)