# 백준) 6단계. 심화 1 - 3003번. 킹, 퀸, 룩, 비숍, 나이트, 폰
# 체스 총 16개 : 킹 1, 퀸 1, 룩 2, 비숍 2, 나이트 2, 폰 8

# 첫째줄 흰색 킹, 퀸, 룩, 비횹, 나이트, 폰의 개수 주어짐. 0 <= X <= 10

origin = [1, 1, 2, 2 ,2 ,8] # 필요한 개수
n = list(map(int, input().split())) # 찾은 개수 받기
answer = [] # 결과

for i in range(len(n)):
    if origin[i] == n[i]:
        answer.append(0)
    else:
        answer.append(origin[i]-n[i])

print(*answer)