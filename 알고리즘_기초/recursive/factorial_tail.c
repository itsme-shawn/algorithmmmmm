#include <stdio.h>

int FactorialTail(int n, int acc){  // acc : accumulator
	if (n == 1) return acc;
	return FactorialTail(n - 1, acc * n);    //  일반 재귀에서의 n * Factorial(n-1)와 달리 반환값에서 추가 연산을 필요로 하지 않음
}

int Factorial(int n){
  return FactorialTail(n, 1);
}

int main(){
  int result = Factorial(4);
  
  printf("%d", result);
  return 0;
}


