# SWEA 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 

# 3회차 월말평가 대비

# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

from collections import deque

def bfs(start, goal):
    global answer
    
    visited = [0]*1000001
    q = deque()
    q.append((start,0)) # 시작 숫자와 현재 0번 연산함
    visited[start] = 1 # 시작 숫자는 방문했으니까 겹치면 최소 연산 불가능
    
    while q:
        cur_n, count = q.popleft()

        if cur_n == goal:
            answer = count
            return
        
        cal = [cur_n+1, cur_n-1, cur_n*2, cur_n-10]
        for i in range(4):
            next_n = cal[i]

            if 1 <= next_n <= 1000000 and visited[next_n] == 0:
                visited[next_n] = 1
                q.append((next_n, count+1))


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = 0

    bfs(N, M)

    print(f'#{tc} {answer}')