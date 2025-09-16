# 1. 다 보자 (완전탐색)
# 2. 앞에서 계산한 것을 재활용(DP)

# 아래의 문제풀이는 DP
# 2. 누적해서 비교

T = int(input())

for tc in range(1, T+1):
    # 이용권 가격들(1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용 계획 (1부터 쓴다)
    days = [0] + list(map(int,input().split()))