# swea 20551번 증가하는 사탕 수열

# 각 상자에 들어 있는 사탕의 개수가 순증가하기를 원함
# 모든 상자에 1개 이상의 사탕이 들어 있기를 원함

# 최소 몇 개의 사탕을 먹어야하는지?

T = int(input())

for tc in range(1, T+1): 
   a, b, c = map(int, input().split()) 
   count = 0

   if b >= c:
        count += b - (c - 1)
        b = c - 1
  
   if a >= b:
        count += a - (b - 1)
        a = b - 1

   if a <= 0 or b <= 0 or c <= 0:
        count = -1

   print(f"#{tc} {count}")