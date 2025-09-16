# swea 4865번 글자수

T = int(input())

for tc in range(1, T+1):

    str1 = input()
    str2 = input()

    count = 0
    max_value = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        if max_value < count:
            max_value = count
        count = 0

    

    print(f'#{tc} {max_value}')