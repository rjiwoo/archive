# 문제2) (배점: 35점)

# 양방향을 개통하여 모든 거점을 서로 오갈 수 있도록 연결
# 각 후보 항로 개통에 드는 에너지 비용이 다름
# 비용의 합이 최소가 되도록 항로를 선택하려고 한다.

# 모든 거점을 한 네트워크로 잇는 데 필요한 최소 총 비용을 계산하는 것
# -> MST 로 접근해야할 것 같음
# MST = 최소신장트리 -> heapq 사용하는데... 
# 간선 중에 최소인 것을 뽑아내려고 힙큐를 쓴 건데
# 비용을 리스트로 담고 최소값만 뽑아내서 풀어라?
# 방법은 prim이랑 크루스칼?이 있음


T = int(input())

for tc in range(1, T+1):
    # V는 마지막 정점 번호
    # E는 간선의 개수
    V, E = map(int, input().split()) 

    graph = []

    for _ in range(E):
        #  거점u와 v를 잇는 양방향 개통 비용 w
        u, v, w = map(int, input().split())
        graph.append((u,v,w))
        # graph[u].append((v, w))
        # graph[v].append((u, w))

    # print(graph)
    # 비용을 기준으로 정렬(작은 비용을 가진 간선을 앞으로 이동)
    graph.sort(key=lambda x:x[2])
    # print(graph)

    answer = 0
    connect = []
    # 그냥 간선만큼 다 돌자.
    for i in range(len(graph)):

        # 고른 거점이 V개가 되면 탐색 더 안할거야
        if len(connect) == V:
            break 

        # connect에 이미 고른 거점이 있다면 건너뛰기
        # 이미 비용이 작은 순서대로 정렬해 둔 뒤에 넣었기 때문에 또 나오면 그건 최소비용이 아님
        if (graph[i][0],graph[i][1]) in connect:
            continue

        # connect에 연결할 거점을 넣어
        # 양방향 개통이니까 상관없지 않나
        connect.append((graph[i][0],graph[i][1]))

        # 그리고 비용을 더해
        answer += graph[i][2]

    # print(connect)
    # print(answer)


    print(f'#{tc} {answer}')