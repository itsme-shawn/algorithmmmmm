import sys
# sys.setrecursionlimit(1500)

N = int(input())
own = list(map(int, sys.stdin.readline().split()))
M = int(input())
check = list(map(int, sys.stdin.readline().split()))

own.sort()

# 이진탐색 재귀
def binary_search(arr, target, start=0, end=None):
  if end==None :
    end = len(arr) - 1

  mid = (start + end ) // 2
  while (start <= end) :
    if (arr[mid] < target):
      return binary_search(arr, target, mid+1, end) 
    elif (arr[mid] > target):
      return binary_search(arr, target, start, mid-1)
    else: # find
      return 1
  return 0

for i in range(len(check)):
  print(binary_search(own, check[i]), end=' ')
