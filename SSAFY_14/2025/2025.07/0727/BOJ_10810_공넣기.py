# 10810번. 공 넣기

# 바구니 N개, 공 N개, 공을 M번 넣을 것임

# 바구니 N개, 공을 M번 넣을 것
N, M = list(map(int, input().split()))

baskets = [0]*(N+1)

# 공을 M번 넣을 것
for i in range(M):

    # 바구니 시작 번호, 끝 번호, 넣을 공 번호
    N_start, N_end, ball_number = list(map(int, input().split())) 
    for k in range(N_start, N_end+1):
        # if baskets[k] != 0:
        #     baskets[k] = 0
        #     baskets[k] = ball_number
        # else:
        #     baskets[k] = ball_number
        baskets[k] = ball_number
print(*baskets[1:])

