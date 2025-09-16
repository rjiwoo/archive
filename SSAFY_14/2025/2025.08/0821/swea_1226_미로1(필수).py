# bfs 구현
# visited 생성
# 큐 생성
# 시작점 인큐
# 인큐 표시

# 반복
# 디큐
# 방문해서 할일
# 방문정점에서 인접하고 미방문이면
#     인큐
#     인큐 표시

# swea 1226 미로1

def find_index(N):
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = [[i,j]]
    visited[i][j] = 1
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0 :
                q.append([wi, wj])
                visited[wi][wj] = 1
    return 0


# # 상, 하, 좌, 우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]


T = 10

for tc in range(1, T+1):
    input()
    maze = [list(map(int, input())) for _ in range(16)] # 16*16행렬

    start_r, start_c = find_index(16)
    result = bfs(start_r,start_c,16)

    print(f'#{tc} {result}')
    