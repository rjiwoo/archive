# swea 2058번 자릿수 더하기

# 첫번째 풀이
n = int(input())
sum = n//1000 + n//100%10 + n//10%10 + n%10
print(sum)


########################################################
# 두번째 풀이

# map함수로 튜플을 만들고, 그걸 배열에 넣어서 더해
answer = sum(list(map(int, input()))) 
print(answer)