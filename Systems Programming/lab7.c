#include <stdio.h>
#include <time.h>
#include <string.h>


int main(int argc){

    //initialize variables
    long secDiff, nSecDiff, epocSecDiff;
    int size;
    char string1[100], string2[100];
    double epocNaSecDiff;
    struct timespec spec;
    time_t sec1, sec2;
    clock_gettime(CLOCK_REALTIME, &spec);
    long epocSec1 = (long)spec.tv_sec, epocSec2;
    long double epocNaSec1 = (long double)1.0e-9*spec.tv_nsec, epocNaSec2, totalDiff;
    
    //prompt for, get string and place end of string
    printf("Please enter a string: \n");
    fgets(string1, 100, stdin);
    size = strlen(string1);
    string1[size-1] = '\0';
    
    //Loop until user enters wrong string
    while(1){
        //init first time (timer starter)
        epocSec1 = (long)spec.tv_sec, epocSec2;
        epocNaSec1 = (double)1.0e-9*spec.tv_nsec, epocNaSec2;

        //prompt for a string, get string, and place end of string
        printf("\nPlease enter the same string: \n");
        fgets(string2, 100, stdin);
        size = strlen(string2);
        string2[size-1] = '\0';

        //get new time
        clock_gettime(CLOCK_REALTIME, &spec);
        epocSec2 = (long)spec.tv_sec;
        epocNaSec2 = (long double)1.0e-9*spec.tv_nsec;
        
        //check if it is the same string if not end program
        if(strcmp(string2, string1) != 0){
            printf("%s\t!=\t%s", string2, string1);
            break;
        }

        //get difference in time
        epocSecDiff = epocSec2 - epocSec1;
        epocNaSecDiff = epocNaSec2 - epocNaSec1;
        totalDiff = (long double)epocSecDiff + (long double)epocNaSecDiff;
        
        //Print the time taken to type
        printf("Time: %0.9Lf seconds\n", totalDiff);
        
    }

    return 0;
}





