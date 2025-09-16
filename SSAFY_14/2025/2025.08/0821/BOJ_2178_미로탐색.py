# 백준 2178번 미로 탐색

# N×M크기의 배열로 표현되는 미로
# 미로에서 1은 이동 가능 칸, 0은 이동할 수 없는 칸을 나타낸다. 
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 
# 지나야 하는 최소의 칸 수를 구하는 프로그램

# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함

# => 최소의 칸 수를 구하는 거니까 BFS -> '큐'로 구현?

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

count = 0

q = deque([(0,0)]) # 첫 시작점을 큐에 넣음

# BFS 탐색
while q:
    x, y = q.popleft() # 현재 위치

    # 상하좌우 확인하면서 인덱스 벗어나지 않고, 1인 경우만 이동
    for i in range(4):
        next_r = x + dr[i]
        next_c = y + dc[i]
        if 0<=next_r<N and 0<=next_c<M and graph[next_r][next_c] == 1:
            # x = next_r
            # y = next_c
            q.append((next_r,next_c)) # 이동 가능하면 다음 위치를 큐에 삽입

            # 다음 위치에 거리를 기록
            # 현재 위치 (x,y)까지 오는 데 걸린 칸의 수(graph[x][y])에 1을 더해서 다음 위치 (next_r, next_c)에 저장
            graph[next_r][next_c] = graph[x][y] + 1

print(graph[N-1][M-1])






#####################################
#### BFS 정석 #######################
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 방문 및 거리 기록을 위한 배열을 생성하고 모두 0으로 초기화
visited = [[0] * M for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1 # 시작점의 거리는 1

    while q:
        curr_x, curr_y = q.popleft()

        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]

            # 다음 위치가 미로 범위 안에 있는지 확인
            if 0 <= next_x < N and 0 <= next_y < M:
                # 1. 아직 방문하지 않았고(visited[next_x][next_y] == 0)
                # 2. 이동할 수 있는 길이라면(graph[next_x][next_y] == 1)
                if visited[next_x][next_y] == 0 and graph[next_x][next_y] == 1:
                    # 이전 칸의 거리 + 1을 기록
                    visited[next_x][next_y] = visited[curr_x][curr_y] + 1
                    q.append((next_x, next_y))

    # 최종 목적지까지의 거리를 반환
    return visited[N-1][M-1]

print(bfs(0, 0))