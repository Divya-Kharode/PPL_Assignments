#include <stdio.h> 
#include <pthread.h> 
#include <semaphore.h> 
#include <unistd.h> 
#include <stdlib.h>
#include <time.h>
  
int hr, min, sec; 
pthread_t t[3];
pthread_mutex_t lock_x;

void* thread(void* arg) 
{ 
    pthread_mutex_lock(&lock_x);
    int *val = (int *)arg; 
	
	if(*val == 0) {
		while (sec < 60) {
			sleep(1);
			printf("\n");
			printf("\t\t\t\t\t%02d:%02d:%02d\n", hr, min, sec);
			sec++;
		}
	}
	
	else if(*val == 1) {
		sec = 0;
		min += 1;
	}
	
	else if(*val == 2) {
		if (min >= 60) {
			min = 0;
			hr += 1;
		}
		
		if(hr >= 24) {
			hr = 0;
			min = 0;
			sec = 0;
		}
	}
	pthread_mutex_unlock(&lock_x);
    
}


int main() {
 	
    time_t rawtime;
    struct tm * t;
    time(&rawtime);
    t = localtime(&rawtime);
    hr = t->tm_hour;
    min = t->tm_min; 
    sec = t->tm_sec;
    pthread_mutex_init(&lock_x, NULL);
    int i = 0;
    while(1) {
    
    	i = 0;
    	while(i < 3) { 
    		pthread_create(&t[i],NULL,thread,(void*)&i); 
    		pthread_join(t[i],NULL); 
    		i++;
    	}
    	
    } 
    return 0; 
} 
