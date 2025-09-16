# 10807번. 개수 세기

N = int(input())
line = list(map(int, input().split()))
find = int(input())

# line에서 find가 몇 번 있는지 카운트
print(line.count(find))

