T = 10

for tc in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점 찾기
    for i in range(100):
        if ladder[99][i] == 2:
            end = i
    
    # 위, 오른쪽, 왼쪽
    dr = [-1, 0, 0]
    dc = [0, 1, -1]


    # 현재 위치 (행 = x, 열 = y) (답안은 열의 값을 원함)
    r = 99
    c = end

    # 거꾸로 올라가서 0행이 될때까지?
    while r > 0:
    
        # 왼쪽 이동
        if c > 0 and ladder[r][c-1] == 1:
            while c > 0 and ladder[r][c-1] == 1: # 왼쪽이 계속 1이면
                c -= 1 # 왼쪽으로 이동
            r -= 1 # 왼쪽 이동 다 하고 위로 올라가기
        
        # 오른쪽 이동
        elif c < 99 and ladder[r][c+1] == 1:
            while c < 99 and ladder[r][c+1] == 1:
                c += 1
            r -= 1

        # 위
        else:
            r -= 1

    print(f'#{tc} {c}')