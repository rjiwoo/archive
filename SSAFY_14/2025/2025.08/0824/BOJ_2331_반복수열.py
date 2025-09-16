# 백준 2331번 반복수열

# D[1] = A
# D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합

A, P = map(int, input().split())

# 수열을 저장할 리스트
D = [A]

# 반복을 찾을 때까지 계속 실행
while True:
    # 현재 수열의 가장 마지막 항을 가져옴
    current_num = D[-1]
    
    # 다음 항을 계산
    next_num = 0
    
    # 각 자릿수를 P제곱하여 더하는 과정
    # 숫자를 문자열로 바꿔 한 글자씩 처리
    for digit in str(current_num):
        next_num += int(digit) ** P
        
    # 만약 새로 계산된 숫자가 이미 존재하면
    if next_num in D:
        # 해당 숫자가 처음 나타난 인덱스를 찾음
        # 이 인덱스가 반복을 제외한 부분의 길이와 같음
        result = D.index(next_num)
        print(result)
        break 
    else:
        # 수열에 없는 새로운 숫자라면 리스트에 추가
        D.append(next_num)