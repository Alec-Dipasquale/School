/**
 * Simple program demonstrating shared memory in POSIX systems.
 *
 * This is the producer process that writes to the shared memory region.
 *
 * Figure 3.17
 *
 * @author Silberschatz, Galvin, and Gagne
 * Operating System Concepts  - Ninth Edition
 * Copyright John Wiley & Sons - 2013
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>

int main(int argc, char *argv[])
{
	const int SIZE = 4096;
	const char *name = "OS";

	int shm_fd;
	void *ptr;

	/* create the shared memory segment */
	shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);

	/* configure the size of the shared memory segment */
	ftruncate(shm_fd,SIZE);

	/* now map the shared memory segment in the address space of the process */
	ptr = mmap(0,SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
	if (ptr == MAP_FAILED) {
		printf("Map failed\n");
		return -1;
	}

	/**
	 * Now write to the shared memory region.
 	 *
	 * Note we must increment the value of ptr after each write.
	 */
  char *p;
  int num;
	char text[40];

  if( argc == 2 ) {
    long conv = strtol(argv[1], &p, 10);
    num = conv;
    printf("The argument supplied is %d\n", num);
      if(num < 0){
        printf("Must be a positive integer!\n");
        exit(0);
      }
   }
   else if( argc > 2 ) {
      printf("Too many arguments supplied.\n");
      exit(0);
   }
   else {
      printf("One argument expected.\n");
      exit(0);
   }
	 	printf("producer %d", num);
	 	sprintf(text, "%d", num);
    sprintf(ptr,"%s",text);
	  ptr += strlen(text);

    while(1){
      if(num % 2 == 0){
        num = num /2;
      } else{
        num = (num * 3) + 1;
      }

      sprintf(text, ", %d", num);
      sprintf(ptr,"%s",text);
	    ptr += strlen(text);
			printf(",%d", num);
      if( num == 1) break;
    }
		sprintf(ptr,"\n");
		printf("\n");

	return 0;
}
