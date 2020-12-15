import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
check = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target) :
  start = 0
  end = len(arr)-1

  while start <= end :
    mid = int(( start + end ) / 2)
    if arr[mid] < target :
      start = mid + 1
    elif arr[mid] > target :
      end = mid - 1
    else : 
      return 1
  return 0

A.sort()

for i in range(0,M):
  print(binary_search(A, check[i]))

# 삽입정렬 쓰면 매우느려짐, sort() 내장함수사용


