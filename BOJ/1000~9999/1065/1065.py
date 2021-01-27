import sys

N = int(sys.stdin.readline())

result = 0

if( N < 100 ):
  result = N
else:
  result = 99
  for i in range(100,N+1):
    arr = list(map(int, list(str(i))))  # 숫자 123 -> arr : [1, 2, 3]
    if( 2*arr[1] == arr[0] + arr[2]):
      result += 1
  
print(result)