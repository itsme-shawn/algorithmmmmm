import sys

while True:
  try: 
    x, y = map(int, sys.stdin.readline().split())
    z = (y*100) // x  # z = (y//x) * 100 는 틀리게 됨
    temp = z

    if(z == 99 or z == 100):
      print(-1)
    else:
      start, end = 1, 1500000000 # end 값은 x가 10억, y가 9.899..억 일때를 계산해서 나온 값 ( 좀 여유있게 설정함 )
      while(start <= end):
        mid = (start + end) // 2
        new_z = ((y+mid)*100 // (x+mid))  # ((y+mid) // (x+mid)) * 100 는 틀리게 됨
        if( new_z > temp ):
          result = mid
          end = mid - 1
        else:
          start = mid + 1

      print(result)
          
  except: break