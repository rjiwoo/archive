T = int(input())

for tc in range(1, T+1):
    N = int(input())

    snail = [[0]*N for _ in range(N)]
    
    # for r in range(N):
    #     for c in range(N):
    #         if r > 0 and c < N and snail[r][c] == 0:
    #             for i in range(1,N**N+1):
    #                 snail[r][c] = i 

    r = 0
    c = 0
    # 오른쪽, 아래, 왼쪽, 위
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    move = 0 # 처음은 오른쪽으로 가기

    for i in range(1, N**N+1):
        snail[r][c] = i
        r += dr[move]
        c += dc[move]

        if r < 0 or c > N or snail != 0:
            move += (move+1) % 4
            
            r += dr[move]
            c += dc[move]

    for row in snail:
        print(*row)


    print(f'#{tc}')