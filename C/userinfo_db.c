#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fpt;

    char content[128];

    //seb im sorry lol i think this is an okay way of doing it :joy:
    char disgusting_setup_sequence[30] = "password:\nname:\nsurname:\nage:\n";
    
    // char pass_setup[9] = "password:";
    // char name_setup[5] = "name:";
    // char surname_setup[8] = "surname:";
    // char age_setup[4] = "age:";


    fpt = fopen("user_info.txt", "a+");
    //initial reading sequence, checks whether file is empty
    while (1)
    {
        char *str_input = fgets(content, 64, fpt);
        if (str_input == NULL)
        {
            //printing the disgusting_setup_sequence if file is empty
            for (int i = 0; i < 30; i++)
            {
                int value = disgusting_setup_sequence[i];
                fputc(value, fpt);
            }
            printf("empty");
            break;
        }
        else
        {
            printf("%s", str_input);
            printf("not empty");
            break;
        }
        
    }
    

    fclose(fpt);
    return 0;
}