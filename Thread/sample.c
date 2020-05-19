#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
int i = 9;
void *hello(){
	while(i > 0){
		printf("Hey :) \n");
		sleep(1);
		i--;
	}
}
void *Bye(){
	while(i > 0){
		sleep(1);
		printf("Have a nice day (*_*) \n");
		i--; 
	}
}


int main(){
	printf("Execution Started\n");
	pthread_t t1,t2;
	pthread_create(&t1,NULL,hello,NULL);
	pthread_create(&t2,NULL,Bye,NULL);
	pthread_join(t1,NULL);	
	pthread_join(t2,NULL);
	printf("Terminating the program \n");
	return 0;
}
