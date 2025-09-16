# 백준) 6단계. 심화 1 - 1157번. 단어 공부

# 알파벳 대소문자로 이루어진 단어 제공. 가장 많이 사용된 알파벳 탐색
# 대소문자 구분X
# 출력) 가장 많이 사용된 단어 대문자로 출력, 여러개일경우 ? 출력

# 단어 입력 받기, 대문자로 모두 변경
word = input().upper()

# 해당 알파벳이 몇 번 나왔는지 저장
new = {}
for i in word:
    if i not in new:
        new[i] = 1
    else:
        new[i] += 1

# print(new)

# 가장 많이 나온 횟수 찾기
max_count = max(new.values())

# 가장 많이 나온 알파벳 찾기
# items() 사용법 다시 한 번 확인해보기. 얻어걸림
result = []
for char, count in new.items():
    if count == max_count:
        result.append(char)

# 많이 사용된 알파벳이 몇 개인지 확인 후 출력
if len(result) > 1:
    print('?')
else:
    print(*result) 