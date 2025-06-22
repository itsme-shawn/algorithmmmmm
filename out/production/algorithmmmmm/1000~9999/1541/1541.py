import sys

input = sys.stdin.readline().rstrip

string = input()

result = 0
temp = ""
flag = 0  # 기존에 '-' 안들어온 상황
for i in range(len(string)):
    if string[i] != "+" and string[i] != "-":
        temp += string[i]
    else:
        if flag == 0:  # 마이너스 아직 안들어온 상황
            if string[i] == "+":
                result += int(temp)
                temp = "+"
                continue
            else:  # '-'
                result += int(temp)
                temp = "-"
                flag = 1
                continue
        else:  # flag == 1 : 마이너스 들어온 상황
            if string[i] == "+":
                result += int(temp)
                temp = "-"
                continue
            else:  # '-'
                result += int(temp)
                temp = "-"

result += int(temp)

print(result)
