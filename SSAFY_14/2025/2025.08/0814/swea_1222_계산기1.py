# swea 1222번 계산기1

T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
 
    # 후위표기식으로 변환
    stack = [0]*100
    top = -1
 
    postfix = ''  # 후위식
    for x in fx:
        if x != '+':   # 피연산자(숫자)면 후위식에 추가
            postfix += x

        else:   # 연산자면
            # 스택에 남아있는 연산자를 모두 꺼내 후위식에 추가
            while top != -1:    
                postfix += stack[top]
                top -= 1

            # 현재 연산자를 스택에 쌓기    
            top += 1  
            stack[top] = x

    # 스택에 남아있는 마지막 연산자를 후위식에 추가
    while top != -1:
        postfix += stack[top]
        top -= 1
 
 
    # 후위표기식 연산
    sum_stack = [0]*100
    top = -1

    for i in postfix:
        if i != '+':    # 피연산자
            top += 1
            sum_stack[top] = int(i)
        else:   # 연산자
            op2 = sum_stack[top]    # 피연산자 꺼내기
            top -= 1
            op1 = sum_stack[top]    # 피연산자 꺼내기
            top -= 1
            if i == '+':  # op1 + op2
                top += 1  # 스택에 넣기
                sum_stack[top] = op1 + op2
 
    print(f'#{tc} {sum_stack[top]}')