# 백준 4179번 불!

# 미로에서 지훈이의 위치와 불이 붙은 위치를 파악해서 불에 타기 전에 탈출할 수 있는지 여부, 
# 얼마나 빨리 탈출할 수 있는지 결정

# 지훈이와 불은 매 분마다 한칸씩 이동(상하좌우만 가능)
# 불은 각 지점에서 상하좌우로 확산됨

# 지훈이는 미로의 가장자리에 접한 공간에서 탈출 가능
# 지훈, 불은 벽이 있는 공간은 통과X

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간

from collections import deque

# 지훈이는 상하좌우로 움직일 수 있음 
# 불이 상하좌우로 확산됨
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    q = deque()
    q.append((sr,sc))   # 첫 시작점 넣기
    visited[sr][sc] = 1

    # 지훈이가 탈출하기 전까지?
    while q:
        cur_r, cur_c = q.popleft()

        for dir in range(4):
            nr = cur_r + dr[dir]
            nc = cur_c + dc[dir]
            
            # 지훈이의 다음 위치가 범위 안이고, 벽이 아니고, 방문하지 않은 공간이고, 불이 없어야 함
            if 0 <= nr < R-1 and 0 <= nc < C-1 and graph[nr][nc] != '#' and graph[nr][nc] != 'F' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[cur_r][cur_c] + 1
                q.append((nr,nc))

            # 그런데 문제점은 지훈이가 불이 없다고 생각해서 이동했는데, 그곳에 불이 번질 경우는?

        for _ in range(len(fire_position)):
            i, j = fire_position.popleft()
            for dir in range(4):
                ni = i + dr[dir]
                nj = j + dc[dir]

                # 다음 불의 위치가 범위 안이고, 이동가능하면(벽이 아니고, 불이 아니면)
                if 0 <= ni < R-1 and 0 <= nj < C-1 and graph[ni][nj] == '.':
                    fire_position.append((ni, nj))  # 불의 위치를 추가하고
                    graph[ni][nj] = 'F' # 불로 맵을 변경하기?





R, C = map(int, input().split()) # 행의 개수, 열의 개수
graph = [list(input()) for _ in range(R)]

# 시작점의 위치를 체크 (지훈이 위치, 불 위치)
start_position = [] # 지훈이 위치
fire_position = deque()  # 불 위치
for r in range(R):
    for c in range(C):
        if graph[r][c] == 'J':
            start_position.append((r,c))
        if graph[r][c] == 'F':
            fire_position.append((r,c))

# 지훈이가 먼저 움직여야 함. 불이 먼저 움직이거나 동시에 움직이면 불에 탐?

# 지훈이가 얼마나 빨리 탈출할 수 있는지를 결정하는 것이기 때문에 최단경로로? BFS로 보는게 좋을듯
visited = [[0]*C for _ in range(R)] # 방문체크 (지훈이가 왔던 길인지 확인하기 위해서)


