from itertools import combinations, permutations, product

items = [1, 2, 3, 4]

print(list(permutations(items, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

print(list(combinations(items, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# 두 개 이상의 리스트에서 각각 원소를 뽑은 조합
lists = [["a", "b", "c"], [1, 2, 3], ["가", "나"]]
print(
    list(product(*lists))
)  # list unpacking (product 함수는 가변인자를 받으므로 list 를 unpacking 하여 함수에 전달한다.)
# print(list(product(["a", "b", "c"], [1, 2, 3], ["가", "나"]))) 와 동일
"""
[('a', 1, '가'), ('a', 1, '나'), ('a', 2, '가'), ('a', 2, '나'), ('a', 3, '가'), ('a', 3, '나'), 
('b', 1, '가'), ('b', 1, '나'), ('b', 2, '가'), ('b', 2, '나'), ('b', 3, '가'), ('b', 3, '나'),
('c', 1, '가'), ('c', 1, '나'), ('c', 2, '가'), ('c', 2, '나'), ('c', 3, '가'), ('c', 3, '나')]
"""

# 응용
# 'A', 'B', 'C' 로 만들 수 있는 경우의 수 생성
pool = ["A", "B", "C"]
print(list(map("".join, permutations(pool, 2))))
# ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
