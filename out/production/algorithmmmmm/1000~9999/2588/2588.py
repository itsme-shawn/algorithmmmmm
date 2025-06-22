import sys

a = int(sys.stdin.readline())
b = list(input())
# b = list(sys.stdin.readline().split()[0])

digit = 1
sum = 0

for item in reversed(b) :
  res = a*int(item)
  print(res)
  sum += res * digit
  digit *= 10

print(sum)

'''
arr.reverse() vs list(reversed(arr))

1. arr.reverse() : 원본자체를 거꾸로 뒤집음. return 값은 없음

2. list(reversed(arr)) : 원본은 그대로 놔두고, 뒤집힌 list_reverseiterator object 를 return 함.
따라서 list() 를 취해줘야 리스트처럼 사용할 수 있다.
( iterator 이기 때문에 for 문에선 그대로 사용가능 )

'''