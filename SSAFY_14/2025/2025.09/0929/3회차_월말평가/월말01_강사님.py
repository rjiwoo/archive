T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]
    graph_filter = [list(map(int, input().split())) for _ in range(M)]
    answer = [[0]*(N-M+1) for _ in range(N-M+1)]

    # 우리는 어디를 채우고 있는가?
    for r in range(N-M+1):
        for c in range(N-M+1):
            
            temp = 0
            # 여기에 어떤 값을 채울까?
            for i in range(M):
                for j in range(M):
                    temp += graph[r+i][c+j] * graph_filter[i][j]
            answer[r][c] = temp

    print(f'#{tc}')
    for i in range(N-M+1):
        print(*answer[i])