# 인접리스트로 풀 것. 이유는?

# SWEA 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
# dfs

def dfs(node):
    # 사람 v와 연결된 모든 사람들을 방문 처리 (같은 그룹)
    for next in adj_list[node]:
        if visited[next]:
            continue
        visited[next] = 1
        dfs(next)
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    connections = list(map(int, input().split()))
    adj_list = [[] for _ in range(N + 1)]  # 인접 리스트 초기화
    visited = [False] * (N + 1)
    answer = 0
     
    # 인접 리스트 
    for i in range(M):
        idx1 = i*2
        idx2 = idx1 + 1

        # adj_list[connections[idx1]].append(connections[idx2])
        # adj_list[connections[idx2]].append(connections[idx1])

        # 내가 연결하고 싶은 친구는 a와 b
        a = connections[idx1]
        b = connections[idx2]

        adj_list[a].append(b)
        adj_list[b].append(a)  # 무방향 그래프
 
    for node in range(1, N + 1):
        if visited[node]:
            continue

        answer += 1   # 새로운 그룹 발견
        visited[node] = 1
        dfs(node)
 
    print(f"#{tc} {answer}")