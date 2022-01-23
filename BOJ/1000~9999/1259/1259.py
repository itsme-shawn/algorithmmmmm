import sys

while True:
    string = list(sys.stdin.readline().rstrip())
    if string == ["0"]:
        break
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            print("no")
            break
    else:
        print("yes")
