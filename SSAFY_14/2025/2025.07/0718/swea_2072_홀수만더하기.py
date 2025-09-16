# swea 2072번 홀수만 더하기

# 첫번째 풀이
# n = int(input())
# for t in range(1, n+1):
#     numbers = list(map(int, input().split()))
#     # numbers = [3, 17, 1, ...]
#     sum = 0
#     for i in numbers:
#         if i % 2 == 1:
#             sum += i
#     print(f"#{t} {sum}")    


# 두번째 풀이
T = int(input())

for tc in range(1, T+1):
    answer = 0 # 케이스마다  answer 값 초기화해서 구해야하기 때문에. 
    numbers = list(map(int, input().split()))
    
    # range() 쓰는 이유 : 몇 번째 도는건지 알기 위해서
    for number in numbers:
        if number % 2 == 1:
            answer += number
    print(f"#{tc} {answer}")