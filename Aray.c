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
		//fp = fopen("data1faze3seti.xls", "w+");
		fp = fopen("dvig5.xls", "w+");
		otf=1;
		
	}
	
	
	Uz=Uz/185;
	U=U/185;
	nc=nc/460;
	dU=dU/1;
	deltaU=deltaU/13;
	param=param/100;
	
	if(cheak>2.5)
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