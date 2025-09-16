# swea 1948번. 날짜 계산기

# 두 번째 풀이

# 테스트 케이스
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_sum =[0]*13

# month번째 월의 누적합은?
for month in range(1, 13):
#   days_sum.append()[month] # append()로 뒤에다가 추가하는 것 (이유: days_sum 길이가 [0]으로 하나일 때)
    days_sum[month] = days_sum[month-1] + days[month]

    
# 테스트 케이스 수만큼 반복
T = int(input())
for tc in range(1, T+1):
    answer = 0
    m1, d1, m2, d2 = map(int, input().split())

    # 사이에 있는 달을 더하기 :days_sum[m2-1] - days_sum[m1]
    # 앞에 달 남은 일수 더하기 : (days[m1] - d1 + 1)
    answer = days_sum[m2-1] - days_sum[m1] + (days[m1] - d1 + 1) + d2  

    print(f'#{tc} {answer}')