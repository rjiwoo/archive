# swea 1952번 수영장 (필수제출)

# 가장 적은 비용으로 수영장을 이용할 수 있는 방법

# 입력) 각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어짐
# 1일, 1달, 3달, 1년 이용권


# 3달 이용권을 구매할지 말지 선택?
def solve(month,cost):
    global min_cost
    # 12월보다 커지면 종료. 12월에 3개월 구매할 필요없음. 아마도..?
    # 11월에는 구매해도 괜찮은건가. 모르겠음...
    if month > 12:
        if min_cost> cost:
            min_cost = cost
            return
    else:    
        solve(month+1, cost+plan[month]) # 1달권 구매 (일일권일수도 있음)
        solve(month+3, cost+month_3) # 3달권 구매

T = int(input())

for tc in range(1, T+1):

    day, month, month_3, year = map(int, input().split())
    plan = list(map(int,input().split()))
    plan.insert(0,0)
    ans = 0
    # print(plan)

    # 1. 1일권 다 구매
    for i in range(1, 13):
        plan[i] = plan[i] * day # 해당 달에 이용한 날의 일일권 가격

    # 2. 1달 이용권 구매
    for i in range(1, 13):
        if month < plan[i]: # 1달 이용권이 1일권보다 저렴하면 변경
            plan[i] = month 

    # plan은 각 달의 최소비용으로 이미 다 값이 들어가 있음
    # 3달 이용권을 구매하려면 그것보다 저렴한지를 확인해야함
    # 3달을 선택하는 방법이 여러가지임. 모든 경우 중 가장 저렴한거 
    # 3. 3달 이용권 구매(10월까지만 구매할 수 있음? 11월,12월에 구매하면 12월까지만 사용할 수 있음) 
    
    # 함수에서 plan[month]를 쓰려고 하니까 인덱스 범위를 벗어나는 오류 발생
    # plan[13]이상도 확인하게 됨. 그런데 자료가 없으니까. 전역 변수 min_cost 사용하기
    # min_cost = 전체 12개월 중 모든 조합 중 최소 총 비용
    min_cost = float('inf') # 가장 큰 수
    solve(1,0)
    
    # print(min_cost)

    # 4. 1년 이용권 구매
    ans = min(min_cost,year)

    print(f'#{tc} {ans}')