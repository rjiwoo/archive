# swea 20739번 고대 유적 2

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0

    # 가로행
    for r in range(N):
        r_count = 0
        for c in range(M):
            if graph[r][c] == 1:
                r_count += 1
            else:
                if max_count < r_count:
                    max_count = r_count
                r_count = 0
        if max_count < r_count:
            max_count = r_count

    # 세로행               
    for c in range(M):    
        c_count = 0
        for r in range(N):
            if graph[r][c] == 1:
                c_count += 1
            else:
                if max_count < c_count:
                    max_count = c_count
                c_count = 0
        if max_count < c_count:
            max_count = c_count


    if max_count == 1:
        max_count = 0

    print(f'#{tc} {max_count} ')