import sys
from collections import deque

while True:
    try:
        string = input()
        if string == ".":
            break
        check = deque()
        flag = 0
        for letter in string:
            if letter == "(" or letter == "[":
                check.append(letter)
            elif check and letter == ")" and check[-1] == "(":
                check.pop()
            elif check and letter == "]" and check[-1] == "[":
                check.pop()
            elif letter == ")" or letter == "]":
                print("no")
                flag = 1
                break
        if flag == 0:
            if not check:
                print("yes")
            else:
                print("no")

    except:
        break
