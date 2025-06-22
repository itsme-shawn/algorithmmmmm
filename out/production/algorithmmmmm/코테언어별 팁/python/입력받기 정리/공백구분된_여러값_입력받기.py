import sys

# 1. split() 함수는 string 타입의 list 를 반환

x = sys.stdin.readline().split()    # input: 1 2 3

print(x)   # output: ['1', '2', '3']


# 2. map() 으로 각 원소들을 int 타입으로 변환하고, map() 의 리턴값 자체로는
# 값을 볼 수 없으므로 list() 를 사용해서 list 로 변환

y = list(map(int, sys.stdin.readline().split()))   # input: 1 2 3

print(y) # output: [1, 2, 3]


# unpacking 이용 (map 객체는 이터레이터라서 list로 굳이 변환안해줘도 됨)

N, M = map(int, sys.stdin.readline().split()) # input : 1 2

print(N, M)   # output: 1 2
