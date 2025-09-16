# SWEA 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합


# 1부터 12까지의 숫자를 원소로 가진 집합 A
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력
# 해당하는 부분집합이 없는 경우 0을 출력

# 부분집합 뽑는 함수
def solve(count, idx):
    global answer 

    # N개를 뽑았을 때, 합이 K이면 answer 추가
    if count == N:
        if sum(picked) == K:
            answer += 1

    # 부분집합 - 뽑았던거 중복되면 안됨
    for i in range(idx, len(A)):
        picked.append(A[i])
        solve(count + 1, i + 1)
        picked.pop()
    

T = int(input())

for tc in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())
    answer = 0
    
    picked = []
    solve(0,0)

    print(f'#{tc} {answer}')