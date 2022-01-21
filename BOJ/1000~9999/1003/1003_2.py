import sys

t = int(sys.stdin.readline())
cnt_zero = [0] * 41
cnt_one = [0] * 41

cnt_zero[0] = 1
cnt_zero[1] = 0
cnt_one[1] = 1

for i in range(2, 41):
    cnt_zero[i] = cnt_zero[i - 1] + cnt_zero[i - 2]
    cnt_one[i] = cnt_one[i - 1] + cnt_one[i - 2]


for _ in range(t):
    n = int(sys.stdin.readline())

    print(cnt_zero[n], cnt_one[n])
