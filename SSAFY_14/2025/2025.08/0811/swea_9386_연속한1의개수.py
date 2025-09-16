# swea 9386번 연속한 1의 개수 

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    s = []
    temp = 0
    for i in range(N):
        if arr[i] == 1:
            temp += arr[i]
            s.append(temp)
        else: # 0을 만나면
            temp = 0
    answer = max(s)

    print(f'#{tc} {answer}')