# # 상, 하, 좌, 우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     N = int(input()) # N*N
#     arr = [list(input()) for _ in range(N)]
#     answer =''
#
#     for r in range(N-5+1):
#         for c in range(N-5+1):
#             if arr[r][c] == 'o':
#
#                 r_count = 0
#                 c_count = 0
#                 for i in range(5):
#                     # 가로 오목 확인
#                     if arr[r+i][c] == 'o':
#                         r_count += 1
#                     if r_count == 5:
#                         answer = 'YES'
#                         break
#
#
#                     # 세로 오목 확인
#                     if arr[r][c+i] == 'o':
#                         c_count += 1
#                     if c_count == 5:
#                         answer = 'YES'
#                         break
#
#
#     print(f'#{tc} {answer}')

dy = [1, 0, 1, -1] # 아래, 오른쪽, 오른쪽 아래 대각선, 왼쪽 아래 대각선
dx = [0, 1, 1, 1]

def is_omok():

    for y in range(n): # 행 우선 순회
        for x in range(n):
            if arr[y][x] == 'o': # 돌 하나 발견
                for i in range(4): # 4방향
                    ny, nx = y, x
                    cnt = 0

                    while 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 'o':
                        cnt += 1 # 돌의 개수마다 counting
                        ny += dy[i]
                        nx += dx[i]
                    if cnt >= 5: # 오목이다.(돌이 5개 이상이다)
                        return 'YES'
    return 'NO' # 모든 경우에서 돌이 5개 이상이 아니다 -> 'NO'

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [input() for _ in range(n)] # 왜 map 함수 안썼을까? map함수의 역할 : 정수로 바꿔주는 역할

    result = is_omok()
    print(f'#{tc} {result}')
