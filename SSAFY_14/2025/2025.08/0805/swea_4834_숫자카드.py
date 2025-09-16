# SWEA 4834번 숫자카드

# T = int(input())    # 테스트 케이스

# for tc in range(1, T+1):

#     N = int(input())    # 카드 장수 N
#     a = input() # 숫자가 여백 없이 주어짐.. 어떻게 리스트로 받지? 까먹음...

#     # int_a = []
#     # for i in a:
#     #     int_a.append(int(i))

#     check = {}
#     for i in a:
#         if i not in check:
#             check[i] = 1
#         else:
#             check[i] += 1
#     print(check)
    
#     many_num = max(check.values())
#     if 

#     # print(many_num)

#     for key, value in check.items():
#         if value == many_num:
#             answer_num = key

#     print(f'#{tc} {answer_num} {many_num}')



T = int(input())    # 테스트 케이스

for tc in range(1, T+1):

    N = int(input())    # 카드 장수 N
    a = list(map(int,input())) 

    count = [0]*11

    for i in a:
        count[i] += 1

    max_count = 0
    max_count_num = 0
    for j in range(len(count)):
        if max_count <= count[j]:
            max_count = count[j]
            max_count_num = j         

    print(f'#{tc} {max_count_num} {max_count}')