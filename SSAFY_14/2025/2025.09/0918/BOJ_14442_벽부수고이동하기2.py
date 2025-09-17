# 백준 14442번 벽 부수고 이동하기2

# N×M의 행렬
# 0 : 이동가능, 1: 벽
# (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 
# 벽을 K개 까지 부수고 이동하여도 된다.

# 최단 경로 = 가장 적은 개수의 칸을 지나는 경로 (불가능할 때는 -1 출력)
# 시작하는 칸과 끝나는 칸도 포함
# 이동할 수 있는 곳 : 상하좌우 인접한 칸

# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 
# 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. 
# (1, 1)과 (N, M)은 항상 0이라고 가정

from collections import deque

## 시간초과 떠서 입력 받는거 바꾸고, pypy로 돌림
## python으로는 어떻게 해야 시간 초과가 안될까?
import sys

input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        r, c, broken = q.popleft()

        if r == N-1 and c == M-1:
            return visited[r][c][broken]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위를 벗어나지 않고
            if 0 <= nr < N and 0 <= nc < M:
                # 벽이 아니고, 방문하지 않았으면
                if graph[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                    visited[nr][nc][broken] = visited[r][c][broken] + 1
                    q.append((nr, nc, broken))
                
                # 벽이고, 방문하지 않았는데, 부술 수 있는 횟수가 남아있으면
                elif graph[nr][nc] == 1 and broken < K and visited[nr][nc][broken + 1] == 0:
                    visited[nr][nc][broken + 1] = visited[r][c][broken] + 1
                    q.append((nr, nc, broken + 1))

    return -1


N, M, K = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
print(bfs())