A, B, C = map(int, input().split())

if(A==B==C):
    result = 10000 + A*1000
elif(A==B):
    result = 1000 + A*100
elif(B==C):
    result = 1000 + B*100
elif(A==C):
    result = 1000 + A*100
else:
    big = max(A,B,C)
    result = big*100
print(result)

# A, B, C = map(int, input().split())

# if(A==B==C):
#     result = 10000 + A*1000
# elif(A==B):
#     result = 1000 + A*100
# elif(B==C):
#     result = 1000 + B*100
# elif(A==C):
#     result = 1000 + A*100
# else:
#     if(A>B and A>C):
#         result = A*100
#     elif(B>A and B>C):
#         result = B*100
#     else:
#         result = C*100
# print(result)