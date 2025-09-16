# 10813번. 공 바꾸기

# 바구니 N개, 공 바꿀 횟수 M
N, M = list(map(int, input().split()))

baskets = [0]*(N+1)

for i in range(1, N+1):
    baskets[i] = i

for j in range(M):
    number_1, number_2 = map(int, input().split())
    baskets[number_1], baskets[number_2] = baskets[number_2], baskets[number_1]

print(*baskets[1:])