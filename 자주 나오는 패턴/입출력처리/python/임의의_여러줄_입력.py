import sys

while True:
  try: x, y = map(int, sys.stdin.readline().split()) # int 값으로 변환 -> 문제 상황마다 바꿔주면 됨
  except: break
  print(x, y)