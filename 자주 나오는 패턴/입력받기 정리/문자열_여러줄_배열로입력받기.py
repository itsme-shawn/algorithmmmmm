import sys

# 행의 수는 보통 주어진다.
# 리스트 컴프리헨션 이용

# 1. 띄어쓰기없는 문자열/정수를 입력받아서 1차원 배열에 문자열로 저장

N = int(input())  # 숫자 하나 정도는 input() 으로 쓰자.. N : 행 수
graph = [input() for _ in range(N)]
# graph = [sys.stdin.readline().split()[0] for _ in range(N)]

# extend 이용
'''
graph = []

for _ in range(N):
  graph.extend(sys.stdin.readline().split())
'''

print(graph)

# -----------------결과--------------------
# input:
'''
  5
  WLLWWWL
  LLLWLLL
  LWLWLWW
  LWLWLLL
  WLLWLWW
'''

# output:
'''
  ['WLLWWWL', 'LLLWLLL', 'LWLWLWW', 'LWLWLLL', 'WLLWLWW']
'''
# --------------------------------------------


# 2. 띄어쓰기없는 문자열/정수를 입력받아서 2차원 배열에 저장

M = int(input())
maze = [list(input()) for _ in range(M)]

# string 을 list로 형 변환시키면, string 이 문자 개별로 분리되는 성질 이용
# 정수데이터일때 : maze = [list(map(int, input())) for _ in range(M)]

# sys.stdin.readline().split() 을 사용하면 이미 문자열 통째로 리스트가 만들어지기 때문에 이 경우는 그냥 input() 을 쓰는게 편하다.
# 굳이 sys 모듈을 쓸꺼면 아래처럼 쓰면 되긴함.
# maze = [ list(sys.stdin.readline().split()[0]) for _ in range(M)]


print(maze)

# -----------------결과--------------------
# input:
'''
  5
  WLLWWWL
  LLLWLLL
  LWLWLWW
  LWLWLLL
  WLLWLWW
'''

# output:
'''
[
  ['W', 'L', 'L', 'W', 'W', 'W', 'L'], 
  ['L', 'L', 'L', 'W', 'L', 'L', 'L'], 
  ['L', 'W', 'L', 'W', 'L', 'W', 'W'], 
  ['L', 'W', 'L', 'W', 'L', 'L', 'L'], 
  ['W', 'L', 'L', 'W', 'L', 'W', 'W']
]
'''
# --------------------------------------------


# 3. 띄어쓰기있는 문자열/정수를 입력받아서 2차원 배열에 저장

K = int(input())
arr = [list(map(str, sys.stdin.readline().split())) for _ in range(K)]
# 정수형일 때는 map() 의 첫 번째인자를 int로 바꿔주면 됨

print(K)

# -----------------결과--------------------
# input:
'''
  3
  apple banana mango
  one two three
'''

# output:
'''
[
  ['apple', 'banana', 'mango'], 
  ['one', 'two', 'three']
]

'''
# --------------------------------------------

# 참고 : https://johnyejin.tistory.com/62