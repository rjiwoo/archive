# 백준 2468번 안전영역
# 지역의 높이 파악 후, 그 지역에 비가 많이 내렸을 때 물에 잠기지 않는 영역이 최대 몇 개인지

# 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태
# 상하좌우로 연결되어 있으면 이어져서 영역 하나

## 문제를 똑바로 읽기!!!! ##
## 비의 양을 다르게 조사해보면서 영역의 최대 개수 찾는거임!! ##
# 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우

from collections import deque

def bfs(r,c,h):
    global count
    q = deque()
    q.append([r,c])
    visited[r][c] = True
    count = 1

    while q:
        current_r, current_c = q.popleft()
        for k in range(4):
            next_r = current_r + dr[k]
            next_c = current_c + dc[k]

            if 0 <= next_r < N and 0 <= next_c < N and graph[next_r][next_c] > h and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                q.append([next_r,next_c])
                count += 1

    return count

# N*N배열
N = int(input()) # 크기의 영역이자 N이상의 높이만 잠기지 않음?
# 구역의 최대 높이 
max_height = 0
graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    max_height = max(max_height, max(row))
    graph.append(row)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0

for h in range(max_height):

    visited = [[False]*N for _ in range(N)]
    safe_zone = 0

    for r in range(N):
        for c in range(N):
            if graph[r][c] > h and not visited[r][c]:
                bfs(r,c,h)
                safe_zone += 1

    ans = max(ans, safe_zone)

print(ans)