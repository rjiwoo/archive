# 백준 15686번 치킨 배달

# 1번. 2중 for문
# 2번. BFS


## 1번 풀이 ##

# from itertools import combinations

# N, M = map(int,input().split())

# graph = [[0] * N for _ in range(N)]
# home_rcs = []
# store_rcs = []
# answer = float('inf')

# for r in range(N):
#     row = list(map(int,input().split()))
#     for c in range(N):
#         graph[r][c] = row[c]
#         if graph[r][c] == 1:
#             home_rcs.append((r, c))
#         elif graph[r][c] == 2:
#             store_rcs.append((r, c))

# # 집-치킨집 거리 미리 계산
# dist_matrix = [[0] * len(store_rcs) for _ in range(len(home_rcs))]
# for home_idx in range(len(home_rcs)):
#     for store_idx in range(len(store_rcs)):
#         hr, hc = home_rcs[home_idx]
#         sr, sc = store_rcs[store_idx]
#         dist_matrix[home_idx][store_idx] = abs(hr - sr) + abs(hc - sc)

# # 치킨집 M개 선택해서 최소 도시 치킨 거리 구하기
# for store_idx_set in combinations(range(len(store_rcs)), M):
#     total_distance = 0
#     for home_idx in range(len(home_rcs)):
#         min_distance = float('inf')
#         for store_idx in store_idx_set:
#             min_distance = min(min_distance, dist_matrix[home_idx][store_idx])
#         total_distance += min_distance
#     answer = min(answer, total_distance)

# print(answer)



# 1부터 시작
# 치킨집의 최대 개수

# M : 폐업시키지 않을 치킨집 최대 개수
# 출력 : 도시의 치킨 거리의 최솟값
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리

# 어떤 경우에 안 뽑아도 되는지
# ㄴ 치킨 거리는 중도 포기가 불가능 

# (단순거리의) 이중포문

from itertools import combinations

N, M = map(int,input().split())

graph = [[0] * N for _ in range(N)]

home_rcs = []
store_rcs = []
answer = float('inf')

for r in range(N):
    row = list(map(int,input().split()))

    for c in range(N):
        graph[r][c] = row[c]

        if graph[r][c] == 1:
            home_rcs.append((r,c))
        elif graph[r][c] == 2:
            store_rcs.append((r,c))

distances = [[0] * len(store_rcs) for _ in range(len(home_rcs))]

for home_idx in range(len(home_rcs)):
    for store_idx in range(len(store_rcs)):

        distances[home_idx][store_idx] = abs(home_rcs[home_idx][0]-store_rcs[store_idx][0]) + abs(home_rcs[home_idx][1]-store_rcs[store_idx][1])

# list(combinations(range(len(store_rcs)) , M)) 절대 쓰지 말아라
for store_idx_set in combinations(range(len(store_rcs)) , M):

    # 해당 집 번호에서 갈 수 있는 치킨 거리 초기화
    distances = 0
    for home_idx in range(len(home_rcs)):
        min_distance = 2*(N-1) # float('inf')

        for store_idx in store_idx_set:
            min_distance = min(min_distance, abs(home_rcs[home_idx][0]-store_rcs[store_idx][0]) + abs(home_rcs[home_idx][1]-store_rcs[store_idx][1]))
        distances += min_distance

    # 해당 조합에 대한 치킨 거리
    # 다른 조합과도 비교해줘야함
    answer = min(answer, distances)

print(answer)


# (조합했다고 치고) BFS