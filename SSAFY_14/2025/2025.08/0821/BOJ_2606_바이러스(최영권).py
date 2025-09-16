computers = int(input()) # 컴퓨터 수
pair = int(input()) # 연결되어 있는 컴퓨터 쌍의 수(=간선의 개수)
lst = [] # 감염된 컴퓨터 저장 -> 길이 확인하여 정답 도출 예정 -1(시작점)

# 인접리스트 (연결되어 있는 거 표시용)
graph = [[] for _ in range(computers+1)]

# 방문 표시용
visited = [False] * (computers+1)

# 바이러스 전파 과정
def virus(a, grid, visited): # 시작점 a, grid == graph,  방문표시

    # 시작점 감염 처리
    if visited[a] == False:
        visited[a] = True

    global lst
    lst.append(a) # 감염된 컴퓨터 추가
    
    # 인접리스트 돌면서 
    for i in range(len(grid[a])):
        if not visited[grid[a][i]]:
            virus(grid[a][i], grid, visited)


for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
virus(1, graph, visited)
print(len(lst), lst)