# SWEA 2817. 부분 수열의 합

# A1, A2, ... , AN의 N개의 자연수가 주어졌을 때, 
# 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램

# def solve(count, idx):
#     global answer

#     if sum(picked) > K:
#         return

#     if sum(picked) == K:
#         answer += 1

#     if count == N: 
#         return

#     for i in range(idx, N):
#         picked.append(A[i])
#         solve(count + 1, i + 1)
#         picked.pop() 

# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
#     answer = 0
#     picked = []

#     solve(0,0)

#     print(f'#{tc} {answer}')


def solve(idx, total):
    global answer
    if total > K:
        return

    if idx == N:
        if total == K:
            # 조건 만족 시 처리
            answer += 1
        return

    # 현재 원소 선택
    solve(idx + 1, total + A[idx])

    # 현재 원소 선택 안 함
    solve(idx + 1, total)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    answer = 0

    solve(0,0)

    print(f'#{tc} {answer}')