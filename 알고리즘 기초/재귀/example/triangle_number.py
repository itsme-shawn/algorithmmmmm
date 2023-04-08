# n번째 triangle number 는 자연수 1부터 n 까지의 합을 일컫는다 (n>=1)

# 재귀로 구현
def triangle_number(n):
  if(n==1):
    return 1
  else:
    return n + triangle_number(n-1)

for i in range(1, 11):
  print(triangle_number(i))