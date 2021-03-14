#include "Aray.h"


FILE *fp;

float a=0;
int otf=0;
float b=0;
float c=0;
float cheak=0;
float dU=0;

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
	fprintf(fp,"%f\n",dU);
	
	
	}

}