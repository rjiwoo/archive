# SWEA 2105. [모의 SW 역량테스트] 디저트 카페

# 대각선으로 움직임
# 사각형 모양을 그리며 출발한 카페로 돌아와야함
# -> 꼭지점에서는 출발을 못해

# 해당 지역을 벗어나면 안됨
# 같은 디저트를 팔고 있는 카페를 가면 안됨 (같은 숫자면 같은 디저트)
# 한 곳만 가도 안돼
# 왔던 길을 다시 가도 안돼
# 최대한 많은 디저트 먹어야해
# 디저트 못먹으면 -1

# 우하향, 좌하향, 좌상향, 우상향 
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

# 현재 위치, 첫시작점, 현재 이동 방향, 방향 바꾼 횟수, 디저트 가게 방문 횟수 
def dfs(r, c, start_r, start_c, dir, dir_count, dessert_count ):
    # 다음 디저트 가게로 갈 수 있는지 확인하
    # 1. 방문한 디저트 종류를 팔고 있으면 안되고
    # 2. 다시 돌아왔을 때 사각형 모양으로 돌아올 수 있는지
    #    -> 방향을 3번 바꿨을 때, 원 위치로 돌아올 수 있는지?

    if dir_count 


    pass


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 디저트 못먹으면 -1
    max_dessert = -1

    # 디저트 종류는 1~100까지
    # 먹었던 디저트는 다시 먹으면 안됨
    visited = [0] * 101

    # 꼭지점 제외하고 돌자...어차피 꼭지점에서는 시작이 안됨
    for r in range(N-2):
        for c in range(1, N-1):
            start_r, start_c = r, c

            # 시작점 디저트 종류는 방문 처리
            visited[arr[start_r][start_c]] = 1

            dfs()



