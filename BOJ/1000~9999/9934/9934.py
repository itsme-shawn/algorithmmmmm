# 직접 이진트리 순회하면서 값 저장하기

import sys
# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

k = int(read())
nodes = list(map(int, read().split()))

tree = [0] * (2**k-1)

# tree = list(range(1,2**k))

i = 0

def mid_order(n):
    global i
    if n < 2**k - 1:
        mid_order(n*2 + 1)
        # print(tree[n])
        tree[n] = nodes[i]
        i += 1
        mid_order(n*2 + 2)

mid_order(0)

for j in range(k):
    print(" ".join(map(str,tree[2**j-1:2**(j+1)-1])))