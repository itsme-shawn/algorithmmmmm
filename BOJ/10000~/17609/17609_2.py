import sys

input = sys.stdin.readline

n = int(input())
strings = []
for _ in range(n):
    strings.append(input().rstrip())


def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


result = []
for s in strings:
    if is_palindrome(s):
        result.append(0)
    else:
        left, right = 0, len(s) - 1
        temp = 0
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                temp += 1
                left += 1
        result.append(temp)

for r in result:
    print(r)
