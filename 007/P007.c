#include <stdio.h>
int main(){
	int p,prod;
	prod=1;
	printf("Max multiplyer :");
	scanf("%d",&p);
	int P=p;
	p=p*100/8;
	//int primes[P*10]
	int num_arr[p];
	int count=0;
	int prime=0;
	for (int i=2;i<p;i++){
		num_arr[i-2]=i;
	}
	for (int i=0;i<p-2;i++){
		int K=num_arr[i];
		int k=K*2;

		while (k<p & k>0){
			num_arr[k-2]=0;
			k=k+K;
			
		}
		k=K;
		
		
		if (k>0){
			if (count!=P){
			prime=k;
			count+=1;
			}else{
				break;
			}

		}

	}

	printf("The product = %d\n",prime);
	return 0;
}