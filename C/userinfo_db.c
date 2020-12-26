#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 32


int main()
{
    FILE *fpt;

    char content[128];
    int choice;
    char input[32];

    //seb im sorry lol i think this is an okay way of doing it :joy:
    //char disgusting_setup_sequence[30] = "password:\nname:\nsurname:\nage:\n";

    char pass_setup[9] = "password:";
    char name_setup[5] = "name:";
    char surname_setup[8] = "surname:";
    char age_setup[4] = "age:";
    
    fpt = fopen("user_info.txt", "a+");

        printf("Do you want to login, or create an account? 1/2");
    while (1)
    {
        scanf("%d", choice);
        if (choice == 1)
        {
            //this will come later
        }
        else if (choice == 2)
        {
            printf("Enter the password you want to use (max 32 characters) > ");
            fgets(input, MAX_SIZE, stdin);
            
            //im using this because it's safe
            for (int i = 0; i < 9; i++)
            {
                int char_ascii = pass_setup[i];
                fputc(char_ascii, fpt);
            }

            //better safe than sorry, just look and yanderedev's example poggg
            for (int i = 0; i < 10; i++)
            {
                int char_ascii = input[i];
                fputc(char_ascii, fpt);
            }

            printf("Enter your name (max 10 characters) > ");
            fgets(input, MAX_SIZE, stdin);


            
            

        }
        
    }
    
    
    while (1)
    {
        char *str_input = fgets(content, 64, fpt);
        if (str_input == NULL)
        {
            
        }

    fclose(fpt);
    return 0;
}