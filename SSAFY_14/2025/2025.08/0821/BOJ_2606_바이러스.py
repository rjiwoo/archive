# 백준 2606번 바이러스

# bfs 구현
# visited 생성
# 큐 생성
# 시작점 인큐
# 인큐 표시

# 반복
# 디큐
# 방문해서 할일
# 방문정점에서 인접하고 미방문이면
#     인큐
#     인큐 표시



# BFS를 사용하여 바이러스 전파 과정 진행
def bfs(start_node):
    visited = [False] *(N+1) # 방문 기록 남길 리스트

    # 큐에 시작 컴퓨터(1번)를 넣습니다.
    q = [start_node]
    # 시작 컴퓨터를 방문(감염) 처리
    visited[start_node] = True
    
    count = 0
    
    while q:
        # 큐에서 컴퓨터를 하나 꺼내기
        node = q.pop(0)
        
        for neighbor in connect[node]:
            # 연결된 컴퓨터가 아직 감염되지 않았다면
            if not visited[neighbor]:
                # 큐에 추가하고 감염 처리
                q.append(neighbor)
                visited[neighbor] = True
                # 감염된 컴퓨터 수를 1 증가
                count += 1
                
    return count



N = int(input()) # 컴퓨터 수
M = int(input()) # 연결되어 있는 컴퓨터 쌍의 수 (=간선의 개수?)

computer = [0]*(N+1)
# 컴퓨터가 서로 연결되어 있는 것 표시 = 인접리스트
# 컴퓨터의 번호와 인덱스 번호를 맞추기 위해서 N+1
connect = [[] for _ in range(N+1)]

# 연결되어 있는 것 표시
for _ in range(M):
    a, b = map(int,input().split())
    connect[a].append(b) # 컴퓨터 a번은 b와 연결됨
    connect[b].append(a) # 무방향 그래프

result = bfs(1)
print(result)