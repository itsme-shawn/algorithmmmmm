"""
문자-아스키(유니코드) 변환 정리.
- ord : 문자 -> 코드포인트
- chr : 코드포인트 -> 문자
코딩테스트에서 알파벳 인덱스 계산, 숫자문자 처리에 자주 활용.
"""


def ascii_examples() -> None:
    print(ord("A"), ord("a"))  # 65, 97
    print(chr(97))  # 'a'

    digit = "7"
    print(int(digit), ord(digit) - ord("0"))  # 7, 7

    alphabet_index = ord("c") - ord("a")  # 0-based
    print(alphabet_index)  # 2


if __name__ == "__main__":
    ascii_examples()
