# 백준 1244번 스위치 켜고 끄기

# ON == 1, OFF == 0
# 남학생: 받은 수의 배수 모두 스위치 상태 바꾸기
# 여학생: 받은 수가 기준. 기준을 중심으로 좌우가 대칭이면서 가장 많은 스위치 포함하는 구간 모두 변경
#         좌우가 대칭이 아니면 기준만 변경

# 남학생 == 1
# 여학생 == 2

n = int(input()) # 스위치 개수
start = list(map(int, input().split())) # 스위치 상태
student = int(input()) # 학생 수

for _ in range(student):
    gender, num = map(int, input().split())
    
    if gender == 1:
        # # num의 배수를 모두 변경
        # for i in range(num, n + 1, num): # num부터 시작해서 스위치 개수까지, num만큼 증감
        #    start[i -1] = 1 - start[i- 1]

        for i in range(num - 1, n, num):
            start[i] = 1 - start[i]

    else:
        # start[num-1]가 기준으로, 좌우대칭
        # 기준 값은 무조건 변경됨
        start[num-1] = 1 - start[num-1]

        # 좌우 대칭을 확인할 범위 설정
        left = num -1 -1
        right = num-1 +1

        # 범위를 벗어나거나 대칭이 깨지면 조건문 탈출
        while left >= 0 and right < n and start[left] == start[right]:
            start[left] = 1 - start[left]
            start[right] = 1 - start[right]
            left -= 1
            right += 1
            
                    
# 출력 조건) 한 줄에 20개씩 끊어서 출력
for i in range(n):
    # i번째 스위치 상태 출력
    print(start[i], end=" ")
    
    # 20개마다 줄바꿈
    # 단, 마지막 스위치에서는 줄바꿈하지 않음
    if (i + 1) % 20 == 0 and i != n - 1:
        print()
        





# n = int(input()) # 스위치 개수
# start = list(map(int, input().split())) # 스위치 상태
# student = int(input()) # 학생 수

# for _ in range(student):
#     gender, num = map(int, input().split())
    
#     if gender == 1:
#         # num의 배수를 모두 변경
#         for i in range(num, n + 1, num): # num부터 시작해서 스위치 개수까지, num만큼 증감
#             start[i -1] = 1 - start[i- 1]

#     # 아마 조건과 길이를 설정 잘못한듯
#     # 여자일 경우,
#     else:
#         # start[num-1]가 기준으로, 좌우대칭
#         # 기준 값은 무조건 변경됨
#         start[num-1] = 1 - start[num-1]
#         length = min(num-1-0, n-num-1) # 좌우대칭을 비교해볼 수 있는 최대 길이

#         for i in range(1, length+1):
#             # 좌우 스위치가 서로 같으면, 대칭-> 둘 다 상태를 변경
#             if start[num - 1 - i] == start[num - 1 + i]:
#                 start[num - 1 - i] = 1 - start[num - 1 - i]
#                 start[num - 1 + i] = 1 - start[num - 1 + i]
#             # 좌우 스위치가 다르면, 대칭이 깨진 것 -> 반복문 탈출
#             else:
#                 break
                
# # 출력 조건) 한 줄에 20개씩 끊어서 출력
# for i in range(n):
#     # i번째 스위치 상태 출력
#     print(start[i], end=" ")
    
#     # 20개마다 줄바꿈
#     # 단, 마지막 스위치에서는 줄바꿈하지 않음
#     if (i + 1) % 20 == 0 and i != n - 1:
#         print()