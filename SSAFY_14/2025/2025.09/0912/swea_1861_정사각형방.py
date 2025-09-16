# swea 1861. 정사각형 방

# 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다
# 상하좌우로 움직여야함

# 처음 출발해야하는 방 번호, 최대 몇 개의 방을 이동할 수 있는지
# 이동할 수 있는 방의 개수가 최대인 방이 여러개면 그 중에서 적힌 수가 가장 작은 것 출력 

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방 번호가 담겨있는 좌표 위치 저장
    room_num = [[-1,-1] for _ in range(N*N+2)]

    for r in range(N):
        for c in range(N):
            room_num[arr[r][c]] = [r, c]
    # print(room_num)

    # 방 번호
    room = 0
    count = 1 # 이동횟수(자기방 포함)
    max_count = 0 # 최대이동횟수?
    start = 0

    for i in range(1, N*N+1):
        if abs(room_num[i][0]-room_num[i+1][0]) + abs(room_num[i][1]-room_num[i+1][1]) == 1:
            if count == 1:
                start = i # 시작점을 체크, 연속이니까
            count += 1

        else: # 여기서 else가 맞나?
            if max_count < count:
                max_count = count
                room = start
            count = 1   # 자기방 포함

    print(f'#{tc} {room} {max_count}')