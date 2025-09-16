# swea 1219번 길찾기

# 강사님 코드 리뷰

def dfs(node):
    global answer

    if node == 99:
        answer = 1
        return 
    
    for next_node in adj_list[node]:
        
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)
        # visited[next_node] = 0  # 방문처리 원복하려면

T = 10

for tc in range(1, T+1):
    _, M = map(int,input().split()) # M = 간선의 수
    info = list(map(int, input().split()))

    # a가 뭐랑 연결되어 있던지 일단 돌아보긴 해야함.
    # 인접리스트가 인접행렬보다 적합함
    adj_list =[[] for _ in range(100)]

    answer = 0
    visited = [0]*100
    # visited = [[0]*M for _ in range(N)]

    for i in range(M):
        # 출발지 a
        a = info[2*i]

        # 도착지 b
        b = info[2*i+1]

        adj_list[a].append(b)
        # adj_list[b].append(a) # 무향 그래프일 때, 이 한 줄 추가
    
    # 0번 노드 방문 처리. 노드 0번에서 시작할거니까
    visited[0] = 1
    dfs(0)
    
    print(f'#{tc} {answer}')

