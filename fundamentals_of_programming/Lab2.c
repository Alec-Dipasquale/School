/*
Write three functions in C or C++: one that declares a large integer array statically (static array),
one that declares the same large array on the stack ( local array variable), and one that creates the
same large array from the heap (malloc). You may randomly fill in the values of these array elements.
You may also try different array sizes, such as 1000, 5000 etc. Call each of the subprograms a large
number of times ( at least 100,000) and output the time required by each function. Explain the results
from the perspectives of array memory allocation and deallocation. 
*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define SIZE 1000
#define ARRAYS 100000

void arrayStatic();
void arrayStack();
void arrayHeap();

int main(void) {
  int i;
  clock_t t;
  t = clock();
  for(i = 0 ; i< ARRAYS; i++)arrayStatic();
  t = clock() - t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
  printf("arrayStatic() took %f seconds to execute \n", time_taken);

  t = clock();
  for(i = 0 ; i< ARRAYS; i++)arrayStack();
  t = clock() - t;
  time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
  printf("arrayStack() took %f seconds to execute \n", time_taken);

  t = clock();
  for(i = 0 ; i< ARRAYS; i++)arrayHeap(i);
  t = clock() - t;
  time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
  printf("arrayHeap() took %f seconds to execute \n", time_taken);

  return 0;
}

void arrayStatic(){
  static int staticArray[SIZE] ;
  for(int i = 0; i <SIZE ; i++){
    staticArray[i] = i % 100;
  }
}

void arrayStack(){
  int stackArray[SIZE];
  for(int i = 0; i <SIZE ; i++){
    stackArray[i] = i % 100;
  }
}

void arrayHeap(int count){
  int *heapArray = (int *) malloc(SIZE * sizeof(int)); 
  for(int i = 0; i <SIZE ; i++){
    heapArray[i] = i % 100;
  }
  free(heapArray);
}
/*
  Explanation:
     A static array will automatically allocate and deallocate memory for the array. The size for the static memory will be a fixed size however. With a stack array the allocation and deallocation is automatically done as well but it is not a fixed size. Malloc is used in order to allocate memory for the given array for the heap array. To deallocate the heapArray, the free function is used which takes the pointer as a parameter.

*/