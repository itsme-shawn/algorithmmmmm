n = int(input())
dic = {}

for _ in range(n):
    a = input()
    dic[a] = len(a)

words = sorted(dic.items())  # 딕셔너리의 키를 기준으로 딕셔너리를 정렬 (오름차순 디폴트)
sortedWords = sorted(words, key=lambda x: x[1])

print(words)
# [('but', 3), ('cannot', 6), ('hesitate', 8), ('i', 1), ('im', 2), ('it', 2), ('more', 4), ('no', 2), ('wait', 4), ('wont', 4), ('yours', 5)]
print(sortedWords)
# [('i', 1), ('im', 2), ('it', 2), ('no', 2), ('but', 3), ('more', 4), ('wait', 4), ('wont', 4), ('yours', 5), ('cannot', 6), ('hesitate', 8)]

for i in sortedWords:
    print(i[0])
