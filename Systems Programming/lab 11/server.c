/* A simple server in the internet domain using TCP
   The port number is passed as an argument
https://www.cs.rpi.edu/~moorthy/Courses/os98/Pgms/server.c
*/
//Alec Dipasquale and Bryan Vincello Lab11 server.c
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
    exit(1);
}

int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno, clilen;
     char buffer[256];
     char sockMsg[30] = "I got message #";
     char sCount[10] = "";
     struct sockaddr_in serv_addr, cli_addr;
     int n;
     int count = 0;
     char command[128];
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     sockfd = socket(AF_INET, SOCK_STREAM, 0);
     if (sockfd < 0)
        error("ERROR opening socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = atoi(argv[1]);
     //check for correct port input
     if(portno < 1024){
             printf("Sorry that's a 'well-known' port and can't be used!\n");
             exit(0);
     } else if(portno > 49151){
             printf("Sorry that's an 'ephemeral' port and can't be used!\n");
             exit(0);
     }
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
//     serv_addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
//     serv_addr.sin_addr.s_addr = htonl(0x824414ab);
     serv_addr.sin_port = htons(portno);
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0)
              error("ERROR on binding");
     listen(sockfd,5);
   clilen = sizeof(cli_addr);
     newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
     if (newsockfd < 0)
          error("ERROR on accept");
     //loop for persistent connection and iterative message response
     for(;;){
        bzero(buffer,256);
        n = read(newsockfd,buffer,255);
        if (  strncmp(buffer, "exit", 4 ) == 0 || strncmp(buffer, "Exit", 4 ) == 0  || strncmp(buffer, "EXIT", 4 ) == 0 ){
                printf("Connection closed. Waiting for new connection.\n");
                break;
        }
        if (n < 0) error("ERROR reading from socket");
        printf("Here is the message: %s\n",buffer);
        count++;//increment message response
        sprintf(sCount, "%d", count);
        strcat(sockMsg, sCount);
        n = write(newsockfd, sockMsg,18);
        strcpy(sockMsg, "I got message #");
        if (n < 0) error("ERROR writing to socket");

     }
     return 0;
}

