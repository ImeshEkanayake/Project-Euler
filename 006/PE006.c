#include <stdio.h>
int main(){
	int S,s,p;
	S=0;
	s=0;
	printf("sum of the sqr and sqr of the cum different of first =");
	scanf("%d",&p);
	for (int i=1;i<=p;i++){
		S=S+(i*i);
		s=s+i;
	}
	s=s*s;
	printf("The answer = %d\n",s-S );
	return 0;
}
