# 1546번. 평균

# 시험 본 과목의 개수 N
N = int(input())

scores = list(map(int, input().split()))
M = max(scores)

for i in range(len(scores)):
    scores[i] = scores[i]/M*100

print(sum(scores)/len(scores))


# 1546번. 평균

# 시험 본 과목의 개수 N
N = int(input())

scores = list(map(int, input().split()))
M = max(scores)

for i in range(N):
    scores[i] = scores[i]/M*100

print(sum(scores)/N)