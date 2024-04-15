# sequence.count() : 해당 sequence 객체 에 데이터가 몇 개 있는지 리턴
# 시퀸스 객체는 a[0],a[1] 과 같이 순차적인 인덱스로 접근할 수 있어야 한다.
# 시퀸스 객체인 문자열,리스트,튜플 가능
# 시퀸스 객체가 아닌 딕셔너리,set 은 불가능

# 문자열
print("hello world".count("ll"))
# 1

# 리스트
print(["ab", "abc", "ab", "abcd"].count("ab"))
# 2
# 리스트는 각 원소를 한 덩어리로 취급

print([1, 1, 1, 2, 2, 3].count(1))
# 3


# 딕셔너리
print(("ab", "abc", "ab", "abcd").count("ab"))
# 2
# 튜플도 리스트와 사용법 동일
