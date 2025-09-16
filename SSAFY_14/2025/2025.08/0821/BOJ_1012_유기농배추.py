# 백준 1012 유기농 배추

# 지렁이가 갈 수 있는 곳은 모두 보호받음
# 4방향에 위치한 경우에 서로 인접

# 0: 배추 없음, 1 :배추 있음

# 1로 연결되어 있는 공간 작성

from collections import deque

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # M*N 크기의 밭, 배추 위치K(개수) 

    arr = [[0]*M for _ in range(N)]

    # x가 열, y가 행
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    # 일단, 1이 있는 곳을 방문해야하는 곳으로 체크해두고
    # 하나를 선택해서 (선택할 때, 지렁이 카운트 +1)
    # 찾으면 1이 연결된 곳 찾으면서 이동
    # 1이 끊길 때까지 1 찾기. 
    # 1이 연결된 곳은 방문해야하는 곳에서 삭제

    count = 0

    # 밭 전체를 순회
    for i in range(N):
        for j in range(M):
            # 만약 배추가 있고 아직 방문하지 않았다면
            if arr[i][j] == 1:
                # 새로운 그룹을 찾았으므로 count +1
                count += 1

                # BFS
                q = deque([(i, j)])
                # 시작점 방문 처리
                arr[i][j] = 0

                while q:
                    # 큐에서 popleft()로 원소를 꺼냄
                    curr_y, curr_x = q.popleft()

                    # 4방향 탐색
                    for k in range(4):
                        ny = curr_y + dr[k]
                        nx = curr_x + dc[k]

                        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
                            arr[ny][nx] = 0       # 방문 처리
                            q.append((ny, nx))    # 큐에 추가

    print(count)



            

    