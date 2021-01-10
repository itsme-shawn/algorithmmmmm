# start 와 end 까지 더하는 함수를 divide and conquer 를 이용해 구현
def consecutive_sum(start, end):
  # base case
  if(start == end):
    return start

  mid = (start + end) // 2

  return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)


print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
