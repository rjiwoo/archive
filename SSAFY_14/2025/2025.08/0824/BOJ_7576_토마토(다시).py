# 백준 7576번 토마토

# N*M배열
# 인접한 토마토 영향 받아서 익음
# 토마토가 모두 익게 되는 최소 일수 구하기 -> 최소일수 =DFS

# 1 토마토 익음, 0 안익음, -1 토마토 없음

# 토마토 모두 익으면 0 출력
# 토마토 모두 안익으면 -1

# 토마토는 동시에 익을 거야.

from collections import deque

M, N = map(int,input().split()) # 상자 N*M
arr = [list(map(int, input().split())) for _ in range(N)] # 토마토 정보

# 익은 토마토 있는 곳 찾기
tomato = deque()
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            tomato.append((r,c)) # 익은 토마토 위치 저장

# 토마토가 익는데까지 걸린 시간 저장
visited = [[0]*M for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# tomato가 있으면,,
while(tomato):
    current_r, current_c = tomato.popleft()

    for i in range(4):
        next_r = current_r + dr[i]
        next_c = current_c + dc[i]

        # 상하좌우를 봤을 때, 범위 안에 포함되고
        # 안익은 토마토이고 == 0
        # 방문하지 않은 곳이면
        if 0<=next_r<N and 0<=next_c<M and arr[next_r][next_c] == 0 and visited[next_r][next_c] == 0:
            arr[next_r][next_c] = 1 # 익은 토마토로 바꾸고
            tomato.append((next_r,next_c)) # 가야하는 토마토로 추가하기@!!!!!!
            visited[next_r][next_c] = visited[current_r][current_c] + 1 # 토마토가 익을 때까지 걸린 시간 누적해서 저장

day = 0

# 토마토 익은 날짜 중에 제일 큰 수가 모두 익을 때까지의 최소 일수
day = max(map(max,visited)) 

for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            day = -1
            break
    if day == -1:
        break

print(day)

