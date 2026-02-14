"""
for 문 반복변수/이터러블 조작 주의.
- 파이썬 for 는 반복변수를 내부에서 바꿔도 다음 반복에 영향 없음.
- 리스트를 순회하며 동시에 수정하면 누락이 발생할 수 있음.
- 인덱스 제어가 필요하면 while 또는 range 기반 for 사용.
"""


def mutate_loop_var() -> None:
    for i in range(5):
        i = 100  # 무시됨
        print(i, end=" ")  # 0 1 2 3 4
    print()


def mutate_iterable() -> None:
    arr = ["a", "b", "c", "d"]
    for x in arr:
        arr.pop()  # 뒤에서 제거 => 일부만 순회
        print(x)  # a, b 만 출력

    # 안전한 방식: while + 인덱스
    arr = ["a", "b", "c", "d"]
    idx = 0
    while idx < len(arr):
        print(arr[idx])
        idx += 1


if __name__ == "__main__":
    mutate_loop_var()
    mutate_iterable()
