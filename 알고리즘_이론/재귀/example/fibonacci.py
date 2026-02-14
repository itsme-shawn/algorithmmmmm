def fib(n):
  if(n == 1 or n == 2):   # base case
    return 1
  else:                   # recursive case
    return fib(n-1) + fib(n-2)

for i in range(1,11):
  print(fib(i))

# 시간복잡도 : O(2^n) (fib(1) 이나 fib(2) 가 호출되기 전까지 각 단계마다 원래 문제의 2배로 문제가 늘어나기 때문)

# 재귀함수의 시간복잡도 계산 : (base case의 시간복잡도) * (recursive case의 시간복잡도)

# base case : O(1)
# recursive case : O(2^n)
