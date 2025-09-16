# SWEA 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

# 각 관리구역을 돌고 다시 사무실로 돌아와
# 사무실에서 출발해서 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때 최소 배터리 사용량

# 1번은 사무실을, 2번부터 N번은 관리구역 번호

# 순열
def perm(count):
    global answer

    # 사무실 번호 빼고 순열을 만들거야.
    if count == len(a):
        # print(picked)
        # 사무실 순서가 결정된 상태
        office_distance = 0
        for i in range(len(picked)-1):
            office_distance += arr[picked[i]][picked[i+1]]
        office_distance += arr[0][picked[0]] + arr[picked[-1]][0]
        
        answer = min(answer, office_distance)
        return
    
    for i in range(len(a)):
        if not visited[i]:
            picked.append(a[i])
            visited[i] = 1
            perm(count + 1)
            visited[i] = 0
            picked.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf')

    # 관리구역 번호
    a = []
    for i in range(1, N):
        a.append(i)
    # 시작과 끝은 무조건 1 (입력 값을 그대로 쓸거라서 0, 0부터 시작임)
    # -> 사무실은 0, 구역은 N-1번까지
    # 그 사이의 구역을 순서를 정해서 돌아야 함.
    # 순서를 정해야 함 -> 순열
    
    
    picked = [] # 순열을 넣어놓을 것 
    visited = [0] * len(a)

    perm(0)

    print(f'#{tc} {answer}')




## 순열

# arr = [1, 2, 3]
# N = 2
# picked = []
# visited = [0] * len(arr)

# perm(0)

# def perm(count):
#     if count == N:
#         return
    
#     for i in range(len(arr)):
#         if not visited:
            
#             picked.append(arr[i])
#             visited[i] = 1
#             perm(count + 1)
#             picked.pop()
#             visited[i] = 0