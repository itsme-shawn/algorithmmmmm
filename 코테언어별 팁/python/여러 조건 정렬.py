"""
sorted(정렬할 데이터)
sorted(정렬할 데이터, reverse 파라미터) : 그냥 순서만 뒤집어줌
sorted(정렬할 데이터, key 파라미터)
sorted(정렬할 데이터, key 파라미터, reverse 파라미터)

sorted() 함수는 리스트를 리턴하므로 인자로 딕셔너리나 튜플을 줘도 리스트가 리턴된다.
"""

a = [(1, 3), (1, 2), (2, 1), (0, 1), (5, 2), (3, 0), (4, 2)]

print(sorted(a))  # sorted(a, key=lambda x: (x[0], x[1])) 와 동일
# [(0, 1), (1, 2), (1, 3), (2, 1), (3, 0), (4, 2), (5, 2)]

print(sorted(a, key=lambda x: (x[0], x[1])))
# [(0, 1), (1, 2), (1, 3), (2, 1), (3, 0), (4, 2), (5, 2)]

print(sorted(a, key=lambda x: x[0]))  # x[0] 기준 오름차순, x[1]은 그냥 나온 순서대로
# [(0, 1), (1, 3), (1, 2), (2, 1), (3, 0), (4, 2), (5, 2)]

print(sorted(a, key=lambda x: -x[0]))  # x[0] 기준 내림차순
# [(5, 2), (4, 2), (3, 0), (2, 1), (1, 3), (1, 2), (0, 1)]

print(sorted(a, key=lambda x: (-x[0], x[1])))  # x[0] 우선 내림차순, x[0] 동일하면 x[1] 오름차순 순
# [(5, 2), (4, 2), (3, 0), (2, 1), (1, 2), (1, 3), (0, 1)]

print(sorted(a, reverse=True))
# [(5, 2), (4, 2), (3, 0), (2, 1), (1, 3), (1, 2), (0, 1)]

print(sorted(a, key=lambda x: (-x[0], x[1]), reverse=True))
# [(0, 1), (1, 3), (1, 2), (2, 1), (3, 0), (4, 2), (5, 2)]

# 딕셔너리 정렬

dic = {"a": 66, "c": 23, "b": -3}
print(dic)
# {'a': 66, 'c': 23, 'b': -3}

print(sorted(dic))  # 그냥 키만 정렬되고, 키만 리턴됨
# ['a', 'b', 'c']

print(sorted(dic.items()))
# [('a', 66), ('b', -3), ('c', 23)]

print(sorted(dic.items(), key=lambda x: x[1]))  # 딕셔너리는 items() 에서만 람다함수 사용가능
# [('b', -3), ('c', 23), ('a', 66)]

print(sorted(dic.keys()))
# ['a', 'b', 'c']

print(sorted(dic.values()))
# [-3, 23, 66]


# 튜플 정렬 => 리스트랑 동일

tpl = ((3, 4), (1, 3), (-1, 6))

print(tpl)
# ((3, 4), (1, 3), (-1, 6)

print(sorted(tpl))
# [(-1, 6), (1, 3), (3, 4)]

print(sorted(tpl, key=lambda x: x[1]))
# [(1, 3), (3, 4), (-1, 6)]
