# SWEA 11092번 최대 최소의 간격

T = int(input())    # 테스트 케이스 수

for tc in range(1, T+1):
    N = int(input())    # 양수의 개수 N
    a = list(map(int, input().split())) # N개의 양수

    # 제일 큰 값 초기화
    max_num = 0
    min_num = 11

    for i in range(N):

        # 큰 수가 여러 개이면 마지막 나오는 위치
        if max_num <= a[i]:
            max_num = a[i]
            max_num_index = i+1

        # 작은 수가 여러 개이면 가장 처음 나온 위치    
        if min_num > a[i]:
            min_num = a[i]
            min_num_index = i+1

    # 두 값의 차이 절대값
    answer = abs(max_num_index-min_num_index)

    print(f'#{tc} {answer}')