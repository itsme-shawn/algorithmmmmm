# 시간초과
import sys

while True:
  try: 
    x, y = map(int, sys.stdin.readline().split())
    z = (y*100) // x
    cnt = 0
    temp = z

    if(z == 99 or z == 100):
      print(-1)
    else:
      while(z == temp):
        x += 1
        y += 1
        z = (y*100) // x
        cnt += 1
      print(cnt)

  except: break


