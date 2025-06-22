import heapq as hq

# 이렇게 사용 하면 안됨.
# bt = hq.heapify([1, 2, 3, 4, 5, 6, 7]) # 잘못 사용한 예시

bt = [1, 2, 3, 4, 5, 6, 7]
hq.heapify(bt)  # 인자로 힙 생성을 원하는 리스트를 넣어주면, 그 리스트가 힙으로 변함
length = len(bt)

# 전위순회
def pre_order(i):
    if i < length:
        print(bt[i], end=" ")
        pre_order(2 * i + 1)
        pre_order(2 * i + 2)


# 중위순회
def in_order(i):
    if i < length:
        in_order(2 * i + 1)
        print(bt[i], end=" ")
        in_order(2 * i + 2)


# 후위순회
def post_order(i):
    if i < length:
        post_order(2 * i + 1)
        post_order(2 * i + 2)
        print(bt[i], end=" ")


# 출력
pre_order(0)
print()
in_order(0)
print()
post_order(0)

"""
return 문 사용하려면 아래와 같이 하면 된다.
def pre_order(i, length=len(bt)):
    if i >= length:
        return
    print(bt[i], end=" ")
    pre_order(2 * i + 1)
    pre_order(2 * i + 2)
"""
