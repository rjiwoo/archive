# swea 1215번 회문1

T = 10

for tc in range(1, T+1):
    n = int(input())     # 길이

    # 8*8 입력 받기
    arr = [list(input()) for _ in range(8)]

    count = 0
    # 가로 행 먼저
    for r in range(8):
        for c in range(8-n+1):

            r_temp = arr[r][c:c+n]

            if r_temp == r_temp[::-1]:
                count += 1


    # 세로 행
    for r in range(8):
        for c in range(8-n+1):

            s = []
            for k in range(n):
                    s.append(arr[c+k][r])
            if s == s[::-1]:
                count += 1
            

    print(f'#{tc} {count}')


