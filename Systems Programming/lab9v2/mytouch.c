//Pair Programming: Alec Dipasquale & Brian Vincello
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <time.h>
#include <utime.h>

#define RVAL 4
#define WVAL 2
#define XVAL 1

int main(int argc, char *argv[])
{
        //Declare variables
        int fd, msgsize, ownerPermission, groupPermission, otherPermission, permissionsNum, index = 0;
        char *permissions, *filename, *message, *dateinput;
        char permissionsNumArray[]="0777", m[20], d[20], y[20];;
        struct utimbuf puttime;
        struct tm askdate;
        int month, day, year;
        time_t date;
        struct stat sfile;

        
         umask(0);

        if(argc > 1){
                // init with command line arguments
                filename=argv[1];
                //create file w/o permissions number
                fd=open(filename, O_CREAT | O_WRONLY, 0777);
                if(argc>3){
                        message=argv[2];
                        dateinput=argv[3];

                        if(argc == 5){
                                permissions=argv[4];
                                //Loop through permissions argument
                                while(index < 9){
                                        //check placement, and correct letter or - and may add to permissionsNum
                                        if( (index == 0 || index == 3 || index == 6) && permissions[index] == 'r'){
                                                permissionsNum = RVAL;
                                        } else if ((index == 1 || index == 4 || index == 7) && permissions[index] == 'w'){
                                                permissionsNum += WVAL;
                                        } else if ((index == 2 || index == 5 || index == 8) && permissions[index] == 'x'){
                                                permissionsNum += XVAL;
                                        } else if(permissions[index], "-"){
                                                printf("");
                                        } else{
                                                printf("Permission formatted wrong!\n");
                                                printf("%s", permissions[index]);
                                                exit(1);
                                        }

                                        //create each permissions number
                                        if(index == 2){
                                                ownerPermission = permissionsNum * 100;
                                                permissionsNum = 0;
                                        } else if(index == 5){
                                                groupPermission = permissionsNum * 10;
                                                permissionsNum = 0;
                                        } else if(index == 8){
                                                otherPermission = permissionsNum;
                                        }
                                        index++;
                                }
                                //combine permissions numbers
                                permissionsNum = ownerPermission + groupPermission + otherPermission;
                                //convert permissions number
                                snprintf(permissionsNumArray, 4, "%d", permissionsNum);
                                permissionsNum = strtol(permissionsNumArray,0, 8);
                                //change permissions of file
                                chmod(filename, permissionsNum);
                        }
                        //separate day month in years in string
                        strcpy(m, strtok(dateinput, "/"));
                        strcpy(d, strtok(NULL, "/"));
                        strcpy(y, strtok(NULL, "/"));

                        // convert strings to integers
                        month=atoi(m);
                        day=atoi(d);
                        year=atoi(y);
                        msgsize=strlen(message);

                        //Set dates in tm
                        askdate.tm_mon=month-1;
                        askdate.tm_mday=day;
                        askdate.tm_year=year-1900;
                        date=mktime(&askdate);
                        puttime.actime=date;
                        puttime.modtime=date;

                        //write to file
                        write(fd, message, msgsize);
                }
        } else{
                printf("Need 1, 3 or 4 arguments\n");
                exit(1);
        }

        if (fd==-1)
        {
                printf("File could not be created.\n");
                exit(1);
        }
        
        //change file time to argument time
        utime(filename, &puttime);

         if(stat(filename, &sfile) == 0) {

        printf("Filename:\n%s\n\n", filename);
        printf("Single line of content:\n%s\n\n", message);
        printf("Date input:\n%s\n\n", dateinput);
        printf("\nFile Permissions User\n");
        printf((sfile.st_mode & S_IRUSR)? "r":"-");
        printf((sfile.st_mode & S_IWUSR)? "w":"-");
        printf((sfile.st_mode & S_IXUSR)? "x":"-");
        printf("\n");
        printf("\nFile Permissions Group\n");
        printf((sfile.st_mode & S_IRGRP)? "r":"-");
        printf((sfile.st_mode & S_IWGRP)? "w":"-");
        printf((sfile.st_mode & S_IXGRP)? "x":"-");
        printf("\n");
        printf("\nFile Permissions Other\n");
        printf((sfile.st_mode & S_IROTH)? "r":"-");
        printf((sfile.st_mode & S_IWOTH)? "w":"-");
        printf((sfile.st_mode & S_IXOTH)? "x":"-");
        printf("\n");
        }

        close(fd);
}
