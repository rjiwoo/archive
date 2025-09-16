# 2562번. 최댓값

nums = []
for i in range(9):
    N = int(input())
    nums.append(N)

max_value = max(nums)
print(max_value)

for j in range(len(nums)):
    if nums[j] == max_value:
        print(j+1)