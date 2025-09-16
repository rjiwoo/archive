# swea 1240번 단순 2진 암호코드

code_map = {'0001101': 0, 
            '0011001': 1, 
            '0010011': 2, 
            '0111101': 3,
            '0100011': 4, 
            '0110001': 5, 
            '0101111': 6, 
            '0111011': 7,
            '0110111': 8, 
            '0001011': 9
            }

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    binary_code = ''

    for i in range(N):
        line = input()
        if '1' in line:
            binary_code = line

    # print(binary_code)

    last_index = -1
    # 암호 끝 점 찾기.모두 1로 끝남
    # 찾은 줄에서 
    for i in range(M-1,-1,-1):
        if binary_code[i] == '1':
            last_index = i
            break
    
    # 암호의 길이는 무조건 56이니까
    # 마지막 인덱스를 찾으면 시작점을 찾을 수 있음
    start_index = last_index - 55
    real_binary_code = binary_code[start_index:last_index+1]

    # print(real_binary_code)

    final_code = []
    # 처음부터 암호의 길이까지 7개씩 나눠
    for j in range(0,56,7):
        temp = real_binary_code[j:j+7] # 7개씩 나눠서 저장하고
        final_code.append(code_map[temp]) # 그 부분을 code_map의 키와 대조에서 값으로 변환해서 저장?

    # print(final_code)

    # 검증코드
    # 홀수자리(인덱스로 0, 2, 4, 6, 8)의 합 *3
    # 짝수자리(인덱스로 1, 3, 5, 7)

    odd_sum = 0
    even_sum = 0

    # 8개의 숫자에 대해 홀수/짝수 자리의 합 계산
    for i in range(8):
        # 인덱스가 0, 2, 4, 6 (홀수 자리)인 경우
        if i % 2 == 0:
            odd_sum += final_code[i]
        # 인덱스가 1, 3, 5, 7 (짝수 자리)인 경우
        else:
            even_sum += final_code[i]
    
    total_sum = odd_sum*3 + even_sum
    ans = 0

    if total_sum % 10 == 0:
        for i in range(8):
            ans += final_code[i]
    
    print(f'#{tc} {ans}')