"""
replace/strip 로 문자열 일부 교체 및 공백 제거.
"""


def replace_examples() -> None:
    text = " 123,456,789,999 "
    print(text.replace(",", ""))  # 모든 쉼표 삭제
    print(text.replace(",", "", 1))  # 첫 1개만 삭제
    print(text.replace("9", ""))  # 특정 문자 제거


def strip_examples() -> None:
    text = "  hello  "
    print(text.strip())  # 양끝 공백 제거
    print(text.replace(" ", ""))  # 모든 공백 제거


if __name__ == "__main__":
    replace_examples()
    strip_examples()
