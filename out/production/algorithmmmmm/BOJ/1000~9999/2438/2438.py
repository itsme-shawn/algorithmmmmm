import sys

[N] = map(int, sys.stdin.readline().split())

for i in range(N):
    for j in range(i+1):
        print('*', end='')
    print('')
