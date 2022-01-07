''' 풀이1
def insertion_sort(list) : 
  for i in range(1, len(list)) : # 외부 루프 : key 값 지정 (순방향)
    for j in range(i, 0, -1) : # 내부 루프 : key 값과 앞의 인덱스를 비교하면서 SWAP
      if( list[j] < list[j-1]) : 
        list[j-1], list[j] = list[j], list[j-1]
  return list
'''

''' 풀이2
def insertion_sort(arr):
  for end in range(1, len(arr)):
    i = end
    while i > 0 and arr[i - 1] > arr[i]:
      arr[i - 1], arr[i] = arr[i], arr[i - 1]
      i -= 1
  return arr
'''

# 풀이3
def insertion_sort(arr):
  for key_idx in range(1, len(arr)):
    to_insert = arr[key_idx]
    i = key_idx
    while i > 0 and arr[i - 1] > to_insert:
      arr[i] = arr[i - 1]
      i -= 1
    arr[i] = to_insert
  return arr

print(insertion_sort([7,4,5,3,1]))