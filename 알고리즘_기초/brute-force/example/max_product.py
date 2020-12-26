def max_product(left_cards, right_cards):
  max_result = left_cards[0] * right_cards[0]

  # iterable 한 컨테이너에 대해 for .. in 문으로 직접 원소에 접근가능
  for left in left_cards:
    for right in right_cards:
      max_result = max(max_result, left * right) # 내장함수인 max 함수를 사용
  return max_result

print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))



# max 함수를 사용하면 더 편리하다.
