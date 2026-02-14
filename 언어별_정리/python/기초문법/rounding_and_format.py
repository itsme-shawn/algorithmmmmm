"""
파이썬의 반올림과 출력 포맷 정리.
- 기본 round 는 'banker's rounding'(짝수 쪽) 이므로 경계값 0.5 처리 시 주의.
- Decimal 을 쓰면 코딩테스트에서 자주 요구되는 '5 올림' 방식으로 제어 가능.
- f-string 으로 자리수 고정 출력하기.
"""

from decimal import Decimal, ROUND_HALF_UP


def builtin_round_examples() -> None:
    """round 기본 동작 예시"""
    print(round(4.5), round(3.5))  # 4, 4 (짝수 방향)
    print(round(1.2345, 3))  # 소수 셋째 자리까지 (1.235)


def half_up_round(x: float, ndigits: int = 0) -> float:
    """
    0.5 이상이면 항상 올림하는 방식(ROUND_HALF_UP).
    Decimal 을 거쳐 문자열로 변환하는 비용이 있지만, 출력용이라면 충분히 빠름.
    """

    quantize_exp = Decimal(1).scaleb(-ndigits)  # 10^{-ndigits}
    d = Decimal(str(x)).quantize(quantize_exp, rounding=ROUND_HALF_UP)
    return float(d)


def format_examples() -> None:
    """f-string 자리수 고정 및 천 단위 구분"""
    pi = 3.14159265
    print(f"{pi:.2f}")  # 3.14
    num = 1234567
    print(f"{num:,}")  # 1,234,567


if __name__ == "__main__":
    builtin_round_examples()
    print(half_up_round(2.345, 2))  # 2.35
    print(half_up_round(4.5))  # 5.0
    format_examples()
