# SWEA 5188번. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

# N*N칸
# 오른쪽이나 아래로만 이동 가능
# 맨 왼쪽에서 오른쪽 아래까지 이동할 때, 숫자의 합계가 최소가 되도록 움직였다면
# 합계가 얼마인지 출력


from collections import deque

# 이동방향(오른쪽, 아래)
dr = [0, 1]
dc = [1, 0]

def dfs(start_r, start_c, cur_sum):
    global answer
    
    # 종료조건 : 오른쪽 맨 아래에 도착하면
    if start_r == N-1 and start_c == N-1:
        answer = min(answer,cur_sum)
        return 
    
    if cur_sum >= answer:
        return
    
    for i in range(2):
        nr = start_r + dr[i]
        nc = start_c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        dfs(nr, nc, cur_sum + arr[nr][nc])
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 21e9

    # 해당 위치에 오기까지의 최소값을 저장해둔다면, 도착지 자리까지 오는데 걸리는 최소값을 알 수 있지 않을까?
    # => 메모이제이션 ? : 이전 값을 저장해두고 쓰는 거니까
    # 아니면, dfs로 하나로 쭉 가다가 최소값보다 크면 그만 가는거지
    
    # (0,0)에서 시작하고, 시작점의 값(arr[0][0])을 초기 합계로 전달
    dfs(0, 0, arr[0][0])

    print(f'#{tc} {answer}')