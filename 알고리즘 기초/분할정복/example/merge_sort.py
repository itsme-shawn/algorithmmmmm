# merge : 정렬된 두 리스트 list1과 list2를 받아서, 하나의 정렬된 리스트를 리턴하는 함수
def merge(list1, list2):
  newlist = []
  i = j = 0
  while(i < len(list1) and j < len(list2)):
    if(list1[i] <= list2[j]):
      newlist.append(list1[i])
      i += 1
    else:  # ( list1[i] > list2[j])
      newlist.append(list2[j])
      j += 1
  if(i == len(list1)):  # list2 가 아직 다 안들어옴
    newlist += list2[j:]
  if(j == len(list2)):
    newlist += list1[i:]
  return newlist

# merge_sort : 합병 정렬
def merge_sort(my_list):
  # base case
  if(len(my_list) <= 1):
    return my_list
  
  mid = len(my_list) // 2  # 분할
  left = merge_sort(my_list[:mid])  # 정복
  right = merge_sort(my_list[mid:]) # 정복

  return merge(left,right)  # 결합

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))