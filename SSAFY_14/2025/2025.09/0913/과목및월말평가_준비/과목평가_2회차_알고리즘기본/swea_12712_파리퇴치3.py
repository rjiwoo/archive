# swea 12712번 파리퇴치3

# 상, 하, 좌, 우
move_1 = [[-1,0],[1,0],[0,-1],[0,1]]

# 오른쪽 위, 오른쪽 아래, 왼쪽 아래, 왼쪽 위
move_2 = [[-1,1],[1,1],[1,-1],[-1,-1]]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for r in range(N):
        for c in range(N):
            
            # 십자가 모양
            temp = arr[r][c]
            for i in range(4):
                for j in range(1,M):
                        new_r = r + move_1[i][0]*j
                        new_c = c + move_1[i][1]*j

                        if 0 <= new_r < N and 0 <= new_c < N:
                            temp += arr[new_r][new_c]
            if max_value < temp:
                max_value = temp
            
            # 엑스자 모양
            temp_2 = arr[r][c]
            for i in range(4):
                for j in range(1,M):
                    new_r = r + move_2[i][0]*j
                    new_c = c + move_2[i][1]*j

                    if 0 <= new_r < N and 0 <= new_c < N:
                        temp_2 += arr[new_r][new_c]
            if max_value < temp_2:
                max_value = temp_2

    print(f'#{tc} {max_value}')