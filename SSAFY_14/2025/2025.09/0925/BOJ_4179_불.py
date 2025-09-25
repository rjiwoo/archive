# 백준 4179번 불

# 지훈이가 불에 타기 전에 탈출할 수 있는지 여부, 얼마나 빨리 탈출할 수 있는지
# 이동은 상하좌우 가능
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출 가능

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간

# 탈출 못하면 IMPOSSIBLE 을 출력
# 탈출할 수 있는 경우에는 가장 빨른 탈출시간을 출력
# --> 최단거리를 확인할거니까 bfs

from collections import deque

# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int,input().split()) # 행, 열 
graph = [list(input()) for _ in range(R)]
# print(graph)
answer = 0

JH = deque() # 지훈이의 위치 저장
fire = deque() # 불의 위치 저장

visited = [[-1]*C for _ in range(R)] # 지훈이의 방문 체크
fire_visited = [[-1]*C for _ in range(R)] # 불 위치의 방문체크

for r in range(R):
    for c in range(C):
        if graph[r][c] == 'J':
            visited[r][c] = 0 # 지훈이의 처음 방문 위치 체크
            JH.append((r,c))

            # 시작 위치가 가장자리면 바로 탈출 가능
            if r == 0 or r == R-1 or c == 0 or c == C-1:
                print(1)
                exit()

        if graph[r][c] == 'F':
            fire_visited[r][c] = 0 # 처음 불의 위치를 체크
            fire.append((r,c))


# 불 먼저 이동하는 것을 모두 fire_visited에 체크해두기(몇 초 뒤에 불이 확산되는지도 체크해두기)
while fire:
    sr, sc = fire.popleft() # 불의 위치를 pop

    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]

        # 불의 다음 위치가 범위 안이고, 벽이 아니고, 방문하지 않은 곳이라면
        if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != '#' and fire_visited[nr][nc] == -1:
            fire_visited[nr][nc] = fire_visited[sr][sc] + 1 # 처음 위치에서 다음 불 위치까지 걸리는 시간 누적
            fire.append((nr,nc))        # 불 다음 위치 추가

# 지훈이의 이동 확인
while JH:
    sr, sc = JH.popleft()

    # 지훈이가 가장자리에 도착하면 탈출 성공
    if sr == 0 or sr == R-1 or sc == 0 or sc == C-1:
        answer = visited[sr][sc] + 1
        break

    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]

        # 지훈이의 다음 위치가 범위 안이고, 벽이 아니고, 지훈이가 방문하지 않은 곳이고
        # 같은 시간에 불이 그 곳에 확산되어 있지 않는다면?
        # --> 거기까지 가는 곳의 누적된 값이 불보다 작아야 이동 가능한 것 !! *이걸 생각하기가 어려웠음
        if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != '#' and visited[nr][nc] == -1:
            visited[nr][nc] = visited[sr][sc] + 1

            # 틀린 원인 1 : 불이 아예 도달하지 않을 곳일 경우를 생각하지 않고 진행함
            # 불보다 먼저 도달할 수 있거나, 불이 아예 도달하지 않는 곳일 경우
            if fire_visited[nr][nc] == -1 or visited[nr][nc] < fire_visited[nr][nc]:
                JH.append((nr,nc))

if answer:
    print(answer)
else:
    print("IMPOSSIBLE")