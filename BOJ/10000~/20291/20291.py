import sys

# sys.stdin = open("in.txt")
read = sys.stdin.readline

n = int(read())

dic = dict()

for _ in range(n):
    fn = read().rstrip().split(".")
    ext = fn[1]
    
    if ext not in dic:
        dic[ext] = 1
    else:
        dic[ext] += 1

result = sorted(list(dic.items()))

for fn,ext in result:
    print(fn, ext)