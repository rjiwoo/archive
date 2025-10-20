# 프로그래머스 [PCCP 기출문제] 2번 / 석유 시추

# 세로길이가 n 가로길이가 m인 격자 모양
# 시추관을 수직으로 단 하나만 뚫을 수 있을 때, 
# 가장 많은 석유를 뽑을 수 있는 시추관의 위치 찾기

# 시추관은 열 하나를 관통하는 형태
# 시추관이 석유 덩어리 일부를 지나면 해당 덩어리에 속한 모든 석유 추출 가능

# 석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열 land가 매개변수로 주어짐


# 풀이 생각
# BFS를 사용하면 되지 않을까?
# BFS 어떻게 사용하더라... deque ....?

from collections import deque

# 상,하,좌,우
dr = [-1, 1, 0, 0] 
dc = [0, 0, -1, 1]

    
def solution(land):
    answer = 0
    
    # land의 크기 구하기
    N = len(land)    # 행
    M = len(land[0]) # 열
    
    # BFS는 visited 사용하니까
    # visited는 land의 크기만큼
    visited = [[0]*M for _ in range(N)]
    oil = [0]*M # 각 열에서 추출할 수 있는 오일의 양
    
    # 오일이 어떻게 어디에 있는지 확인하기 위해서 BFS 사용
    def bfs(r,c):
        q = deque()
        q.append((r,c))
        visited[r][c] = 1
        count = 1   # 현재 석유 크기

        # 시추관이 석유 덩어리 일부를 지나면 해당 덩어리에 속한 모든 석유 추출 가능하니까
        # 지금 찾는 석유 덩어리가 어느 열에 걸쳐있는지 파악해야함
        columns = set() # 중복 제거를 위해서 set()
        columns.add(c)  # c열 지나감
        
        while q:
            cur_r, cur_c = q.popleft()

            # 석유 있는지 4방향 탐색
            for i in range(4):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]

                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] != 1 and land[nr][nc] == 1:
                    visited[nr][nc] = 1
                    q.append((nr,nc)) 
                    count += 1
                    columns.add(nc)

        return count,columns
        

    for r in range(N):
        for c in range(M):
            if land[r][c] == 1 and visited[r][c] == 0:
                oil_count, coulmns = bfs(r,c)
                # print(oil_count, coulmns)

                for j in coulmns:
                    oil[j] += oil_count

                # print(oil)

    answer = max(oil)
    
    return answer
