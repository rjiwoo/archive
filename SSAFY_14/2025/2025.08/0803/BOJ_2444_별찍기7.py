# 백준) 6단계. 심화 1 - 2444번. 별찍기7
# 한 번 풀은 문제임에도 규칙을 빠르게 못 찾았음.
# 2차원 빈 배열을 만드는 법 슉지 필요
# 출력하기 위해 join()이 바로 기억나지 않았음

# N = int(input())

# mid = (2*N-1)//2
# star = [[' ' for _ in range(2*N-1)] for _ in range(2*N-1)]

# # print(star)

# # 해당 줄만큼 반복문 돌기
# for i in range(2*N-1):

#     # 규칙) *의 시작점이 i-mid. mid를 지나고부터 음수이기 때문에 절대값 계산
#     start = abs(i-mid)
#     end = 2*N-1 - abs(i-mid)

#     for j in range(start, end):
#         star[i][j] ='*'

# # 리스트 구조로 출력되기 때문에 ''로 연결해서 하나의 문자열로 출력
# for row in star:
#     print(''.join(row))

#########################################
# 출력 형식 오류) 별 뒤에 공백이 없어야함.
##########################################

# 바로 출력하는거 생각해보기
N = int(input())

mid = (2*N-1)//2

# 해당 줄만큼 반복문 돌기
for i in range(2*N-1):

    # 앞의 공백이 필요. 시작점 전까지 공백이어야함
    space = abs(i-mid)
    # 별의 개수. 끝 부터 시작점 빼기
    # star = (2*N-1 - abs(i-mid)) - abs(i-mid)
    star = 2*N-1 - 2*space

    # 출력) 공백 + 별
    print(' '*space + '*'*star)

# for i in range(2*N-1):
#     if i <= mid:
#         for j in range(mid - i, mid+i+1):
#             star[i][j]= '*'
#     else:
#         for j in range(i -mid, (2*N-1) - (i-mid)):
#             star[i][j] = '*'

# for row in star:
#     print(''.join(row))

