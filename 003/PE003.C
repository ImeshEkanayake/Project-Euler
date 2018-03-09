
/*
Use gcc PE003.c -lm     to compile 
*/
#include <stdio.h>
#include <math.h>
int main(){
	double range,limit,x,maxP;
	int i=2;
	printf("Enter the value :");
	scanf("%lf",&range);
	limit=sqrt(range);
	x=range;
	maxP=range;
	while (i<limit){
		
		if (fmodl(range, i)==0){
			maxP=i;
			printf("fmod(%lf, %d) = %.1f\n", range,i,fmod(range,i));
			range=range/i;
		}else{
		i+=1;
		}
		if (i>limit & range>limit ){
			maxP=range;
			break;
		}

	}
	printf("%lf\n",maxP);
	return 0;
	}
