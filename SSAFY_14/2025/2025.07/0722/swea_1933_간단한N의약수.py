# swea 1933번 간단한 N의 약수

# 첫번째 풀이
N = int(input())

for i in range(1,N+1):
    if(N % i == 0):
        print(i, end=" ")


# 두 번째 풀이
N = int(input())

n_list = []
for i in range(1,N+1):
    if(N % i == 0):
        n_list.append(i)

print(*n_list)