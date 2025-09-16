# swea 4835번 구간합

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a_sum = []
    for i in range(N-M+1):
        sum_sum = sum(a[i:i+M])
        a_sum.append(sum_sum)


    max_value = max(a_sum)    
    min_value = min(a_sum)

    result= max_value - min_value

    print(f'#{test_case} {result}')

