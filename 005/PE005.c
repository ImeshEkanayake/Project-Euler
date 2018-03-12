#include <stdio.h>
int main(){
	int p,prod;
	prod=1;
	printf("Max multiplyer :");
	scanf("%d",&p);
	int num_arr[p];
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
		while (k<p & k>0){
			num_arr[i]=k;
			k=k*K;
		}
		if (k>0){
			prod=prod*num_arr[i];

		}

	}

	printf("The product = %d\n",prod);
	return 0;
}