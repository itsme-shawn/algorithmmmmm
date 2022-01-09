# replace(없앨값, 변경값, [바꿀횟수])

text = " 123,456,789,999 "

replace_t0 = text.replace(",", "0")
replace_t1 = text.replace(",", "", 1)  # 첫 등장하는 1개만 바꿈
replace_t2 = text.replace("9", "")

print("전체길이:", len(text))
print(replace_t0)
print(replace_t1)
print(replace_t2)
print("제거후길이:", len(replace_t2))

"""
전체길이: 16
 123045607890999
 123456,789,999
 123,456,78,
제거후길이: 12
"""

# 공백 제거 하기 1 : replace() 함수 사용
print(text.replace(" ", ""))

# 공백 제거 하기 1 : strip() 함수 사용
# 하지만 strip() 은 좌우 양 끝 공백만 제거할 수 있다는 단점이 있음
print(text.strip())
