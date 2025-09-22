# SWEA 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

# (이거 다시 풀기!!!!)
# N*N 배열
# 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 함
# 세로로 같은 줄에서 두 개의 이상의 숫자를 고를 수 없음

# => 가로 세로 줄에서 하나씩

def dfs(r, c, total):
    global min_answer

    if total >= min_answer:
        return
    
    if r == N:
        min_answer = min(min_answer, total)
        return
    
    for c in range(N):
        if not used_col[c]: # 그 열에 있는 번호를 선택하지 않았다면
            used_col[c] = True
            dfs(r + 1, used_col, total + graph[r][c])
            used_col[c] = False

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    min_answer = float('inf')

    # 조건에 맞게 숫자를 고르는 방법이 뭐가 있을까?
    # 일단 한 줄에서 하나씩 뽑고, 그게 세로에서 겹치지 않는 경우를 뽑아서 최솟값 갱신?
    # 그럼 조합으로 풀면 되지 않을까?
    
    used_col =[False] * N
    dfs(0, used_col, 0)

    print(f'#{tc} {min_answer}')