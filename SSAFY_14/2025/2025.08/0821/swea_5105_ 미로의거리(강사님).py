# 강사님 코드

from collections import deque

dr = [-1, 1, 0, 0]
dc = [ 0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = []
    answer = -1 # 도착까지 가는데 만나는 0의 수
    # 도착까지 가는 경로의 수
    # 도착까지 가는데 걸리는 걸음 수
    # 도착까지 가는데 만나는 0의 수

    # 위 3개는 답이 다 달라

    # 입력과 동시에 출발의 위치를 찾고 싶은 것
    start_r , start_c = -1, -1
    for r in range(N):
        temp = list(map(int,input())) # temp 속에 2 가 있는지 없는 궁금함.
        for c in range(N):
            if temp[c] == 2:
                start_r = r
                start_c = c
        graph.append(temp)
    
    # BFS 탐색(이유: 최단경로)

    visited = [[0]*N for _ in range(N)]
    q = deque() 
    
    # 튜플. 데이터로 전송할 때 리스트보다 튜플이 빠름.    
    # 시작점은 변할 일이 없기 때문에 ?
    q.append((start_r,start_c))
    visited[start_r][start_c] = 1

    flag = False # 찾으면 나가고 싶음

    while q:
        
        answer += 1

        for _ in range(len(q)):
            r, c = q.popleft() # q는 방문대기열이니까 갈 수 있는 다음 지점을 찾아야 함

            for dir in range(4):
                next_r = r + dr[dir]
                next_c = c + dc[dir]

                # 아래의 조건을 만족하면 가라
                # 1. 맵 안쪽이어야 한다
                # 2. 1이 아니어야 한다.
                # 3. 방문 안했어야 한다
                # if 0<=next_r<N and 0<=next_c<N and graph[next_r][next_c] != 1 and not visited:

                # 위 조건 중 하나라도 만족하지 않으면 가지 마라

                # 이 중 하나라도 만족하면 다음 방향을 보세요
                # 1. 맵 바깥쪽이거나
                # 2. 1이거나
                # 3. 방문했거나
                if next_r<0 or next_c<0 or next_r>=N or next_c >= N or graph[next_r][next_c] == 1 or visited[next_r][next_c]:
                    continue

                if graph[next_r][next_c] == 3:
                    flag = True
                    break

                visited[next_r][next_c] = 1
                q.append((next_r, next_c))

            if flag:
                break
        if flag:
            break

    if not flag:
        answer = 0

    print(f'#{tc} {answer}')
