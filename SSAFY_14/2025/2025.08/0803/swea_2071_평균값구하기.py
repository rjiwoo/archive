# 2071. 평균값 구하기

# 내장함수 사용
# T = int(input())

# for tc in range(1,T+1):
#     scores = list(map(int, input().split()))
#     answer = round(sum(scores)/len(scores), 1) # 첫째자리에서 반올림
                
#     print(f'#{tc} {answer}')


# sum, len 내장함수 사용X
T = int(input())

for tc in range(1,T+1):
    scores = list(map(int, input().split()))

    scores_sum = 0
    count = 0
    for i in scores:
        scores_sum += i
        count += 1
    answer = round(scores_sum / count)
                
    print(f'#{tc} {answer}')