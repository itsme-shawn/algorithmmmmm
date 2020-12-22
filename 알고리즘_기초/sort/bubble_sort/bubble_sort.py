def bubble_sort(list) :
  for cnt in range(0, len(list)) : # 바깥 루프
    for idx in range(0, len(list)-1-cnt) : # 안쪽 루프
      if( list[idx] > list[idx+1]) :
        list[idx], list[idx+1] = list[idx+1], list[idx]
        
        '''
          temp = list[idx]
          list[idx] = list[idx+1]
          list[idx+1] = temp
        '''
  return list

print(bubble_sort([7,4,5,3,1]))

