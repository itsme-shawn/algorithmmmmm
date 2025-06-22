import sys

for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    lst = []
    n = int(input())
    for _ in range(n):
        lst.append(input())
    for item in lst:
        if item.lower() == item[::-1].lower():
            print("YES")
        else:
            print("NO")
    print()
