# 백준 2667번 단지 번호 붙이기 - BFS로 풀음

# 정사각형 모양의 지도가 있음
# 1 : 집 / 0 :  집 없음
# 집이 연결되어 있다는 건 상하좌우
# 총 단지가 몇 개 있는지 출력하고, 각 단지에 몇개의 집이 있는지 오름차순으로 정렬하여 출력

from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

# 상,하,좌,우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 집이 있는지 없는지를 돌면서 체크
# 예를 들어서, 1이 있는 곳에서 시작을 해 (첫 시작이 단지 개수 +1)
# 상하좌우를 확인하면서 집이 있으면 그곳으로 이동하는거지. (집의 개수 +1)
# 그리고 내가 그 집을 갔으면 0으로 변경해서 다시 안들리게 하자.
# visited 를 쓰는게 나을까? 아니면 그냥 0으로 다 변경해서 안가게 할까
# visited 를 쓰자. 그게 정석이니까....

# 단지 수
danji = 0

# 단지 별 집의 개수
home_count_list = []

# 방문 체크 (graph 크기와 똑같이 만들어서 그곳을 방문했는지 체크)
visited = [[0]*N for _ in range(N)]

# 첫 시작을 어떻게 잡을거야?
# 1. 집이 있고
# 2. 방문하지 않을 때 첫 시작..?
# 그러면 첫 시작이 단지의 시작이라서 +1 할건데 이건 어케 표현해야하지
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and visited[r][c] == 0:
            start_r = r
            start_c = c

            # 집이 있는 곳을 발견했으니까 이게 단지의 시작
            danji += 1

            # q는 내가 가야할 곳을 넣어놓는 곳? q를 정확하게 어떻게 표현해야할지 모르겠다.
            q = deque()
            q.append([start_r, start_c])
            visited[start_r][start_c] = 1   # 첫 시작도 방문처리 해줘야 함

            # # 단지 안에 들어있는 집의 수 세기
            # 왜 0이어야해? 시작점도 단지 안에 속하는거니까 집의 개수 카운트하는거 아닌가?
            home_count = 1

            while q:
                # 현재 위치를 q에서 꺼내
                cur_r, cur_c = q.popleft()

                # 현재 위치에서 상,하,좌,우를 확인해서 인접하면 가야하니까 (인접하면 같은 단지)
                for i in range(4):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]

                    # 다음으로 이동하는 곳이 1.범위 안에 있고, 2.집이 있고, 3.방문하지 않았어야해
                    # 그러면 이동할 수 있는거니까 q에 가야할 곳으로 append 하기
                    if 0 <= next_r < N and 0 <= next_c < N and graph[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
                        q.append([next_r, next_c])
                        visited[next_r][next_c] = visited[cur_r][cur_c] + 1
                        home_count += 1
                        # print(home_count, next_r, next_c)


            home_count_list.append(home_count)

print(danji)
home_count_list.sort()  # 각 단지에 속하는 집의 수를 오름차순으로 정렬
for i in home_count_list:
    print(i)
