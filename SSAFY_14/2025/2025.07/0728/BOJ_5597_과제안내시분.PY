# 5597번 과제 안 내신분?

student = []
for _ in range(28):
    N = int(input())
    student.append(N)

not_submit = []

for i in range(1,31):
    if i not in student:
        not_submit.append(i)

not_submit.sort()
print(not_submit[0])
print(not_submit[1])
