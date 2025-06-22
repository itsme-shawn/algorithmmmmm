import sys

a = input()  # ab cd 입력
print(a)  # 'ab cd'

# 우선 split('구분자') 함수를 이해해야한다.
# split('구분자') 은 구분자를 기준으로 문자열을 잘라서 리스트를 리턴하는 함수이다.
# 따라서 '구분자' 에 공백이 들어오면, 공백단위로 문자열을 잘라서 리스트를 리턴하게 된다.

b = input().split()  # ab cd 입력
print(b)  # ['ab', 'cd'] => split() 은 리스트를 리턴함을 알 수 있음.

c = sys.stdin.readline()  # ab cd 입력
print(c)  # 'ab cd\n' => 개행문자가 들어옴!!

c = sys.stdin.readline().rstrip()  # ab cd 입력
print(c)  # 'ab cd' => 개행문자 안 들어옴

d = sys.stdin.readline().split()  # ab cd 입력
print(d)  # ['ab', 'cd']=> split() 을 해주게 되면 개행문자 없어짐
# readline() 을 쓸 때에도 split() 을 해주면 개행문자 사라져서 굳이 rstrip() 안 해줘도 된다.

# 문자열에 list() 를 해주면 문자 하나하나가 리스트의 원소가 된다.

e = list(input())
print(e)  # ['a', 'b', ' ', 'c', 'd']

# 주의 : split()을 먼저 해버리면 문자열이 아닌 리스트 상태이므로 문자 하나하나를 못 쪼개준다.
f = list(input().split())
print(f)  # ['ab', 'cd'] => split() 자체가 list를 만들어주기 때문에 굳이 list() 해줄 필요 없음

g = list(sys.stdin.readline())
print(g)  # ['a', 'b', ' ', 'c', 'd', '\n'] => 문자들이 각각 원소가 되고, 개행까지 같이 들어옴

g = list(sys.stdin.readline().rstrip())
print(g)  # ['a', 'b', ' ', 'c', 'd'] => input() == sys.stdin.readline().rstrip()

h = list(sys.stdin.readline().split())
print(h)  # ['ab', 'cd'] => 앞에서 말한 언급한 주의사항의 예시
# split() 을 하고 list() 를 하면 의미가 없다. split() 을 하면 이미 통으로 된 list 임.
