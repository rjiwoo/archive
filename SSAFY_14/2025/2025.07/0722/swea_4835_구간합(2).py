T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    # for i in range(N): # 쓸데없는 for문 왜 쓴거임? 멍청했다... 무지성 for문...
    max_sum = -9999999
    min_sum = 9999999
    for i in range(N-M+1):
        # num_sum = nums[i: i+M]
        num_sum = 0
        for j in range(i, i+M):
            num_sum += a[j]
        if max_sum < num_sum:
            max_sum = num_sum
        if min_sum > num_sum:
            min_sum = num_sum
        answer = max_sum - min_sum
    print(f'#{tc} {answer}') 