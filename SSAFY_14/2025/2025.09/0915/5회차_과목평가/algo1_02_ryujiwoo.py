# 문제1 : 단순증가패턴( 배점: 40점)

# 단순증가패턴 : 패턴 내 숫자들이 감소나 정체 없이 꾸준히 증가하는 패턴
# `단순증가패턴`을 가지는 윈도우는 몇 개인지 출력

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    # window = N//M
    arr = list(map(int, input().split()))
    answer = 0

    # 받은 배열을 길이 M으로 나눠서
    # 그 나눈 길이만큼을 확인하면서 정체 없이 증가하는지 확인해. 
    # 맞으면 answer += 1

    picked = []

    # 받은 배열을 길이 M으로 나눠서 저장
    for i in range(N//M):
        picked.append(arr[0:M])
        # print(picked)

        for _ in range(M):
            arr.pop(0)
        # print(arr)
    
    # N이 M의 배수가 아닌 경우 마지막 윈도우에 넣기
    if arr:
        a = len(arr)
        picked.append(arr[:])
        for _ in range(a):
            arr.pop()

    # print(picked)
    # print(arr)

    # print(len(picked))

    # 윈도우마다 돌면서 증가하는지 윈도우 내 숫자들이 꾸준히 증가하는 패턴인지 확인
    # 단순증가패턴을 가지는 윈도우가 있으면 answer += 1
    for i in range(len(picked)):
        temp = 0
        count = 0
        for j in range(len(picked[i])-1):
            if count == len(picked[i])-1:
                break

            if picked[i][j] < picked[i][j+1]:
                # print(picked[i][j], picked[i][j+1])
                count += 1
                temp += 1
                # print(f'count{count}')

        if temp == len(picked[i])-1:
            answer += 1

    print(f'#{tc} {answer}')






    