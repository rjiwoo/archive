# SWEA 1249. [S/W 문제해결 응용] 4일차 - 보급로

# 누적 시간이 가장 작은 경로
# 음수 X -> Dijkstra

# 전형적인 다익스트라 문제
# 그래프 문제와 차이점
# - 이동가능한게 상하좌우 4방향
# - 최단거리를 저장할 리스트를 2차원으로 구성해야한다
# - 기존 : 특정 노드까지 가는 최단거리
# - 문제 : 특정 좌표까지 가는 최단거리
# - heapq에 들어가야 할 데이터 (누적거리, y, x)형태
from heapq import heappop, heappush
def dijkstra():
    dists = [[21e8] * N for _ in range(N)]   # 최단거리를 저장할 2차원 리스트
    dists[0][0] = 0  # 시작점 초기화
    
    pq = [(0,0,0)]   # 누적거리, y, x
    while pq:
        dist, y, x = heappop(pq)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 범위 밖이면 다음 방향 확인
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            # 누적거리 계산
            new_dist = dist + graph[ny][nx]
            # 이미 더 작거나 같은 시간으로 온 적이 있다
            if dists[ny][nx] <= new_dist:
                continue
            
            dists[ny][nx] = new_dist
            heappush(pq, (new_dist,ny,nx))
    return dists[N-1][N-1]
            
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0 , 1, -1]
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    result = dijkstra()
    
    print(f"#{tc} {result}")