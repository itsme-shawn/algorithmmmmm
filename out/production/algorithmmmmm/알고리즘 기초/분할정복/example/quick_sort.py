# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(lst, idx1, idx2):
  lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(lst, start, end):
  pivot_idx = end 
  big_idx = cur_idx = start # small 그룹의 첫 번째 요소는 start 인덱스이므로 small_idx 변수 필요없음

  # cur_idx 가 pivot_idx 보다 작을 동안만 loop
  while( cur_idx < pivot_idx ):
    if( lst[cur_idx] >= lst[pivot_idx] ): # cur_idx 가 가리키는 요소를 big 그룹에 추가
      cur_idx += 1
    elif( lst[cur_idx] < lst[pivot_idx] ):  # cur_idx 가 가리키는 요소를 small 그룹에 추가
      swap_elements(lst, cur_idx, big_idx)  # cur_idx 의 요소를 big 그룹의 첫 요소와 swap 함
      cur_idx += 1
      big_idx += 1  # cur_idx 와 big_idx 가 한 칸씩 전진함으로써 small 그룹도 확장됨
    
  # pivot 요소와 big 요소를 swap 하고 big_idx 를 1 늘려주면 small, pivot, big 그룹으로 partiton 완료  
  swap_elements(lst, pivot_idx, big_idx)
  pivot_idx = big_idx 
  big_idx += 1

  return pivot_idx

# 퀵 정렬
def quicksort(lst, start=None, end=None):

  # Set Optional Parameter
  if( start == None and end == None):
    start = 0
    end = len(lst) - 1  # pivot 을 항상 대상 list 의 맨 오른쪽으로 설정하는 퀵소트임

  # base case
  if( start > end ):
    return
  
  pivot = partition(lst, start, end)  # 분할
  quicksort(lst, start, pivot-1)      # 정복
  quicksort(lst, pivot+1 , end)       # 정복

  # quick sort 는 원래 list 상에서 sort 를 하기 때문에, 결합 과정이 필요없음


# 테스트 0
list0 = [1, 6, 5, 3, 4]
quicksort(list0, 0, len(list0) - 1)
print(list0)  # [1, 3, 4, 5, 6]
  
# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)  # [1, 3, 5, 7, 9, 11, 11, 13]

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)  # [1, 5, 7, 9, 13, 15, 28, 30, 48]

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)  # [1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]