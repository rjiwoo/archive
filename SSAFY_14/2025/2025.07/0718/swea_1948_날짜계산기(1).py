# swea 1948번. 날짜 계산기

# 첫 번째 풀이
T = int(input())

for tc in range(1, T+1):

    answer = 0
    n = list(map(int, input().split()))
    
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if n[0] == n[2]:
        answer = n[3]- n[1] + 1
    else:
        total_days = 0
        
        # 첫 달 남은 일수
        total_days += month_day[n[0] - 1] - n[1] + 1
        
        # 사이에 있는 달들
        for i in range(n[0], n[2] - 1):
            total_days += month_day[i]
        
        # 마지막 달 날짜
        total_days += n[3]
        
        answer = total_days

    print(f"#{tc} {answer}")
