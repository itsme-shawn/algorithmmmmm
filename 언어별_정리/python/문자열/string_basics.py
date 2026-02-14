"""
문자열 기본기.
- 불변(immutable)하므로 슬라이싱/concat 은 새 문자열을 만든다.
- split/join, lower/upper 등 자주 쓰는 메서드 모음.
"""


def basics() -> None:
    s = "Hello World"
    print(s.lower(), s.upper())
    print(s[::-1])  # 역순
    words = s.split()  # 공백 기준 분리
    print(words)
    print("-".join(words))  # 구분자 넣어 합치기
    print(s.replace("World", "BOJ"))


if __name__ == "__main__":
    basics()
