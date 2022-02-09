/*
Write a C program that does a large number of references to elements of two-dimensional arrays, 
using only subscribing. For example, you may do matrix multiplication or addition.  
You can repeat the operation multiple times. Write a second program that does the same operations 
but uses pointers and pointer arithmetic for the storage-mapping function to do the array references. 
Compare the readability and time efficiency of the two programs and explain your opinion. 
*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define ROW 100
#define COL 50

void array_subscript();
void array_pointers(int iterations);

int main(void) {
  int iterations =4;

  //measure time and output of matrix addition
  //using subscript in array
  clock_t t;
  t = clock();
  //init array subscript
  array_subscript(iterations);
  t = clock() - t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
  printf("array_subscript() took %f seconds to execute \n", time_taken);

  //measure time and output of matrix addition
  //using pointer in array
  t = clock();
  //init array pointer
  array_pointers(iterations);
  t = clock() - t;
  time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
  printf("array_pointers() took %f seconds to execute \n", time_taken);

  return 0;
}

void array_subscript(int iterations)
{ 
  //assuming that the usage of
  
  int arr[ROW][COL];

  for (int i = 0; i < ROW; i++)
    for (int j = 0; j < COL; j++)
      arr[i][j] = 1;
  int count = 0, i, j;

  while (count != iterations){
    for(j=0; j<COL ; j++){
      for(i=0; i<ROW; i++){
      arr[i][j] = arr[i][j] + arr[i][j]; //no operation is done, only accessing the element

      }
      // printf("after addition arr[%d][%d] = %d\n", i, j, arr[i][j]);

    }
    count++;
  }

  return ;
}

void array_pointers(int iterations){
  int arr[ROW][COL]; 
  for (int i = 0; i < ROW; i++)
    for (int j = 0; j < COL; j++)
      arr[i][j] = 1;

  int *pointerArr = &arr[0][0];
  int count = 0,i ,j;

  while (count != iterations){
    for(j=0; j<COL ; ++j){
      for(i=0; i<ROW; ++i){
        *(pointerArr + ( i * COL) + j) = *(pointerArr + ( i * COL) + j) + *(pointerArr + ( i * COL) + j);
      }
      

    }
    count++;

  }
  return ;
}