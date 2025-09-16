# swea 2805번 농작물 수확하기

T = int(input())

for tc in range(1, T+1):
    # 농장의 크기 N*N
    N = int(input())
    area = [] # 농장의 가치를 저장할 빈 리스트

    for _ in range(N):
        row = list(map(int, input()))
        area.append(row)

    # 중간 값 mid
    mid = N//2
    result = 0

    
    for i in range(N):
        if i < mid:
            result += sum(area[i][mid-i:mid+i+1])
        elif i==mid:   
            result += sum(area[i][::])
        else: # i>mid
            result += sum(area[i][i-mid:mid-i])

    print(f'#{tc} {result}')