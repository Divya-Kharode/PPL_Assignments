#include<stdio.h>
#include<limits.h>
int fact(int num){
	if(num < 0)
		return INT_MAX;
	if(num == 0)
		return 1;
	
	return num*fact(num - 1);

}
int main(){
	int num = 5;
	fact(num);
	return 0;
}
