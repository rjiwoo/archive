# swea 2063번 중간값 찾기

N = int(input())
score = list(map(int, input().split()))
score.sort()
mid = N // 2
print(score[mid])