# swea 4866번 괄호검사

T = int(input())

for tc in range(1, T+1):

    text = input()
    top = -1
    stack = [0]*100

    is_correct = 1

    for i in text:
        if i == '(' or i =='{':
            top += 1
            stack[top] = i

        elif i ==')' or i == '}':

            # 앞에 들어간 거 없이 괄호 닫히면
            if top == -1:
                is_correct = 0 # 오류
                break


            # 괄호 종류 비교?
            elif i ==')' and stack[top] == '(':
                top -= 1
            elif i == '}' and stack[top] == '{':
                top -= 1
                
            else:
                    is_correct = 0
                    break

                
                    
    if top != -1:
        is_correct = 0


    print(f'#{tc} {is_correct}')