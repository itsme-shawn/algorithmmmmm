# input() : 개행문자 \n 안 들어옴
# sys.stdin.readline() : 개행문자 까지 같이 들어옴 => 조심해야함

# 정리
# input() == sys.stdin.readline().rstrip()

import sys

a = input()  # abc 입력
b = sys.stdin.readline()  # abc 입력
c = sys.stdin.readline().rstrip()  # abc 입력

print(len(a))  # 3 (개행문자는 안 셈)
print(len(b))  # 4 (개행문자까지 같이 셈)
print(len(c))  # 3 (개행문자 없어짐)
