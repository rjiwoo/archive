# 백준 1913번 달팽이

N = int(input()) # 홀수인 자연수, N*N배열
a = int(input()) # 좌표를 찾을 대상 숫자

# 0으로 채운 N*N 배열 생성
snail = [[0]*N for _ in range(N)] 

# 아래, 오른쪽, 위, 왼쪽
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
move = 0

# (0,0)에서 시작
i = 0
j = 0

# N*N부터 1까지 채울 것.
# 거꾸로 돌면 됨
for k in range(N*N, 0, -1):
    snail[i][j]= k # 첫 시작 N제곱

    # 다음 위치 미리 계산
    ni = i + dr[move]
    nj = j + dc[move]

    # 다음 위치(ni, nj)가 범위를 벗어나거나
    # 이미 값이 채워져 있다면 방향 바꿈
    if ni < 0 or nj < 0 or ni >= N or nj >= N or snail[ni][nj] != 0:
        move = (move + 1) % 4
    
    # 현재 위치를 다음 방향으로 바꿈
    i += dr[move]
    j += dc[move]

# 달팽이 출력
for row in snail:
    print(*row)

# 대상 숫자의 좌표 확인
answer_r = 0
answer_c = 0

for r in range(N):
    for c in range(N):
        if snail[r][c] == a:
            answer_r = r+1
            answer_c = c+1
print(answer_r, answer_c)