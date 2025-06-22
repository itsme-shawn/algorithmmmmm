import sys

r, c = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
word = []

# 가로
for y in range(r):
    temp = ""
    for x in range(c):
        if board[y][x] != "#":  # '#' 이 아닌 문자일 때 temp 에 추가
            temp += board[y][x]
        if len(temp) > 1 and (
            board[y][x] == "#" or x == c - 1
        ):  # '#' 을 만났거나, 문자열 끝에 도달했을 때 temp 를 word 에 저장하는데 한 글자 초과여야함
            word.append(temp)
            temp = ""
        if len(temp) == 1 and board[y][x] == "#":  # 한 글자 짜리는 버림
            temp = ""

# 세로
for x in range(c):
    temp = ""
    for y in range(r):
        if board[y][x] != "#":
            temp += board[y][x]
        if len(temp) > 1 and (board[y][x] == "#" or y == r - 1):
            word.append(temp)
            temp = ""
        if len(temp) == 1 and board[y][x] == "#":
            temp = ""

word.sort()
print(word[0])
