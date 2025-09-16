# 백준 2798번 블랙잭

# N장
# M과 제일 가까운 카드 3장의 합
N, M = map(int, input().split())
arr = list(map(int, input().split()))

value = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            n3 = arr[i]+arr[j]+arr[k]

            # M보다 큰 건 저장 안 함
            if n3 <= M:
                value.append(n3)

# value.sort()
# # print(value)

# print(value[-1])

# 저장한 것 중 가장 큰 값
print(max(value))