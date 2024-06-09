import sys

input = sys.stdin.readline

n = int(input())
string = []
for _ in range(n):
    string.append(input().rstrip())


# 회문인지 검사
def palindrome(s, e, temp):
    while s <= e:
        if str[s] == str[e]:
            s += 1
            e -= 1

        # 회문이 아니라면 아닌 곳에서 한 문자 배제하고 재귀로 다시 회문검사
        else:
            if temp == 0:
                left = palindrome(s + 1, e, temp + 1)  # 왼쪽 문자 제거
                right = palindrome(s, e - 1, temp + 1)  # 오른쪽 문자 제거
                return min(left, right)
            else:
                return 2
    return temp


result = []
for str in string:
    s, e = 0, len(str) - 1
    result.append(palindrome(s, e, 0))

for r in result:
    print(r)
