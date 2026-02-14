"""
문자열에서 특정 문자/패턴 등장 위치 전부 찾기.
find, index, enumerate 다양한 패턴 비교.
"""


def using_find(s: str, target: str) -> list[int]:
    idx = -1
    res = []
    while True:
        idx = s.find(target, idx + 1)
        if idx == -1:
            break
        res.append(idx)
    return res


def using_enumerate(s: str, target: str) -> list[int]:
    return [i for i, ch in enumerate(s) if ch == target]


if __name__ == "__main__":
    text = "Hello World"
    print(using_find(text, "l"))  # [2, 3, 9]
    print(using_enumerate(text, "l"))
