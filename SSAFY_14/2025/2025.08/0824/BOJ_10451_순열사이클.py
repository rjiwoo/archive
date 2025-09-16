#백준 10451번 순열 사이클 (다시풀기)

from collections import deque

T = int(input())

for _ in range(T):
    N = int(input()) # N개의 정수

    graph = [0] + list(map(int, input().split()))
    
    # 방문 여부를 기록
    visited = [False] * (N + 1)
    
    cycle_count = 0

    # 1부터 N까지 모든 노드를 확인
    for i in range(1, N + 1):
        # 만약 아직 방문하지 않은 노드라면, 새로운 사이클의 시작점
        if not visited[i]:
            cycle_count += 1 # 새로운 사이클을 발견했으므로 카운트 증가
            j = i 
            
            # 이 사이클에 연결된 모든 노드를 방문 처리
            while not visited[j]:
                visited[j] = True
                j = graph[j] # 다음 노드로 이동
                
    print(cycle_count)
