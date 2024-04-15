# find(찾는문자열[, 시작인덱스 [, 끝인덱스]]) : 문자열만 사용가능 (리스트,튜플,딕셔너리 불가능)
# index(찾는문자열[, 시작인덱스 [, 끝인덱스]]) : 리스트,튜플,문자열 사용가능 (딕셔너리불가능)

string = "Hello World"

# 1. for문
for i in range(len(string)):
    if string[i] == "l":
        print(i)  # 2 3 9

# 2. for문 리스트 컴프리헨션
index_list = [i for i in range(len(string)) if string[i] == "l"]
print(index_list)  # [2,3,9]

# 3. find 함수 사용 (시작점 옵션 활용)
idx = -1
index_list = []
while True:
    idx = string.find("l", idx + 1)
    if idx == -1:
        break
    index_list.append(idx)
print(index_list)  # [2,3,9]

# 4. index 함수 => 찾는 문자가 없을 시 에러를 리턴하므로 count() 함수를 같이 써줘야함.
# 이 방법은 find 함수에서도 그대로 사용가능
idx = -1
index_list = []
while True:
    if string.count("l", idx + 1) == 0:
        break
    else:
        idx = string.index("l", idx + 1)
        index_list.append(idx)
print(index_list)  # [2,3,9]

# 5. filter 와 lambda 함수 사용
# filter(조건 함수, 순회 가능한 데이터)
# 조건 함수의 리턴값이 True 인 데이터만 추려냄
index_list = list(filter(lambda x: string[x] == "l", range(len(string))))
print(index_list)  # [2,3,9]

# 6. enumerate 사용
index_list = []
for i, v in enumerate(string):
    if v == "l":
        index_list.append(i)
print(index_list)  # [2,3,9]

# 7. enumerate 리스트 컴프리헨션
index_list = [i for i, v in enumerate(string) if v == "l"]
print(index_list)  # [2,3,9]
