# 파라미터 some_list를 거꾸로 뒤집는 함수
# 내 코드
'''
def flip(some_list):
  length = len(some_list)
  if(length <= 1):
    return some_list
  else:
    return [some_list[length-1]] + flip(some_list[1:length-1]) + [some_list[0]]
'''

# 더 좋은 코드
def flip(some_list):
  # base case
  if len(some_list) == 0 or len(some_list) == 1:
      return some_list

  # recursive case
  return some_list[-1:] + flip(some_list[:-1])
  # 파이썬에서는 리스트의 마지막 인덱스를 몰라도 -1 인덱스로 처리가능하다!!!
    
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 핵심point: 부분문제로 쪼개기
# 9 를 맨 앞으로 보내고 [1,2,3,4,5,6,7,8] 을 flip 하면 됨
# [1,2,3,4,5,6,7,8] 을 flip 하는 것은 전체문제의 부분문제임

# 시간복잡도 계산
# base case : O(1)
# recursive case : 재귀호출횟수(flip함수) : n번 , 각 호출의 시간복잡도 : O(n-1) (some_list[:-1] 은 O(n-1) 이기 때문) => O(n^2)
# 총 시간복잡도 : O(n^2)

