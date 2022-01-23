import sys

word = sys.stdin.readline().rstrip().upper()

dic = dict()
for ch in word:
    if ch not in dic.keys():
        dic[ch] = 1
    else:
        dic[ch] += 1

maxx = max(dic.values())
max_cnt = 0
max_ch = ""

for key, value in dic.items():
    if value == maxx:
        max_cnt += 1
        max_ch = key
    if max_cnt > 1:
        print("?")
        break
else:
    print(max_ch)
