#include "Aray.h"


FILE *fp;

float deltaU=0;
float a=0;
int otf=0;
float b=0;
float c=0;
float cheak=0;
float dU=0;
float old_U=0;
float old_U2=0;


void WriteFunc()
{
	if(!otf)
	{
		fp = fopen("data.xls", "w+");
		otf=1;
	}
	
	a=a/1;
	b=b/2;
	c=c/5;
	dU=dU/45;
	
	if(cheak>=1)
	fclose(fp);
	else
	{
		
	fprintf(fp,"%f;",a);
	fprintf(fp,"%f;",b);
	fprintf(fp,"%f;",c);
	fprintf(fp,"%f;",old_U);
	fprintf(fp,"%f;",dU);
	fprintf(fp,"%f;",cheak);
	fprintf(fp,"%f;",deltaU);
	fprintf(fp,"%f\n",old_U2);
	
	}
	old_U2=old_U;
	old_U=c;
	

}