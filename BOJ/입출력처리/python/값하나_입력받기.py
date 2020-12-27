import sys

# 1. Enter(개행)까지 입력을 받기 때문에 사실상 못 쓴다.
x = sys.stdin.readline()   # input: 1

print(x)  # output: 1\n

# 2. input 값을 string 타입의 list 로 리턴한다.
y = sys.stdin.readline().split()  # input: 2

print(y)  # output: ['2']

# 3. 흔히 아는 int(input()) 과 똑같이 기능한다. map 객체 unpacking 을 위해 list 로 변환
[z] = map(int, sys.stdin.readline().split())  # input: 3

print(z)  # output: 3


