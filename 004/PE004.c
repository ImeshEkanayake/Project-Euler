#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(){
	int p,ll,ul,maxnum,x,g;
	char k[20]={0}; 
	char K[20]={0};
	/* 
	P=number of digits
	ll=lover limit
	ul=upper limit
	*/
	printf("Enter the number of digits to multiply :");
	scanf("%d",&p);
	ul=powl(10,p)-1;
	ll=ul;
	x=ul;
	maxnum=0;

	while (ll!=pow(10,p-1)){
		for (int i=ul;i>ll-1;i--){
			g=i*ll;
			if (maxnum>g){
				break;
			}
			sprintf(k,"%d",g);
			int len=strlen(k);			
			int qwe=1;
			for (int j=0;j<len;j++){
					
					if (k[j]!=k[len-1-j]){
						qwe=0;
						break;
					}
			}
			//printf("%s %d %d\n",k,qwe,maxnum);
			if (qwe==1){
				if (maxnum<g){
					maxnum=g;
				}
			}
			


		}
		ll-=1;
	}
	printf("The maximum palandromic number is %d\n",maxnum );
}
