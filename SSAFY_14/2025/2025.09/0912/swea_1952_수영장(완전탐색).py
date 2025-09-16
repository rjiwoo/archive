# 1952. [모의 SW 역량테스트] 수영장

# 1. 다 보자 (완전탐색)
# 2. 앞에서 계산한 것을 재활용(DP)

# 아래의 문제풀이는 완전탐색
# 1. 4가지 경우를 모두 확인

# 종료조건: 12월을 모두 고려한 경우
# 가지의 수: 4개(1일, 1달, 3달, 1년) 
def recur(month, total_cost):
    global min_cost

    if month > 12:
        # 최소값 갱신
        min_cost = min(min_cost, total_cost)
        return
    
    # 1일권으로 다 사는 경우
    recur(month + 1, total_cost + (days[month] * cost_day))
    # 1달권으로 다 사는 경우
    recur(month + 1, total_cost + cost_month)
    # 3달권으로 다 사는 경우
    recur(month + 3, total_cost + cost_month3)
    # 1년 이용권으로 사는 경우
    recur(month + 12, total_cost + cost_year)


T = int(input())

for tc in range(1, T+1):
    # 이용권 가격들(1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용 계획 (1부터 쓴다)
    days = [0] + list(map(int,input().split()))
    min_cost = 31 * 12 * 3000 # 최대 금액 (다 1일권 사용) 
    recur(1, 0) # 1월부터 시작

    print(f'#{tc} {min_cost}')