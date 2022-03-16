import sys

sys.stdin = open("in1.txt", "rt")

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
diff = []
dic = {}
temp = []
print(lst)

# 파이썬 round 에 이슈가 있다고는 하는데 일단은 넘어갔음
avg = round(sum(lst) / len(lst))
print("avg:", sum(lst) / len(lst))

# temp : 이중리스트 [ [인덱스,값,차이], ... ]
for x in enumerate(lst):
    x = list(x)
    x.append(abs(avg - x[1]))
    temp.append(x)

# 차이 를 기준으로 해서 제일 작은 값을 검색해나가다가, 같은 차이 값이 나오면 값이 더 큰 것, 값까지 같으면 인덱스가 작은 것 선택

# find : 현재까지의 해
find = temp[0]
for item in temp:
    if item[2] < find[2]:
        find = item
    elif item[2] == find[2]:
        if item[1] > find[1]:
            find = item
        elif item[1] == find[1]:
            if item[0] < find[0]:
                find = item

print(avg, find[0] + 1)  # 몇 번째니까 인덱스에다가 +1 해줘야함
