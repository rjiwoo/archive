# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [ 0, 0, -1, 1]


T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N*N배열

    graph = [list(map(int, input().split())) for _ in range(N)]

    monster_r = -1
    monster_c = -1
    answer = 0

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 2:
                monster_r = r
                monster_c = c
    

    for i in range(4):
        next_r = monster_r + dr[i]
        next_c = monster_c + dc[i]

        while(0 <= next_r < N and 0 <= next_c < N and graph[next_r][next_c] == 0):
            graph[next_r][next_c] = 1

            next_r += dr[i]
            next_c += dc[i]
        
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 0:
                answer += 1


    print(f'#{tc} {answer}')
