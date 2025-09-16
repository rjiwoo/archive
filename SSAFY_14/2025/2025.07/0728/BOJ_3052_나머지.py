# 3052번. 나머지

nums =[]
for _ in range(10):
    N = int(input())
    nums.append(N)

results = []
for i in range(len(nums)):
    result = nums[i] % 42
    results.append(result)

# set() 중복을 허용하지 않는 자료형
count = len(set(results))

print(count)