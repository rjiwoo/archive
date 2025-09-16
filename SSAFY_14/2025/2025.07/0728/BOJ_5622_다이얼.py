#5622번 다이얼

dial = [
    '',        # 0번
    '',        # 1번
    'ABC',     # 2번
    'DEF',     # 3번
    'GHI',     # 4번
    'JKL',     # 5번
    'MNO',     # 6번
    'PQRS',    # 7번
    'TUV',     # 8번
    'WXYZ'     # 9번
]

word = input()
time = 0
for char in word:
    for i in range(len(dial)):
        if char in dial[i]:
            time += i+1

print(time)