#include <stdio.h>

int main()
{
    FILE *fpt;

    //read
    char arr[64];
    char input[64];
    fpt = fopen("textfile.txt", "r");
    while (1)
    {
        char *s = fgets(arr, 64, fpt);
        if (s == NULL)
        {
            break;
        }
        
        printf("%s", arr);
    }
    fclose(fpt);

    //write
    
    while (1)
    {
        fpt = fopen("textfile.txt", "a+");
        fgets(input, 64, stdin);
        if (input[0] == '!')
        {
            break;
        }
        else
        {
            fprintf(fpt, "%s", input);
        }
        fclose(fpt);
        
    }
    fclose(fpt);
     return 0;


}
