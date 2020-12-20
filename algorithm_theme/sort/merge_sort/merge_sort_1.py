# merge_sort : 병합정렬의 주 함수
def merge_sort(arr, start=None, end=None):
  if (start == None and end == None):
    start = 0
    end = len(arr) - 1
  
  if (start < end):
    mid = start + (end - start) // 2  # mid = (start + end) // 2 와 동일 (오버플로우 방지 스킬)
    merge_sort(arr, start, mid) # 분할(Divide) : 왼쪽 리스트
    merge_sort(arr, mid+1, end) # 분할(Divide) : 오른쪽 리스트
    merge(arr, start, mid, end) # 정복(Conquer)

def merge(arr, start, mid, end):
  for i in range(start, end+1):
    temp[i] = arr[i]     # temp 배열에 원본배열을 그대로 복사함
    
  part1 = start         # part1 : 왼쪽 리스트의 인덱스 역할
  part2 = mid + 1       # part2 : 오른쪽 리스트의 인덱스 역할
  index = start         # index : 원본 리스트(arr)의 인덱스 역할

  # 왼쪽 리스트와 오른쪽 리스트를 비교하면 실제로 merge 하는 작업
  while (part1 <= mid and part2 <= end):
    if (temp[part1] <= temp[part2]):
      arr[index] = temp[part1]
      part1 += 1
    else:
      arr[index] = temp[part2]
      part2 += 1
    index += 1
  
  # while 이 끝나고 왼쪽 리스트(part1)가 남아있으면 원본 리스트에 담아준다.
  # 오른쪽 리스트(part2)는 검사를 안하는 이유는 
  # 왼쪽 리스트(part1)가 다 원본으로 담아졌다면,
  # 이미 오른쪽 리스트는 원본리스트에 정렬된 채로 존재할 것이다.
  if (part1 <= mid and part2 > end): # 사실 if 문은 없어도됨 (코드이해를 위해 남겨둠)
    for i in range(0, (mid - part1) + 1):
      arr[index + i] = temp[part1 + i]

arr = [30, 50, 80, 90, 10, 0, 20]
temp = list()  # 임시배열은 전역변수로 사용하는게 메모리 효율적

for _ in range(0, len(arr)):
  temp.append(0)

print('Before sorted : ', arr)

merge_sort(arr)

print('After sorted : ', arr)