import sys

# 0. Enter(개행)까지 입력을 받기 때문에 사실상 PS 에서는 쓸 일이 거의 없다
w = sys.stdin.readline()   # input: 1

print(w)  # output: 1\n

# 1. sys.stdin.readline() 를 int 함수로 감싸주면 숫자 하나를 받기에 좋다. -> 매우 유용

x = int(sys.stdin.readline())   # input: 1

print(x)  # output: 1

# 2. input 값을 string 타입의 list 로 리턴한다.
y = sys.stdin.readline().split()  # input: 2

print(y)  # output: ['2']

# 3. 흔히 아는 int(input()) 과 똑같이 기능한다. map 객체 unpacking 을 위해 list 로 변환
[z] = map(int, sys.stdin.readline().split())  # input: 3

print(z)  # output: 3


