# merge 방식을 통해 정렬된 temp 리스트를 return 하는 함수
def merge(left, right):
  temp = list()
  i = 0   # left array index
  j = 0   # right array index

  while(i < len(left) and j < len(right)):
    if(left[i] <= right[j]):
      temp.append(left[i])
      i += 1
    else:
      temp.append(right[j])
      j += 1
  
  if(i == len(left)):
    temp += right[j : len(right)]
  if(j == len(right)):
    temp += left[i : len(left)]
  return temp

def merge_sort(arr):
  if(len(arr) <= 1):
    return arr
  
  mid_idx = len(arr) // 2 # 분할

  left = merge_sort(arr[0:mid_idx])         # 정복 : 왼쪽 부분배열 정렬
  right = merge_sort(arr[mid_idx:len(arr)]) # 정복 : 오른쪽 부분배열 정렬
  return merge(left, right) # 결합 : 정렬된 왼쪽,오른쪽 부분배열 결합

print(merge_sort([30, 50, 80, 90, 10, 0, 20]))

