# 에라토스테네스의 체 방법 사용

import sys
import math

T = int(input())
arr = list()
for _ in range(T):
  arr.append(int(input()))

MAX = int(max(arr))

# 소수 리스트 초기화
primeList = [False, False] + [True] * (MAX- 1)

for i in range(2, int(math.sqrt(len(primeList)))+1 ):
  if (primeList[i] == True):
    for j in range(i*2, len(primeList) , i):
      primeList[j] = False

for i in range(T):
  check = int(arr[i] / 2)
  while check >= 2 :
    if primeList[check] and primeList[arr[i]-check]:
      print(check,arr[i]-check)
      break
    else: 
      check -= 1