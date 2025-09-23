# 백준 4179번 불!

# 미로에서 지훈이의 위치와 불이 붙은 위치를 파악해서 불에 타기 전에 탈출할 수 있는지 여부, 
# 얼마나 빨리 탈출할 수 있는지 결정

# 지훈이와 불은 매 분마다 한칸씩 이동(상하좌우만 가능)
# 불은 각 지점에서 상하좌우로 확산됨

# 지훈이는 미로의 가장자리에 접한 공간에서 탈출 가능
# 지훈, 불은 벽이 있는 공간은 통과X

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간

R, C = map(int, input().split()) # 행의 개수, 열의 개수
graph = [list(input()) for _ in range(R)]

start_position = 
for r in range(R):
    for c in range(C):
        if graph[r][c] == 'J':
            start_position.append((i, j, 0))
# 지훈이가 먼저 움직여야 함. 불이 먼저 움직이거나 동시에 움직이면 불에 탐.

escape = []

for i in range(R):
    if graph[0][i] == '.':
        escape.append((0, i))
    if graph[R-1][i] == '.':
        escape.append((R-1, i))
for r in range(R):
    for c in range(C):
        if graph[r][c] == '.':
            escape.append((r,c))