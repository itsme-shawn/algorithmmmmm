import sys

t = int(input())
for _ in range(t):
    word = sys.stdin.readline().rstrip()
    stack = []
    for x in word:
        if x == "(":
            stack.append(x)
        elif x == ")":
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if stack:
            print("NO")
        else:
            print("YES")
