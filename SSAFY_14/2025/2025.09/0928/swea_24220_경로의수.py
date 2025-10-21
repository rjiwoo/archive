# SWEA 24220. 경로의 수

# 3회차 월말 대비

T = int(input())
N, E = map(int, input().split())
arr = list(map(int, input().split()))
S, G = map(int, input().split())

# 인접리스트
adj_list = [[] for _ in range(N+1)]
# print(adj_list)

for i in range(0, len(arr), 2):
    a = arr[i]
    b = arr[i+1]
    adj_list[a].append(b)

print(adj_list)