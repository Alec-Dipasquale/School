#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main(){
    // create variables some init
    int wstatus;
    char command[50] = "ps -ef | grep ";
    char *theargs[2];
    pid_t pid[4];
    char *arg[2];
    int randomInt = 1;
    char nephewNames[4][10] = {"peepeye", "pipeye", "pupeye", "poopeye"};
    char winOrderNames[4][10];
    int order = 0;
    char  nephewTimes[4][12];
    int popIntPid = getpid();
    char poppid[6];   // ex. 34567
    sprintf(popPid, "%d", popIntPid);

    //add the pid to the grep command
    strcat(command, popPid);
    strcat(command, "| grep -v grep");
    system("clear");

    //show Popeye pid through getpid() and system command
    printf("\nPopeye 'getpid()': %s\n\n", popPid);
    system(command);

    //start the race
    printf("\nPopeye: Ready, Set, Go!!!\n");

     //get and store each random number for each respective child.
     srand( time(NULL));
     for(int i = 0; i< 4; i++){
        randomInt = ((rand()) % 6) + 5;
        snprintf(nephewTimes[i], 12, "%d", randomInt);
     }

     //Create each child process w/ arguments and error handling
     for( int i = 0 ; i< 4; i++){
        if ((pid[i]=fork()) == 0) {


        arg[0] = nephewNames[i];
        arg[1] = nephewTimes[i];
        arg[2] = NULL;
        execvp("./nephew",arg);

        perror("Execvp error");
        _exit(1);
        }
        if (pid[i] < 0) {
                perror("Fork error");
        }
     }

    //show all child processes
    system(command);

    //waiting for terminations and storing in order the names of each process that finished.
    for (int i = 0; i < 4; i++) {
         if (pid[i] > 0) {
             int status;

             waitpid(pid[i], &status, 0);
             if (status == 0) {
                     strcpy(winOrderNames[order], nephewNames[i]);
                     order++;
             }
         }
     }

    //show just popeye is left in processes
    system(command);

    //Have Popeye congratulate the winners
    printf("\n\nPopeye: Congrats to %s for getting in first!\n", winOrderNames[0]);
    printf("Popeye: Congrats to %s for getting in second!\n", winOrderNames[1]);
    printf("Popeye: Congrats to %s for getting in third!\n", winOrderNames[2]);
    printf("Popeye: Congrats to %s for getting in last, NOT!\n", winOrderNames[3]);

    return 0;
}
