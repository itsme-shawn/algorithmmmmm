import sys

r, c = map(int, input().split())

# puzzle = [list(sys.stdin.readline().split()[0]) for _ in range(r)]
puzzle = []
for _ in range(r):
    puzzle.append(list(sys.stdin.readline().rstrip()))

# puzzle = [['a', 'd', 'a', 'c', 'a'], ['d', 'a', '#', '#', 'b'], ['a', 'b', 'b', '#', 'b'], ['a', 'b', 'b', 'a', 'c']]

# 낱말 기준은 연속 2개

# 가로 낱말
word = []
for row in puzzle:
    lp = rp = 0
    length = len(row)
    while (lp < length) and (rp < length):
        if row[lp] == "#":
            lp += 1
            rp = lp + 1
            continue
        if row[rp] != "#":
            rp += 1
            if rp == length:
                word.append(row[lp:rp])
                break
        if row[rp] == "#":
            word.append(row[lp:rp])
            lp = rp

# 세로 낱말
for j in range(len(puzzle[0])):
    lp = rp = 0
    length = len(puzzle)
    while (lp < length) and (rp < length):
        if puzzle[lp][j] == "#":
            lp += 1
            rp = lp + 1
            continue
        if puzzle[rp][j] != "#":
            rp += 1
            if rp == length:
                temp = []
                for i in range(lp, rp):
                    temp += puzzle[i][j]
                word.append(temp)
                break
        if puzzle[rp][j] == "#":
            temp = []
            for i in range(lp, rp):
                temp += puzzle[i][j]
            word.append(temp)
            lp = rp

# 이렇게 하면 word 에 알파벳 1개인 것도 들어옴
# 어쩔수없이 1개짜리는 수동으로 없애주는 걸로..
ans = []
i = 0
while i < len(word):
    if len(word[i]) == 1:
        del word[word.index(word[i])]
        continue
    string = ""
    for letter in word[i]:
        string += letter
    ans.append(string)
    i += 1

ans.sort()
print(ans[0])
