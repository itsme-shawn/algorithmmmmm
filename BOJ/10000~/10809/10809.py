import sys

word = sys.stdin.readline().rstrip()

for ch in range(ord("a"), ord("z") + 1):
    print(word.find(chr(ch)), end=" ")
