# swea 1946번 간단한 압축 풀기

# 첫번째 풀이
T = int(input())

for tc in range(1, T+1):
    n = int(input()) # 줄 번호
    line = ''
    for _ in range(n):
        alpha, num = input().split()
        num = int(num)
        line += alpha*num

    print(f'#{tc}')

    for i in range(0, len(line), 10):
        print(line[i:i+10])
