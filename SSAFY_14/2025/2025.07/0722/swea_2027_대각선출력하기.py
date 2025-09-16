# swea 2027번 대각선 출력하기

for i in range(5):
    s=''
    for j in range(5):
        if i==j:
            s+='#'
        else:
            s+='+'
    print(s) 