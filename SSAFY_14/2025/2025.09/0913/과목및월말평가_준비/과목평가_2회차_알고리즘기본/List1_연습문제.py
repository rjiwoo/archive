# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     max_value = 0
#     min_value = 9999999999
#     for i in arr:
#         if max_value < i:
#             max_value = i
#         if min_value > i:
#             min_value = i 

#     print(f'#{tc} {max_value-min_value}')

# Gravity 문제

N = int(input())

arr = list(map(int, input().split()))

max_value = 0
for i in range(N):
    temp = 0
    for j in range(1,N):
        if arr[i] > arr[j]:
            temp += 1
    if max_value < temp:
        max_value = temp
print(max_value)