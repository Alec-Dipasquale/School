/*
  https://www.cs.rpi.edu/~moorthy/Courses/os98/Pgms/client.c
*/
//Alec Dipasquale and Bryan Vincello Lab11 client.c

#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

void error(char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n, isDone = 1;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char command1[128], command2[128];//arrays for system() greps


    char buffer[256];
    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }
    portno = atoi(argv[2]);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0)
        error("ERROR opening socket");
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr,
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);
    if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0)
        error("ERROR connecting");
    //Loop for continuous messeging, until one of the exits
    for(;;){
        printf("Please enter the message: ");
        bzero(buffer,256);
        fgets(buffer,255,stdin);
        //checks for exit input
    if( strncmp(buffer, "exit", 4 ) == 0 || strncmp(buffer, "Exit", 4 ) == 0  || strncmp(buffer, "EXIT", 4 ) == 0 ){
                isDone = 0;
        }
        n = write(sockfd,buffer,strlen(buffer));
        if (n < 0)
                error("ERROR writing to socket");
        bzero(buffer,256);
        n =0;
        n = read(sockfd,buffer,255);
        if (n < 0)
                 error("ERROR reading from socket");
        printf("%s\n",buffer);
        sprintf(command1, "netstat -na | grep %s", argv[2]);//show server is listening and established
        sprintf(command2, "ps -ef | grep -e ./server -e %s", argv[2]);//show server
        system(command1);
        system(command2);
        if(isDone == 0){
                printf("client exit\n");
                break;
        }
    }
    return 0;
}

