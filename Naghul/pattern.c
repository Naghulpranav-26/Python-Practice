#include<stdio.h>
void main()
{
        int a,i,j;
        printf("Enter the number:");
        scanf("%d",&a);
        for (i=0;i<a;i++)
        {
            for(j=0;j<=a;j++)
            {
                printf("* ");

            }
            printf("\n* ");
        }
}
