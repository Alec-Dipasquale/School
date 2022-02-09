/**
 * A pthread program illustrating how to
 * create a simple thread and some of the pthread API
 * This program implements the summation function where
 * the summation operation is run as a separate thread.
 *
 * Most Unix/Linux/OS X users
 * gcc thrd.c -lpthread
 *
 * Solaris users must enter
 * gcc thrd.c -lpthreads
 *
 * Figure 4.9
 *
 * @author Gagne, Galvin, Silberschatz
 * Operating System Concepts  - Ninth Edition
 * Copyright John Wiley & Sons - 2013
 */

#include <pthread.h>
#include <stdio.h>

int average; /* this data is shared by the thread(s) */
int min;
int max;
int argCount;

void *avg_runner(int arr[]); /* the thread */
void *min_runner(int arr[]);
void *max_runner(int arr[]);

int main(int argc, char *argv[])
{
pthread_t tid; /* the thread identifier */
pthread_attr_t attr; /* set of attributes for the thread */

argCount = argc;
int arr[argCount];
if (argCount < 2) {
	fprintf(stderr,"usage: a.out <integer value> <integer value> etc...\n");
	/*exit(1);*/
	return -1;
} else
if (argCount == 2) {
	printf("The average value is %d\n",atoi(argv[1]));
	printf("The minimum value is %d\n",atoi(argv[1]));
	printf("The maximum value is %d\n",atoi(argv[1]));
  return 0;
} else{
  for(int i = 1; i < argc; i++){
    if (atoi(argv[i]) < 0) {
      fprintf(stderr,"Argument %d must be non-negative\n",atoi(argv[i]));
      /*exit(1);*/
      return -1;
    }
    arr[i-1] = atoi(argv[i]);
  }
}

/* get the default attributes */
pthread_attr_init(&attr);

/* create the threads */
pthread_create(&tid,&attr,avg_runner,arr);
pthread_create(&tid,&attr,min_runner,arr);
pthread_create(&tid,&attr,max_runner,arr);

/* now wait for the threads to exit */
pthread_join(tid,NULL);
printf("average = %d\n",average);
printf("minimum = %d\n",min);
printf("maximum = %d\n",max);
}

/**
 * The thread will begin control in these functions
 */
void *avg_runner(int arr[]) 
{
  int sum = 0;
  for(int i = 0; i < argCount-1; i++)
  {
    sum += arr[i];
    average = sum / (argCount-1);
  }

  pthread_exit(0);
}

void *min_runner(int arr[]) 
{
  min = arr[0];
  for(int i = 0; i < argCount-1; i++)
  {
    if(min > arr[i]){
      min = arr[i]; 
    }
  }
  pthread_exit(0);
}

void *max_runner(int arr[]) 
{
    max = arr[0];
  for(int i = 0; i < argCount-1; i++)
  {
    if(max < arr[i]){
      max = arr[i]; 
    }
  }

  pthread_exit(0);
}