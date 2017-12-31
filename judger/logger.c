#include<stdio.h>
#include<stdlib.h>
#include<sys/file.h>
#include<time.h>
#include<stdarg.h>
#include<unistd.h>

#include"logger.h"

#define LOG_BUFFER_SIZE 8192

FILE *log_open(const char *filename)
{
	FILE *Log_fp=fopen(filename,"a");
	if(log_fp==NULL)
	{
		fprintf(stderr, "can not open log file %s\n",filename );
	}
	return log_fp;
}

void log_close(FILE *log_fp)
{
	if(log_fp!=NULL)
	{
		fclose(log_fp);
	}
}

void write(int level,const char *source_filename,const int line,const FILE *log_fp,const char *fmt,...)
{
	char LOG_LEVEL_NOTE[][10]={"FATAL","WARNING","INFO","DEBUG"};
	if(log_fp==NULL)
	{
		fprintf(stderr,"can not open log file");
		return;
	}

	static char buffer[LOG_BUFFER_SIZE];
	static char	log_buffer[LOG_BUFFER_SIZE];
	static char	datetime[100];
	static char line_str[20];
	static time_t now;
	now=time(NULL);

	strftime(datetime,99,"%Y-%m-%d %H:%M:%S",localtime(&now));
	snprintf(line_str,19,"%d",line);
	va_list ap;
	va_start(ap,fmt);
	vsnprintf(log_buffer,LOG_BUFFER_SIZE,fmt,ap);
	va_end(ap);

	int count=snprintf(buffer,LOG_BUFFER_SIZE,"%s [%s] [%s:%s]%s\n",LOG_LEVEL_NOTE[level],datetime,source_filename,line_str,log_buffer);
	int log_fd=fileno((FILE*)log_fp);
	if(flock(log_fd,LOCK_EX)==0)  //response 0 is success
	{
		if(write(log_fd,buffer,(size_t)count)<0)
		{
			fprintf(stderr, "write error");
			return;
		}
		flock(log_fd,LOCK_UN);
	}  
	else
	{
		fprintf(stderr, "flock error", );
		return;
	}
}