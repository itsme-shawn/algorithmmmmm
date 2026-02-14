import sys

sys.stdin = open("in1.txt", "rt")

n = int(input())
lst = sys.stdin.readline().split()


def reverse(x):
    return int(x[::-1])


# 1 리턴 시 소수, 0 리턴 시 소수아님
def isPrime(x):
    flag = 1
    if x == 1:
        return 0
    for i in range(2, int(x ** (1 / 2)) + 1):
        if i == x:
            continue
        if x % i == 0:
            flag = 0
            break
    return flag


for item in lst:
    rev = reverse(item)
    if isPrime(rev):
        print(rev, end=" ")

print()
