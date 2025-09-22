# 백준 1600번 말이 되고픈 원숭이

# 말은 격자판에서 체스의 나이트와 같은 이동방식. 대각선 이동
# 말은 장애물을 뛰어넘을 수 있음

# 원숭이는 대각선 이동은 K번만 가능
# 그 이후에는 인접한 칸으로만 이동(상하좌우)

# 시작지점 (0,0) 도착지점 (H-1, W-1)
# 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법의 수 출력
# 갈 수 없을 경우에는 -1 

# 0 : 평지, 1 : 장애물 

from collections import deque

# 대각선 이동
# 우상향1, 우상향2, 우하향1, 우하향2, 좌하향1, 좌하향2, 좌상향1, 좌상향2
cross_dr = [-2, -1, 1, 2, -2, -1, 1, 2]
cross_dc = [1, 2, 2, 1, -1, -2, -2, -1]


# 인접칸 이동
# 상,하,좌,우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, move):
    q = deque()
    q.append((sr,sc, move))  # 시작점 넣기
    visited[sr][sc][move] = 1 # 시작점도 방문체크(맨처음 이동하는 것을 체크해서 나중에 결과값에서 빼기)

    while q:
        cur_r, cur_c, move_dir = q.popleft()

        if cur_r == H-1 and cur_c == W-1:
            return visited[cur_r][cur_c][move_dir] - 1
        
        # 대각선 이동 횟수가 남아 있으면
        if move_dir < K:
            for i in range(8):
                nr = cur_r + cross_dr[i]
                nc = cur_c + cross_dc[i]
                
                # 범위를 벗어나지 않고
                if 0 <= nr < H and 0 <= nc < W:
                    # 이동할 수 있고, 방문하지 않았으면
                    if graph[nr][nc] == 0  and visited[nr][nc][move_dir + 1] == 0:
                        visited[nr][nc][move_dir + 1 ] = visited[cur_r][cur_c][move_dir] +1
                        q.append((nr, nc, move_dir + 1))
        
        # 인접방향 이동
        for j in range(4):
            nr = cur_r + dr[j]
            nc = cur_c + dc[j]

            if 0 <= nr < H and 0 <= nc < W:
                if graph[nr][nc] == 0  and visited[nr][nc][move_dir] == 0:
                    visited[nr][nc][move_dir] = visited[cur_r][cur_c][move_dir] + 1
                    q.append((nr, nc, move_dir))

    return -1

K = int(input()) # 대각선 이동 가능 방향
W, H = map(int, input().split()) # 가로, 세로
graph = [list(map(int, input().split())) for _ in range(H)] 

visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
print(bfs(0,0,0))