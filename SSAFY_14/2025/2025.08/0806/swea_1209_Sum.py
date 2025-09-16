# SEWA 1209번 Sum

# 테스트케이스 10개 주어짐
# 첫 줄 : 테스트케이스 번호
# 배열의 크기는 100*100
# 다음줄부터 2차원 배열의 각 행 값이 주어짐

# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값

T = 10
for tc in range(1,T+1):
    num = input()
    arr = [list(map(int, input().split())) for _ in range(100)] # 100*100 값 입력 받기

    # print(arr)
    
    # 각 행의 합, 각 열의 합, 각 대각선의 합 모음
    total_sum = [] 

    # 각 행의 합
    for r in range(100):
        r_total = 0
        for c in range(100):
            r_total += arr[r][c]
        total_sum.append(r_total)

    # 각 열의 합
    for r in range(100):
        c_total = 0
        for c in range(100):
            c_total += arr[c][r] 
        total_sum.append(c_total)
            
        
    # 좌 -> 우 대각선
    r_down_sum = 0
    for i in range(100):
        r_down_sum += arr[i][i]
    total_sum.append(r_down_sum)

    # 우 -> 좌 대각선
    l_down_sum = 0
    for i in range(100):
        l_down_sum += arr[i][100-1-i]
    total_sum.append(l_down_sum)


    answer = max(total_sum)
    print(f'#{tc} {answer}')