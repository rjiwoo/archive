# swea 5656번 [모의SW역량테스트] 벽돌 깨기 

# 구슬을 쏘아 벽돌을 깨뜨리는 게임
# 구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 W*H 배열로 주어짐
# 0은 빈 공간을 의미

# 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.

# 벽돌은 숫자 1 ~ 9 로 표현되며,
# 구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거됨

# N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다.
# N, W, H, 그리고 벽돌들의 정보가 주어질 때,
# ▶ 남은 벽돌의 개수를 구하라!

# 벽돌 선정은 맨 위에 있는 벽돌을 다 시도해보는 것
# BFS

def shoot(count, remain_blocks, graph):
    


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]

    # print(graph)
    
    min_blocks = 1e9  # 최소 벽돌 수
    # 벽돌 개수
    blocks = 0

    # 벽돌 개수 세기
    for r in range(H):
        for c in range(W):
            if graph[r][c]:
                blocks = 0

    # 벽돌 깨기
    # 슈팅한 횟수, 남은 벽돌 수, 원본
    shoot(0, blocks, graph)


    print(f'#{tc} {answer}')