import sys
import math

T = int(input())
arr = list()
for _ in range(T):
  arr.append(int(input()))

# return 값 False : 소수가 아님 / True : 소수
def isPrime(num):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0 : return False 
  return True 

for i in range(T):
  check = int(arr[i] / 2)
  while check >= 2 :
    if isPrime(check) and isPrime(arr[i]-check):
      print(check,arr[i]-check)
      break
    else: 
      check -= 1