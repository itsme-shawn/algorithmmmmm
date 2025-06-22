def binary_search(element, some_list, start_index=0, end_index=None):
  # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
  if end_index == None:
    end_index = len(some_list) - 1
  
  while(start_index <= end_index):
    mid = (start_index + end_index) // 2
    if(some_list[mid] > element):
      return binary_search(element, some_list, start_index, mid-1)
    elif(some_list[mid] < element):
      return binary_search(element, some_list, mid+1, end_index)
    else:
      return mid
  return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

# 시간복잡도 : 반복문과 마찬가지로 탐색범위가 반절씩 줄기때문에 재귀함수가 lg n 번 호출된다. 따라서 시간복잡도는 O(log n) 이다.