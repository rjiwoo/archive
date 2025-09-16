# 백준 2667번 단지 번호 붙이기

# 정사각형 집
# 1 집 있음, 0 집 없음
# 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙일 것

# 상, 하, 좌, 우로 연결됨
# 출력) 단지 수, 각 단지에 속하는 집의 수를 오름차순으로 정렬


# 지도를 탐색하다가 1이 있으면, 1이 끝날때까지 쫓아가면서 2로 변경
# 그 다음 1이 있으면 3으로 변경, 4로 변경하기
# 변경하면서 해당 번호의 단지수를 count해서 저장하기?
# 나중에 지도를 다시 탐색해서 최대값 구한 다음에 -1 하면 단지 수 

from collections import deque

N = int(input()) # N*N 지도

graph = [list(map(int, input())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 단지 수 체크
count_list = []

# 방문체크
visited = [[False]*N for _ in range(N)]

# 방문해야하는 곳
visit = deque()
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and not visited[r][c]:

            q = deque([(r,c)])
            visited[r][c] = True
            count = 1

            while q:
                # 처음 들려야하는 곳(시작)
                current_r, current_c = q.popleft()

                # 상하좌우를 확인했을 때, 1이 있으며 이동
                for k in range(4):
                    next_r = current_r + dr[k]
                    next_c = current_c + dc[k]
                    if 0<=next_r<N and 0<=next_c<N and graph[next_r][next_c] == 1 and not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        q.append((next_r,next_c))
                        count += 1

            count_list.append(count)
                        

print(len(count_list))

count_list.sort()
for i in count_list:
    print(i)

