import copy

# 얕은복사와 깊은복사
# 얕은복사 : 겉 원소만 복사되고, 내부 배열은 여젼히 원본배열을 참조함
# 깊은복사 : 모든 원소 값만 복사. 원본을 바꿔도 깊은복사본은 안 바뀜

### 얕은 복사 ###
lst = [0, [1, 2]]
shallow = lst.copy()  # copy.copy(lst) 랑 동일
lst[0] = "A"
lst[1][0] = "B"
print(lst)  # ['A', ['B', 2]]
print(shallow)  # [0, ['B', 2]]
# 그냥 카피를 하면 겉 원소는 값 복사가 되지만, 내부 배열은 값만 카피하는게 아니라 실제로 같은 객체임.

### 깊은 복사 ###
lst = [0, [1, 2]]
deep = copy.deepcopy(lst)
lst[0] = "A"
lst[1][0] = "B"
print(lst)  # ['A', ['B', 2]]
print(deep)  # [0, [1, 2]]
# deepcopy 는 내부 배열까지 값만 복사한 것이라서 원본 배열을 바꿔도 딥카피본은 안 바뀜
