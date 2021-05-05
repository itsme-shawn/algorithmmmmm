N = int(input())

lst = [0] * 10001  # 40000바이트(40KB)

for i in range(N):
    lst[int(input())] += 1

for i in range(N):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)
