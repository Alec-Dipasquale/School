#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <utime.h>

int main(int argc,char *argv[]){

    FILE *fp;
    char fileName[50];
    char str[50];

    if(argc >= 2){
        strcpy(fileName, argv[1]);
        fp = fopen(fileName, "a+");
        if ( fp == NULL )
        {
            printf( "Could not open file %s" , fileName) ;
            return 1;
        }

        if(argc == 3){
           utime(fileName, argv[2]);
        }
    } else {
        printf("\nThis is the argv: %s\n", argv[1]);
    }

    // fgets();

    fclose(fp);
    return 0;
}