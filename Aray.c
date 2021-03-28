#include "Aray.h"


FILE *fp;

float deltaU=0;
float Uz=0;
int otf=0;
float U=0;
float nc=0;
float cheak=0;
float dU=0;
float old_U=0;
float old_U2=0;
float param;


void WriteFunc()
{
	if(!otf)
	{
		fp = fopen("data1faze3setiR2.xls", "w+");
		otf=1;
		
	}
	
	
	Uz=Uz/100;
	U=U/105;
	nc=nc/3700;
	dU=dU/6.3;
	deltaU=deltaU/100;
	param=param/2;
	
	if(cheak>=1)
	{
	fclose(fp);
	}
	else
	{
		
	fprintf(fp,"%f;",Uz);
	fprintf(fp,"%f;",U);
	fprintf(fp,"%f;",nc);
	fprintf(fp,"%f;",old_U);
	fprintf(fp,"%f;",dU);
	fprintf(fp,"%f;",cheak);
	fprintf(fp,"%f;",deltaU);
	fprintf(fp,"%f;",old_U2);
	fprintf(fp,"%f\n",param);
	
	}
	old_U2=old_U;
	old_U=nc;
	

}