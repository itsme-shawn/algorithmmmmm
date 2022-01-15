#### 파이썬 for 문 유의 #####
# 한줄요약 : 파이썬에서 반복문 내에서 인덱스 조작을 할 일이 있으면 for문 보다 while 문을 써라

# 1. for 문 변수(i) 변경 불가능
# python 의 for문은 c언어의 for문 과 다르게 for문 내부에서 for 문 변수를 변경하지 못한다. #
for i in range(10):
    print(i, end=" ")
    i = 10  # 내부에서 i 를 10 으로 변경해도 다음 루프 때 i 는 그냥 다음 값으로 덮어씌워진다.

# 출력 : 0 1 2 3 4 5 6 7 8 9

# 2. 최초 범위(range) 변경 불가능
# 반복문 변수 뿐만 아니라 iterator 를 range 로 줄 시에는, for문 내부에서 range에 해당하는 객체를 조잭해도 최초 루프 수에 영향을 안 주는듯함.
lst = [1, 2, 3, 4, 5, 6]
i = 0
for i in range(len(lst)):
    lst.clear()
    print(i)
# 0 1 2 3 4 5 출력됨.
# for문 내부에서 lst 를 없앴는데도 불구하고, for문 루프횟수(len(lst)) 에는 영향을 안 줬음.


# 하지만 range 가 아니라 리스트에서 직접 빼낼때는 영향을 줌.
lst = ["a", "b", "c", "d", "e", "f"]
for letter in lst:
    del lst[-1]  # 매 시행마다 맨 마지막 원소 제거
    print(letter)
# a b c 출력됨. for문 내부에서 lst 를 변경한 게 for문 루프횟수에 영향을 줬음.

# while 문은 우리의 예상대로 반복문 내부의 조작이 루프 수에 영향을 줌
lst = [1, 2, 3, 4, 5, 6]
i = 0
while len(lst) > 0:
    lst.clear()
    print(i)
    i += 1
# 0 출력
