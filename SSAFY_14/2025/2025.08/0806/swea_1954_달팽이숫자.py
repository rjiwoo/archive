# 테스트 케이스
T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 달팽이 크기 입력 받기

    snail = [[0]*N for _ in range(N)] # 달팽이 크기만큼 0으로 배열 만들기

    # 오른쪽, 아래, 왼쪽, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    x = 0
    y = 0

    # 오른쪽: 0, 아래: 1, 왼쪽: 2, 위: 3
    move = 0  # 첫 시작은 오른쪽으로 가야하니까

    for i in range(1, N*N+1):
        snail[x][y] = i
        x += di[move]
        y += dj[move]

        # 방향을 바꿔야 하는 조건
        if x < 0 or y < 0 or x >= N or y >= N or snail[x][y] != 0:
            x -= di[move]
            y -= dj[move]   

            # move = 4이면 0으로 변경해야하니까
            move = (move + 1) % 4

            x += di[move]
            y += dj[move]


    print(f'#{tc}')
    for row in snail:
        print(*row)