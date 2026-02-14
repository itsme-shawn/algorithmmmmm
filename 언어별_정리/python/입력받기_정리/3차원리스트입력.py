# 3차원리스트 입력받아서 만들기

# 방법1 : 빈 배열에 2차원리스트 넣기
h, row, col = map(int, input().split())

arr = []

for i in range(h):
    temp = []
    for j in range(row):
        temp.append(list(map(int, input().split())))
    arr.append(temp)  # 이차원리스트 append

print(arr)

# 방법2 : 리스트 컴프리헨션으로 이차원리스트 만들고 인덱스로 이차원리스트 넣어주기
h, row, col = map(int, input().split())

arr = [[] for _ in range(h)]

for i in range(h):
    arr[i] = [list(map(int, input().split())) for _ in range(row)]

print(arr)

# 방법3 : 리스트 컴프리헨션만으로 3차원리스트 만들기
h, row, col = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(row)] for _ in range(h)]

print(arr)


"""
높이2,행3,열4

[input]

2 3 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
21 22 23 24

[output]

[
    [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], 
    [ [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24] ]
]

"""
