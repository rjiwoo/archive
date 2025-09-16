# 10811번 바구니 뒤집기

# 바구니 N개, 역순으로 바꿀 횟수 M번
N, M = map(int,input().split())

# 바구니 만들기
baskets = list(range(0,N+1))

for _ in range(M):
    i, j = map(int,input().split())
    baskets[i:j+1] = baskets[i:j+1][::-1] # 숫자 뒤집기 [::-1] 기억하기

print(*baskets[1:])