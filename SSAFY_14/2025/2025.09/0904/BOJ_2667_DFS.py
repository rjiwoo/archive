# 백준 2667번 단지 번호 붙이기 - DFS

# 정사각형 모양의 지도가 있음
# 1 : 집 / 0 :  집 없음
# 집이 연결되어 있다는 건 상하좌우
# 총 단지가 몇 개 있는지 출력하고, 각 단지에 몇개의 집이 있는지 오름차순으로 정렬하여 출력

def dfs(start_r, start_c):
    global home_count

    home_count += 1
    visited[start_r][start_c] = 1

    # 현재 집 포함

    for i in range(4):
        next_r = start_r + dr[i]
        next_c = start_c + dc[i]

        if 0 <= next_r < N and 0 <= next_c < N and graph[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
            # visited[next_r][next_c] = 1
            dfs(next_r, next_c)

    return None


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

danji = []

# 상,하,좌,우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and visited[r][c] == 0:
            home_count = 0
            dfs(r, c)
            danji.append(home_count)

danji.sort()
print(len(danji))
for i in danji:
    print(i)
