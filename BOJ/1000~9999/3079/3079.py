import sys

fileName = "1.txt"
sys.stdin = open(fileName, "rt")
read = sys.stdin.readline

n, m = map(int, read().split())
print(n, m)

lines = [int(read()) for _ in range(n)]



