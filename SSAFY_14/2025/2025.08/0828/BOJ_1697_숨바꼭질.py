# 백준 1697 숨바꼭질

# 수빈이의 위치는 N
# 동생의 위치는 K

# 수빈이는 걷거나 순간이동 가능. 
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
#                     순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후?
# 가장 빠른 시간 = 최단 시간 = BFS

from collections import deque

N, K = map(int,input().split())

ans = 0
maxnum = 100001
visited = [-1] * maxnum

def bfs(N, K):
    q = deque()
    
    visited[N] = 0
    q.append(N)

    if N == K:
        return 0

    while q:
        x = q.popleft()
        
        for next_x in [x+1, x-1, x*2]:
            if 0<=next_x<maxnum and visited[next_x] == -1:
                visited[next_x] = visited[x] + 1
                q.append(next_x)
    return visited[K]

ans = bfs(N, K)
print(ans)
