/**
 * This program forks a separate process using the fork()/exec() system calls.
 *
 * Figure 3.09
 *
 * @author Silberschatz, Galvin, and Gagne
 * Operating System Concepts  - Ninth Edition
 * Copyright John Wiley & Sons - 2013
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{

  char *p;
  int num;

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
  pid_t pid;

	/* fork a child process */
	pid = fork();

	if (pid < 0) { /* error occurred */
		fprintf(stderr, "Fork Failed\n");
		return 1;
	}
	else if (pid == 0) { /* child process */
    printf("I am the child %d\n ",pid);
    printf("%d", num);

    while(1){
      if(num % 2 == 0){
        num = num /2;
      } else{
        num = (num * 3) + 1;
      }

      printf(" ,%d", num);
      if( num == 1) exit(0);
    }
    
		execlp("/bin/ls","ls",NULL);
	}
	else { /* parent process */
		/* parent will wait for the child to complete */
		printf("I am the parent %d\n",pid);
		wait(NULL);
		
		printf("\nChild Complete\n");
	}
    
    return 0;
}
