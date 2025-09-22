# BOJ 2606번 바이러스

# 웜 바이러스
# 네트워크 상에서 연결되어 있으면 감염됨

# 인접리스트로 연결되어 있는 것을 체크하고 시작하는 것

def bfs(start_node):




N = int(input())    # 컴퓨터의 수
computer_pair = int(input())    # 컴퓨터가 연결된 쌍의 수

connect = [[] for _ in range(N+1)]  # 인접리스트(컴퓨터가 연결된 것을 표시하는)

for _ in range(computer_pair):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

# print(connect)

bfs(1)
