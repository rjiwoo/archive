# SWEA 1249. [S/W 문제해결 응용] 4일차 - 보급로

# 공병대는 출발지(S) 에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행
# 도로가 파여진 깊이에 비례해서 복구 시간은 증가
# 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.
# 깊이가 1이라면 복구에 드는 시간이 1이라고 가정

# 지도 정보는 그림1(b)와 같이 2차원 배열 형태 표시
# 출발지는 좌상단의 칸(S)이고 도착지는 우하단의 칸(G)

# 이동 경로는 상하좌우 방향으로 진행할 수 있으며, 한 칸씩 움직일 수 있다.

# 지도 정보에는 각 칸마다 파여진 도로의 깊이가 주어진다. 
# 현재 위치한 칸의 도로를 복구해야만 다른 곳으로 이동할 수 있다.

# 출발지(S)와 도착지(G)는 좌상단과 우하단이 되고 입력 데이터에서는 0으로 표시
# 출발지와 도착지를 제외한 곳이 0인 것은 복구 작업이 불필요한 곳

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):

    q = deque()
    q.append((sr,sc))
    visited[sr][sc] = graph[sr][sc] # 시작점 방문체크 겸 걸리는 시간 누적

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 범위를 벗어나지 않았을 때
            if 0 <= nr < N and 0 <= nc < N:

                # 방문한 곳까지 가는 거리에 대한 합이 최소가 아니면?
                # 방문체크를 해서 가지 않게 되면, 그걸 포함했을 때가 더 최소가 될 수도 있으니까?
                # 어라. 그럼 이건 bfs가 아닌가??????/
                if visited[nr][nc] > visited[cur_r][cur_c] + graph[nr][nc]:
                    visited[nr][nc] = visited[cur_r][cur_c] + graph[nr][nc]
                    q.append((nr,nc))


T = int(input())

for tc in range(1, T+1):

    N = int(input())    # 지도의 크기 N*N
    graph = [list(map(int, input())) for _ in range(N)]
    
    visited = [[float('inf')]*N for _ in range(N)]
    bfs(0,0)


    print(f'#{tc} {visited[N-1][N-1]} ')