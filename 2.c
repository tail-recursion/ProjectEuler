
/*

Each new term in the Fibonacci sequence is generated by adding the previous two terms.

By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

*/
#include <stdio.h>

int main(int argc, char* argv[]) {
  int a = 1, b = 2;
  int temp;
  int sum = 0;
  while (b < 4000000) {
    temp = a + b;
    a = b;
    if (b % 2 == 0) {
      sum += b;
    }
    b = temp;
  }
  printf("Sum of even valued fibonacci numbers below four million: %d\n", sum);
  return 0;
}
