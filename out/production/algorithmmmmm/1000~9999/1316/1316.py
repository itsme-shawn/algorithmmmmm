import sys

n = int(input())
cnt = 0

for _ in range(n):
    # dict.fromkeys() 이럴때는 어케쓰는지?
    string = list(sys.stdin.readline())
    # split() 마지막에 하면 안되는 이유?

    alpha = dict()
    for char in string:
        if char not in alpha:
            alpha[char] = 1
        else:
            alpha[char] += 1

    for i in range(len(string)):
        if alpha[string[i]] >= 2:
            if string[i] != string[i + 1]:
                break
            alpha[string[i]] -= 1
    else:
        cnt += 1

print(cnt)
