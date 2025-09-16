# 백준) 7단계. 2차원 배열 - 2738번. 행렬 덧셈
# 2차원 빈 배열 만들기 숙지 필요
# 2차원 배열 입력 받는법 숙지 필요

# N행, M열
N, M = list(map(int, input().split()))

# arr = []
# for i in range(N):
#     arr.append([0] * M)
# print(arr)

# A = [[0]*M for _ in range(N)]
# B = [[0]*M for _ in range(N)]

# 2차원으로 입력 받기
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

C = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        C[r][c] = A[r][c] + B[r][c]

for r in C:
    print(*r)