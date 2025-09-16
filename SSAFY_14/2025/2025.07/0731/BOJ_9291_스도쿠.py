 # 백준 9291번. 스도쿠 채점


# 1. 가로세로 확인 후, 3*3 확인

# 테스트 케이스 개수 T
T = int(input())

for tc in range(1, T+1):
    # s = []
    # for r in range(9):
    #     s.append(list(map(int, input().split())))

    # 2차원으로 입력 받기
    s = [list(map(int, input().split())) for _ in range(9)] 

    # 출력 조건 (맞으면 True, 틀리면 False)
    is_correct = True

    # 가로세로 중복 확인
    for r in range(9):
        a = []
        b = []
        for c in range(9):
            a.append(s[r][c])
            b.append(s[c][r])

        # set()으로 중복 없는 것과 길이 비교. 길이 다르면 중복이 있던 것    
        if len(set(a)) != len(a) or len(set(b)) != len(b):
            is_correct = False
            break

    # 3*3 확인
    if is_correct:

        # 3*3을 만드는 것에 어려움을 겪음. for i in range(0,9,3)을 한 번만 시행함(오류원인)
        for i in range(0,9,3):
            for j in range(0,9,3):
                c = []

                for k in range(3):
                    for l in range(3):
                        c.append(s[i+k][j+l])
                if len(set(c)) != len(c):
                    is_correct = False
                    break

            # 해당 조건으로 break를 안해서 for문을 빠져나오지 못한 오류 발생함
            # break를 쓰는 위치, 조건을 잘 생각해야할 듯
            if is_correct == False:
                break
    # 출력        
    if is_correct == False:
        print(f'Case {tc}: INCORRECT')
    else:
        print(f'Case {tc}: CORRECT')

    # 케이스 다음에 공백을 한 번 받아야함. 
    if tc != T:
        input()



###########################################################################
# 2. 가로 -> 세로 -> 3*3 확인

# # 테스트 케이스 개수 T
# T = int(input())

# for tc in range(1, T+1):
#     # s = []
#     # for r in range(9):
#     #     s.append(list(map(int, input().split())))

#     s = [list(map(int, input().split())) for _ in range(9)] 


#     # 가로줄부터 돌면서, 숫자가 중복이 있으면, 종료
#     j = True
#     # 가로 중복
#     for i in s:
#         if len(i) != len(set(i)):
#             j = False
#             break

#     # 세로 중복
#     if j == True:
#         for r in range(9):
#             col = []
#             for c in range(9):
#                 col.append(s[c][r])
#             if len(col) != len(set(col)):
#                 j = False
#                 break

#     # 3*3 중복 확인
#     if j == True:
#         for g in range(0,9,3):
#             for h in range(0,9,3):
#                 c = []
#                 for k in range(3):
#                     for l in range(3):
#                         c.append(s[g+k][h+l])
#                 if len(set(c)) != len(c):
#                     j = False
#                     break
#             if j == False:
#                 break

#     if j == False:
#         print(f'Case {tc}: INCORRECT')
#     else:
#         print(f'Case {tc}: CORRECT')


#     if tc != T:
#         input()


        
            
