# 백준 14502번 연구소

# 연구소 크기가 N×M인 직사각형
# 직사각형은 1×1 크기의 정사각형

# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지
# 일부 칸은 바이러스가 존재
# 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역

# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램

def dfs(sr, sc, visited):
    visited[sr][sc] = 1 # 방문표시

    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]

        # 범위를 벗어나지 않고
        if 0 <= nr < N and 0 <= nc < N:
            if graph[nr][nc] == 0 and visited[nr][nc] == 0:
                graph[nr][nc] = 2
                visited[nr][nc] = 1
                dfs(nr,nc)


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def comb(count, idx):
    if count == 3:
        # print(picked)

        # 선택한 조합의 위치에 벽 세우기
        for i in range(len(picked)):
            graph[picked[i][0]][picked[i][0]] = 1
        
        visited = [[0]*N for _ in range(N)]
        # 조합에 맞게 변형된 연구소의 지도에서 바이러스를 퍼뜨려
        for r in range(N):
            for c in range(N):
                # 바이러스이고, 방문하지 않은 위치라면
                if graph[r][c] == 2 and visited[r][c] == 0:
                    dfs(r, c)
                    for k in range(N):
                        for h in range(N):
                            
        return
    
    for i in range(idx, len(block)):
        picked.append(block[i])
        comb(count + 1, i + 1)
        picked.pop()



# 세로, 가로
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = N*N    # 안전 영역 크기의 최댓값(배열의 크기를 넘지 못함)

# 벽을 3개 세울 건데, 어디다가 세우느냐에 따라서 바이러스 퍼지는게 달라짐
# 그러면 하나씩 다 세워보고 -> 빈 칸 위치 구해서 조합으로 3개 선정
# -> 새로운 벽이 생긴 연구소의 지도가 조합의 결과만큼 나옴
# 그 때마다 한바퀴 돌면서 
# 바이러스를 일단 퍼뜨리고 -> dfs 모양으로 바이러스가 퍼지는 것.
# 바이러스가 다 번진 상태로 안전 영역의 크기를 카운트
# 최댓값이 나올 때마다 갱신하기.

# 빈칸의 위치를 저장해둘 곳
block = []
for r in range(N):
    for c in range(N):
        if graph[r][c]:
            block.append((r,c))

# print(block)
picked = []
comb(0,0)


