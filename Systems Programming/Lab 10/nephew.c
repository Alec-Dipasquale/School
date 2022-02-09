#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char **argv){
        int sleepTime = atoi(argv[1]);
        sleep(sleepTime);
        printf("\n%s finished in %d seconds!\n", argv[0], sleepTime);

        exit(0);
}
