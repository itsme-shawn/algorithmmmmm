import sys

read = sys.stdin.readline

n = int(read())

tree = {}

for _ in range(n):
    root, left, right = read().split()
    tree[root] = [left, right]


def preorder(node):
    print(node, end="")
    if tree[node][0] != ".":
        preorder(tree[node][0])
    if tree[node][1] != ".":
        preorder(tree[node][1])


def inorder(node):
    if tree[node][0] != ".":
        inorder(tree[node][0])
    print(node, end="")
    if tree[node][1] != ".":
        inorder(tree[node][1])


def postorder(node):
    if tree[node][0] != ".":
        postorder(tree[node][0])
    if tree[node][1] != ".":
        postorder(tree[node][1])
    print(node, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
