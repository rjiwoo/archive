# # 두 개의 문자열 s1과 s2. s1의 각 글자가 s2에 모두 존재하는가?

# s1 = 'XYPV'
# s2 = 'EOGGXYPVSY'

# if s1 in s2:
#     print('True')
# else:
#     print('False')


# for i in s1:
#     if i not in s2:
#         print('False')
#     break
# print('True')


# # 'Z'가 존재하는가?

# N = int(input())
# arr = [list(input()) for _ in range(N)]

# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 'Z':
#             print(r,c)
#             print('True')

# # N과 N x N 크기의 문자열 배열 입력
# N = int(input())
# text = [input() for _ in range(N)]

# is_found = False
# for row_str in text:
#     if 'Z' in row_str:
#         is_found = True
#         break  # 'Z'를 찾으면 반복문 종료

# print(is_found)




# #집중호우 피해구역 수는?
N = int(input())
arr = [input() for _ in range(N)]

count = 0
for i in arr:
    for j in i:
        if j == '#':
            count += 1

print(count)


# AB
# CD
# 해당 패턴이 있는지?
N = int(input())
text = [input() for _ in range(N)]

found = False
for r in range(N - 1):  # 행은 N-1까지만 순회
    for c in range(N - 1):  # 열은 N-1까지만 순회
        if text[r][c] == 'A' and text[r][c+1] == 'B' and \
           text[r+1][c] == 'C' and text[r+1][c+1] == 'D':
            found = True
            break
    if found:
        break

print(found)