import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    print(R, S)
    rep = int(R)
    for ch in range(len(list(S))):
        print(ch * rep, end="")
