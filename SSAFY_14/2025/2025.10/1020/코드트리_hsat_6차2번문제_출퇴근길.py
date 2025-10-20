# 코드트리 hsat 6차 2번 문제 - 출퇴근길

# 도로의 연결 모양, 일방통행 여부 등으로 출퇴근길 모두 방문 가능한 동네 한정
# 출퇴근길은 단방향 그래프로 나타낼 수 있음
# 각 동네를 1~n까지 번호로 매겨진 n개의 정점
# m개의 일반통행의 도로를 단방향 간선

# 집 = S, 회사 = T

# S에서 T로 가는 출근길 경로와 T에서 S로 가는 퇴근길 경로에 모두 포함될 수 있는 정점의 개수를 세라. 

# n, m이 공백으로 구분되어 주어짐
# m개의 줄에 x -> y 가 공백으로 주어짐
# 마지막 줄에 S, T 

# 풀이 생각
# S에서 T로 갈 수 있는 경로 찾기
# T에서 S로 갈 수 있는 경로 찾기
# 교집합

# 다른 코드와 GPT의 도움을 받아서 코드를 수정했는데, 
# 왜 역그래프를 이용해서 확인해야하는지 이해가 가지 않음 ..

from collections import deque

# 경로 찾기
def find_nodes(start, graph, n, stop_node):
    visited = [False]*(n+1)
    q = deque()
    q.append(start)
    visited[start] = True

    node = set()
    node.add(start)
    
    while q:
        now = q.popleft()

        if now == stop_node:
            continue

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                node.add(i)
    return node 

# 경로 입력 받기 : 인접리스트
n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
adj_list_rev = [[] for _ in range(n + 1)] # 역방향 그래프 추가

for _ in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list_rev[y].append(x) # 역방향 간선 추가

S, T = map(int, input().split())

# 1. 출근길(S -> T) 경로에 포함될 수 있는 정점 찾기
#    - 조건 1: S에서 해당 정점으로 갈 수 있어야 함 (S -> V)
#    - 조건 2: 해당 정점에서 T로 갈 수 있어야 함 (V -> T)

# 조건 1 만족하는 집합 (S에서 출발)
from_S = find_nodes(S, adj_list, n, T)
# 조건 2 만족하는 집합 (역방향 그래프에서 T에서 출발)
to_T = find_nodes(T, adj_list_rev, n, -1)

# 두 조건을 모두 만족하는 출근길 정점 집합
going = from_S & to_T


# 2. 퇴근길(T -> S) 경로에 포함될 수 있는 정점 찾기
#    - 조건 3: T에서 해당 정점으로 갈 수 있어야 함 (T -> V)
#    - 조건 4: 해당 정점에서 S로 갈 수 있어야 함 (V -> S)

# 조건 3 만족하는 집합 (T에서 출발)
from_T = find_nodes(T, adj_list, n, S)
# 조건 4 만족하는 집합 (역방향 그래프에서 S에서 출발)
to_S = find_nodes(S, adj_list_rev, n, -1)

# 두 조건을 모두 만족하는 퇴근길 정점 집합
coming = from_T & to_S


# 3. 출퇴근길 모두에 포함되는 정점의 교집합 찾기
answer = going & coming

# 문제 조건에 따라 S, T는 제외
answer -= {S, T}

print(len(answer))