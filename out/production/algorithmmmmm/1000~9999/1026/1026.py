import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


B.sort(reverse=True)
A.sort()
result = 0

for i in range(len(A)):
    result += A[i] * B[i]

print(result)
