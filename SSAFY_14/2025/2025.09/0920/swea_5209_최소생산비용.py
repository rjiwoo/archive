# SWEA 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용


# N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 함
# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산

# 각 제품을 번호라고 생각하고 접근하면
# 공장의 순서가 제품을 생산하는 것
# 공장의 순서를 순열로 결정하고, 그 순서에 맞는 제품을 생산하면 되니까
# 해당 순열에 해당 제품의 생산 비용을 더해서 최소를 하면 됨

def perm(count, total):
    global answer

    if total >= answer:
        return

    if count == N:
        answer = min(answer, total) 
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            perm(count + 1, total + graph[count][i])
            visited[i] = 0
            

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 제품의 개수이자, 공장의 개수임
    graph = [list(map(int, input().split())) for _ in range(N)] # 제품별 공장의 생산 비용
    answer = float('inf')

    picked = []
    visited = [0] * N
    perm(0, 0)
    
    print(f'#{tc} {answer}')



### 제한시간 초과코드 ###
# def perm(count):
#     global answer

#     if count == N:
#         # 순서가 만들어지면, 그 상태로 생산비용 가져오기
#         # 지금 이거의 순서는 0번이 0번 공장, 1번이 1번 공장 이런 느낌임
#         total = 0
#         for i in range(N):
#             total += graph[i][picked[i]]

#         answer = min(answer, total) 
#         return

#     for i in range(N):
#         if not visited[i]:
#             visited[i] = 1
#             picked.append(i)
#             perm(count + 1)
#             picked.pop()
#             visited[i] = 0
            

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input()) # 제품의 개수이자, 공장의 개수임
#     graph = [list(map(int, input().split())) for _ in range(N)] # 제품별 공장의 생산 비용
#     answer = float('inf')

#     picked = []
#     visited = [0] * N
#     perm(0)
    
#     print(f'#{tc} {answer}')
