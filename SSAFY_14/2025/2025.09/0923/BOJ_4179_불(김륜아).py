# 불!

# #은 벽, J는 지훈, F는 불

from collections import deque

N, M = map(int, input().split())
raw = [input() for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 불과 지훈이 q, visited 만들기
q_fire = deque()
q_JH = deque()
fire_visited = [[-1]*M for _ in range(N)]
JH_visited = [[-1]*M for _ in range(N)]

for i in range(N):
    for j in range(M):

        # 지훈이 위치 append
        if raw[i][j] == 'J':
            # 현재 지훈 위치 0 방문처리
            JH_visited[i][j] = 0
            q_JH.append((i, j))

        # 불 위치 append 
        elif raw[i][j] == 'F':
            # 현재 불 위치 0 방문처리
            fire_visited[i][j] = 0
            q_fire.append((i, j))

# 불이 갈 수 있는 곳 BFS로 visited 채우기
while q_fire:
    i, j = q_fire.popleft()

    for delta in range(4):
        ni = i + di[delta]
        nj = j + dj[delta]

        if 0 <= ni < N and 0 <= nj < M and raw[ni][nj] != '#' and fire_visited[ni][nj] == -1:
            fire_visited[ni][nj] = fire_visited[i][j] + 1
            q_fire.append((ni,nj))


# 지훈이가 탈출할 수 있으면 answer에 답 넣어주기
answer = 0
# 지훈이가 갈 수 있는 곳 visited 채우기
# JH_visited 값이 fire_visited 보다 작으면 지훈이가 안전하게 이동했다는 것을 의미
while q_JH:
    i, j = q_JH.popleft()

    # 지훈이가 가장자리에 도착하면 탈출 성공
    if i == 0 or i == N-1 or j == 0 or j == M-1:
        answer = JH_visited[i][j] + 1
        break

    for delta in range(4):
        ni = i + di[delta]
        nj = j + dj[delta]

        if 0 <= ni < N and 0 <= nj < M and raw[ni][nj] != '#' and JH_visited[ni][nj] == -1:
            JH_visited[ni][nj] = JH_visited[i][j] + 1

            # fire_visited 값보다 작거나 fire_visited == -1 이면 지훈이가 이동 가능
            if JH_visited[ni][nj] < fire_visited[ni][nj] or fire_visited[ni][nj] == -1:
                q_JH.append((ni,nj))

if answer:
    print(answer)
else:
    print("IMPOSSIBLE")