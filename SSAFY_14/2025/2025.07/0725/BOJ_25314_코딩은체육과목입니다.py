# 25314

N = int(input())

type_str = ''
for i in range(0,N//4):
    if i == 0:
        type_str = 'long int'
    else:
        type_str = 'long '*(i+1)
        type_str += 'int' 

print(type_str)