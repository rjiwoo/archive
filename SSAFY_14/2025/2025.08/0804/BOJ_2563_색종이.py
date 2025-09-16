# 백준) 7단계. 2차원 배열 - 2563번 색종이

# 100*100의 색종이 위에 10*10 색종이를 여러개 붙임
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램

# 100*100 크기의 색종이 영역에 0으로 채우기
ground = [[0]*100 for _ in range(100)]


n = int(input()) # 색종이 개수 

for i in range(n):
    a, b = map(int, input().split()) # 색종이가 붙을 시작점의 위치(왼쪽 아래 꼭짓점)

    for x in range(a, a+10):
        for y in range(b, b +10):
            ground[x][y] = 1

count = 0
for r in range(100):
    for c in range(100):
        if ground[r][c] == 1:
            count += 1
print(count)
