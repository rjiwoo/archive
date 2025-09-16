# 11720번 숫자의 합

# 숫자의 개수 N
N = int(input())
nums = input()

result = 0
for i in range(N):
    result += int(nums[i])
print(result)