# 25304
# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치

X = int(input())
n = int(input())

total = 0
for i in range(n):
    a, b = map(int, input().split())
    total += a*b

if X == total:
    print('Yes')
else:
    print('No')