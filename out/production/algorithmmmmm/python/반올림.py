# 파이썬의 round 반올림 함수는 round_half_even 방식을 택한다.
# 반올림되는 수가 반올림의 경계(0.5, 0.05, ...)일 때, 짝수 쪽으로 반올림이 된다.

print(round(4.5))  # 결과가 5가 아니라 4 => 짝수인 4를 향함
print(round(3.5))  # 결과는 4 => 짝수인 4를 향함

print(3.5 % 1)

# 주어진 수에 0.5를 더해서 반올림하는 방식을 사용할텐데,
# 소수 첫째 자리가 0인 경우(ex. 3) 0.5를 더해서 반올림하면 안 되므로 체크를 해준다.
def my_round(a):
    if a % 1 == 0:  # 3.0 % 1 == 0
        return a
    else:
        return round(a + 0.5)


print(my_round(3))  # 3
print(my_round(3.5))  # 4
print(my_round(4.5))  # 5
