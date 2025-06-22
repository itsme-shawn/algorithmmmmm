# n의 각 자릿수의 합을 리턴
def sum_digits(n):
  if(n // 10 == 0):
    return n % 10
  else:
    return n % 10 + sum_digits(n // 10)

# sol 2
'''
def sum_digits(n):
  num_to_str = str(n)

  if(len(num_to_str) == 1 ):
    return int(num_to_str)
  else:
    return int(num_to_str[0]) + sum_digits(int(num_to_str[1:]))
'''

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 시간복잡도 : O(log n)