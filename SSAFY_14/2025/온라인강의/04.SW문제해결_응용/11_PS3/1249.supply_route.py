import sys
sys.stdin = open("input.txt")

# 전형적인 다익스트라 문제
# 그래프 문제와 차이점
#  - 이동 가능한 게 상하좌우 4개 방향
#  - 최단 거리를 저장할 리스트를 2차원으로 구성해야한다
#    - [기존] 특정 노드까지 가는 최단거리
#    - [문제] 특정 좌표까지 가는 최단거리
#  - heapq에 들어가야 할 데이터 (누적거리, y, x)형태

from heapq import heappop, heappush


def dijkstra():
    dists = [[21e8] * N for _ in range(N)]  # 최단거리를 저장할 2차원 리스트
    dists[0][0] = 0  # 시작점 초기화

    pq = [(0, 0, 0)]  # (누적거리, y, x)

    while pq:
        dist, y, x = heappop(pq)

        for i in range(4):  # 상하좌우 확인
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위 밖이면 다음 방향 확인
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            # 누적거리 계산 = 현재까지의 거리 + 다음 거리
            new_dist = dist + graph[ny][nx]

            # 이미 더 작거나 같은 시간으로 온 적이 있다
            if dists[ny][nx] <= new_dist:
                continue

            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, ny, nx))

    return dists[N-1][N-1]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print(f'#{tc} {result}')
