#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 

void *myFunction(void* arg) {
	
	int* val = (int *)arg;

	if(*val == 0) {
		printf("Hello World\n");
	}
	
	else if (*val == 1) {
		printf("Goodbye World\n");
	}
	sleep(1);

	return NULL; 
} 

int main() {
 
	int i = 0;  
	pthread_t thread_id;
	while(1) {
		i = 0;
		while (i < 2) { 
			pthread_create(&thread_id, NULL, myFunction, (void *)&i); 
			pthread_join(thread_id, NULL); 
			i++; 
		} 
	}

	return 0; 
} 
