# swea 6196번. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 4. 변수

T = int(input())

for test_case in range(1, T + 1):
	a = T
	print( a + (a*10+a) + (a*100+a*10+a) +(a*1000+a*100+a*10+a) )