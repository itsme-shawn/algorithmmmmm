def selection_sort(list) :
  for i in range(0, len(list)-1) : # 외부 루프 : n-1 번
    min_idx = i
    for j in range(i+1, len(list)) : # 내부 루프 : 최솟값 탐색
      if( list[j] < list[min_idx] ) :
        min_idx = j
    list[i], list[min_idx] = list[min_idx], list[i] # SWAP
  return list

print(selection_sort([7,4,5,3,1]))