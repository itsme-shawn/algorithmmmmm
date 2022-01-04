import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    S = list(S)
    for char in S:
        print(char * R, end="")
    print("")
