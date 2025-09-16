# swea 5644번 무선충전

# 가로, 세로 크기는 10
# 사용자는 총 2명
# 사용자A는 지도의 (1, 1) 지점에서, 사용자B는 지도의 (10, 10) 지점에서 출발

# 테스트 케이스의 첫 번째 줄에는 총 이동 시간(M), BC의 개수(A)가 주어진다.
# 2개의 줄에는 각각 사용자 A와 B의 이동 정보가 주어진다.
# 한 사용자의 이동 정보는 M개의 숫자로 구성되며, 각각의 숫자는 다음과 같이 매초마다 이동 방향을 의미

from pprint import pprint
# 움직이지 않음, 상, 우, 하, 좌
dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]


T = int(input())

for tc in range(1, T+1):

    graph = [[[] for _ in range(10)] for _ in range(10)] # 가로세로10 (시작점은 1,1 이라는데 0,0이라고 생각하기)

    M, A = map(int, input().split()) # 이동시간 M, BC의 개수 A
    info_a = list(map(int, input().split()))
    info_b = list(map(int, input().split()))

    # 첫 시작점
    a = [0,0]
    b = [9,9]

    info_ap = [] # 충전소 위치(r,c), 충전범위, 성능
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        info_ap.append((y - 1, x - 1, c, p))
    
    pprint(info_ap)


    # 충전소 위치에서 해당하는 충전범위만큼의 위치에 성능의 값을 써 놓기
    # 충전 범위 표시
    for idx, (r, c, coverage, power) in enumerate(info_ap, 1):  # BC 번호 1부터 시작
        for i in range(10):
            for j in range(10):
                if abs(r - i) + abs(c - j) <= coverage:
                    graph[i][j].append((idx, power))

    pprint(graph)

    # 만약 충전범위가 겹친다면 append로 추가해서 a가 이동할 때 해당 좌표에 값이 2개면 그 해당 부분에 b가 없으면 큰 값을 충전하고, 있으면 서로 겹치지 않게



    print(f'# {tc} ')