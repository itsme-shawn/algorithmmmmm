# 딕셔너리나 Counter 를 이용한 개수세기

from collections import Counter

# 1. fromkeys 로 딕셔너리 생성 => 다만, 고정된 value 로만 초기화 가능
keyList = ["a", "a", "a", "b", "b", "c"]

dic_1 = dict.fromkeys(keyList, 0)
print(dic_1)  # {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

# 2. 일반적인 방식으로 딕셔너리 생성 => 데이터까지 한 번 삽입가능
dic_2 = dict()
for key in keyList:
    if key not in dic_2:
        dic_2[key] = 0
    dic_2[key] += 1

print(dic_2)  # {'a': 3, 'b': 2, 'c': 1}

# 3. collections 모듈의 Counter 클래스 사용
dic_3 = Counter("hello world")
print(
    dic_3
)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(dict(dic_3))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

dic_4 = Counter(keyList)
print(dict(dic_4))  # {'a': 3, 'b': 2, 'c': 1}

# 응용
# 4. 주어진 단어에서 가장 많이 등장하는 알파벳과 그 개수 구하는 함수
def find_max(word):
    counter = Counter(word)  # 개수가 담긴 카운터 생성(딕셔너리 대체)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count


print(find_max("hello world"))  # ('l', 3)
