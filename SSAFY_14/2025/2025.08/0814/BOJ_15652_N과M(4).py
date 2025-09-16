# 백준 15652번 N과M(4)

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

def comb_rep(start):

    if len(pick_nums) == M:
        print(*pick_nums)
        return

    for i in range(start,N+1):
        pick_nums.append(i)
        comb_rep(i)
        pick_nums.pop()


N, M = map(int, input().split())

pick_nums = []
comb_rep(1)
