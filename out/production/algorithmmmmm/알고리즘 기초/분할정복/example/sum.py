# start 와 end 까지 더하는 함수를 divide and conquer 를 이용해 구현
def consecutive_sum(start, end):
  # base case
  if(start == end):
    return start

  mid = (start + end) // 2  # 분할

  return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)  
  # 각각의 consecutive_sum() 호출은 정복
  # 두 함수의 리턴값을 더하는 과정이 결합

# base case 를 반복문으로 해결한 경우
'''
def consecutive_sum(start, end):
  # base case
  while(start != end):

    mid = (start + end) // 2  # 분할

    return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)  
    # 각각의 consecutive_sum() 호출은 정복
    # 두 함수의 리턴값을 더하는 과정이 결합

  return start
'''

print(consecutive_sum(1, 10))   # 55
print(consecutive_sum(1, 100))  # 5050
print(consecutive_sum(1, 253))  # 32131
print(consecutive_sum(1, 388))  # 75466
