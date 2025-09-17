# 백준 2206번 벽 부수고 이동하기

# N×M의 행렬
# 0 : 이동가능, 1: 벽
# (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 
# 벽을 한 개 까지 부수고 이동하여도 된다.

# 최단 경로 = 가장 적은 개수의 칸을 지나는 경로 (불가능할 때는 -1 출력)
# 시작하는 칸과 끝나는 칸도 포함
# 이동할 수 있는 곳 : 상하좌우 인접한 칸

# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 
# 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. 
# (1, 1)과 (N, M)은 항상 0이라고 가정

from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0,0,0))         # r, c, 벽을 부쉈는지 여부 (0: 안 부숨, 1: 부숨)
    visited[0][0][0] = 1    # 시작 위치에서 벽 안 부순 상태
    
    while q:
        cur_r, cur_c, broken = q.popleft()


        # BFS 특성상 최단거리부터 탐색하므로, 
        # (N-1, M-1)에 첫 도착 순간이 최단 경로. 이 때의 visited 값이 답이 됨
        if cur_r == N-1 and cur_c == M-1:
            return visited[cur_r][cur_c][broken]

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 범위를 벗어나지 않고 
            if 0 <= nr < N and 0 <= nc < M:
                # 벽이 아니고, 방문하지 않은 곳이면
                if graph[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                    visited[nr][nc][broken] = visited[cur_r][cur_c][broken] + 1
                    q.append((nr,nc, broken))
                
                # 벽인데 아직 안 부쉈을 때 -> 벽을 부숨
                elif graph[nr][nc] == 1 and broken == 0 and visited[nr][nc][1] == 0:
                    visited[nr][nc][1] = visited[cur_r][cur_c][0] + 1
                    q.append((nr, nc, 1))

    return -1   # 마지막에 도달하지 못하면 -1

# 첫번째 시작이 (1,1) -> 입력 받을 때는 시작이 (0,0)이라는거 기억하기 
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 시작 (0,0) 
# 끝 (N-1, M-1)

# print(graph)

# 최단경로니까 BFS

# 벽을 부술 수 있으니까, 해당 상태를 저장해야함.
# 벽을 부순 상태 / 안 부순 상태를 구분 -> visited를 3차원으로 구성?

# visited[r][c][0] -> 벽 안 부수고 도달한 경우
# visited[r][c][1] -> 벽 부수고 도달한 경우
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs())
