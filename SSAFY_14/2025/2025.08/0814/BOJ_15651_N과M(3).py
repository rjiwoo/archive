# 백준 15650번. N과 M(3) 

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

# 중복순열
def comb_rep(start):

    if len(pick_nums) == M:
        print(*pick_nums)
        return

    for i in range(1,N+1):
        pick_nums.append(i)
        comb_rep(i)
        pick_nums.pop()


N, M = map(int, input().split())

pick_nums = []
comb_rep(1)