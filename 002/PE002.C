#include <stdio.h>

int main(){
	printf("Enter the range : ");
	int a,b,sum,P,c;
	scanf("%d",&P);
	a=1;
	b=1;
	sum=0;
	while (1){
		if (b>P){
			break;
		}else{
			c=b;
			b=b+a;
			a=c;
			int k=b%2;
			if (b % 2==0){
				sum=sum+b;
			}
		}
	}
	printf("The sum of the even numbers in range =%d\n",sum);
	return 0;
}