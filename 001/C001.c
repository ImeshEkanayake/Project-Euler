#include <stdio.h>
int sum_of_range(int x){
	int k;
	k=(x+1)*x/2;
	return k;
}
int main(){
	printf("Enter the range : ");
	int P,p3,p5,p15,sum;
	scanf("%d",&P);
	P=P-1;
	p3=P/3;
	p5=P/5;
	p15=P/15;
	sum=sum_of_range(p3)*3 + sum_of_range(p5)*5 - sum_of_range(p15)*15;
	printf("The tota sum is %d\n",sum );

	return 0;
}