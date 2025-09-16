# SWEA 1974번 스도쿠 검증

# 가로 9칸, 세로 9칸
# 스도쿠 겹치지 않으면 정답으로 1 출력, 아니면 0 출력

T = int(input())

for tc in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    is_correct = True

    if is_correct == True:
        # 행, 열 중복 확인
        for r in range(9):
            r_list = set()
            c_list = set()
            for c in range(9):
                r_list.add(arr[r][c])
                c_list.add(arr[c][r])
            # 행 중복
            if len(r_list) < 9:
                is_correct = False
                break
            # 열 중복
            if len(c_list) < 9:
                is_correct = False
                break


    if is_correct == True:
        # 3*3 구역 중복 확인
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                
                check = set()
                for k in range(3):
                    for h in range(3):
                        check. add(arr[i+k][j+h])
                if len(check) < 9:
                    is_correct = False
                    break
                
    if is_correct == True:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')