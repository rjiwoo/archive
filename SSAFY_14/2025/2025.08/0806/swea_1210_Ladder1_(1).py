# 사다리 있는 곳은 1
# 도착 지점은 2
# 도착 지점에 도착하려면 출발을 어디서 해야하는지, x좌표 구하기

T = 10

for tc in range(1,T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 위, 왼쪽, 오른쪽
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    move = 0

    # 도착 지점 인덱스 찾기 arr[99][end]
    for i in range(100):
        if arr[99][i] == 2:
            end = i
    # end = arr[99].index(2)
    x = 99
    y = end

    # x가 0이 될 때까지 거꾸로 올라갑니다.
    while x > 0:
        # 왼쪽으로 사다리가 있는지 확인
        if y > 0 and arr[x][y-1] == 1:
            # 사다리가 끝날 때까지 왼쪽으로 이동
            while y > 0 and arr[x][y-1] == 1:
                y -= 1
            x -= 1 # 왼쪽 이동 후, 위로 한 칸 이동
        # 오른쪽으로 사다리가 있는지 확인
        elif y < 99 and arr[x][y+1] == 1:
            # 사다리가 끝날 때까지 오른쪽으로 이동
            while y < 99 and arr[x][y+1] == 1:
                y += 1
            x -= 1 # 오른쪽 이동 후, 위로 한 칸 이동
        # 좌우에 사다리가 없으면 위로 한 칸 이동
        else:
            x -= 1
    
    print(f'#{tc} {y}')



# 사다리 있는 곳은 1
# 도착 지점은 2
# 도착 지점에 도착하려면 출발을 어디서 해야하는지, x좌표 구하기

T = 10

for tc in range(1,T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 위, 왼쪽, 오른쪽
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    move = 0

    # 도착 지점 인덱스 찾기 arr[99][end]
    for i in range(100):
        if arr[99][i] == 2:
            end = i
    # end = arr[99].index(2)
    y = 99
    x = end

    while y > 0:
        # 왼쪽 사다리 확인
        if x > 0 and arr[y][x - 1] == 1:
            move = 1 # 방향을 '왼쪽'으로 설정
            # 사다리가 끝날 때까지 왼쪽으로 이동
            while x > 0 and arr[y][x - 1] == 1:
                x += dc[move] # 열(x)만 변경
            
        # 오른쪽 사다리 확인
        elif x < 99 and arr[y][x + 1] == 1:
            move = 2 # 방향을 '오른쪽'으로 설정
            # 사다리가 끝날 때까지 오른쪽으로 이동
            while x < 99 and arr[y][x + 1] == 1:
                x += dc[move] # 열(x)만 변경
            
        # 좌우에 사다리가 없거나, 옆 이동이 끝났으면 위로 한 칸 이동
        y += dr[0]


    print(f'#{tc} {x}')



