#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 32


int main()
{
    FILE *fpt;

    char content[128];
    int choice;
    char input[MAX_SIZE];
    char useless[4];

    //seb im sorry lol i think this is an okay way of doing it :joy:
    //char disgusting_setup_sequence[30] = "password:\nname:\nsurname:\nage:\n";

    char pass_setup[9] = "password:";
    char name_setup[5] = "name:";
    char surname_setup[8] = "surname:";
    char age_setup[4] = "age:";
    
    fpt = fopen("user_info.txt", "a+");

        printf("Do you want to login, or create an account? 1/2\n");
    while (1)
    {
        scanf("%d", &choice);

        //fgets to consume the \n ????
        fgets(useless, 4, stdin);
        //

        if (choice == 1)
        {
            printf("you chose 1");
            break;
            //this will come later
        }
        else if (choice == 2)
        {
            int counter;
            int temp_size;

            // ENTERING PASSWORD

            printf("Enter the password you want to use (max 32 characters) > ");
            fgets(input, MAX_SIZE, stdin);
            
            //counter determining the size of the string
            counter = 1;
            for (int i = 0; i < MAX_SIZE; i++)
            {
                if (input[i] == '\n')
                {
                    break;
                }
                else
                {
                    counter++;
                }
            }
            temp_size = counter;

            //safe approach of storing shit into file
            for (int i = 0; i < 9; i++)  // 5 is size of "password:"
            {
                int char_ascii = pass_setup[i];
                fputc(char_ascii, fpt);
            }

            //again, i mean copy pasting code cannot be bad, right? just look at yanderedev's example pogg
            for (int i = 0; i < temp_size; i++)
            {
                int char_ascii = input[i];
                fputc(char_ascii, fpt);
             
            }

            //ENTERING NAME 

            printf("Enter your name (max 32 characters) > ");
            fgets(input, MAX_SIZE, stdin);

            //counter determining the size of the string
            counter = 1;
            for (int i = 0; i < MAX_SIZE; i++)
            {
                if (input[i] == '\n')
                {
                    break;
                }
                else
                {
                    counter++;
                }
            }
            temp_size = counter;


            for (int i = 0; i < 5; i++)  // 5 is size of "name:"
            {
                int char_ascii = name_setup[i];
                fputc(char_ascii, fpt);
            }

            for (int i = 0; i < temp_size; i++)
            {
                int char_ascii = input[i];
                fputc(char_ascii, fpt);
             
            }

            //ENTERING SURNAME 

            printf("Enter your surname (max 32 characters) > ");
            fgets(input, MAX_SIZE, stdin);

            //counter determining the size of the string
            counter = 1;
            for (int i = 0; i < MAX_SIZE; i++)
            {
                if (input[i] == '\n')
                {
                    break;
                }
                else
                {
                    counter++;
                }
            }
            temp_size = counter;


            for (int i = 0; i < 8; i++)  // 8 is size of "surname:"
            {
                int char_ascii = surname_setup[i];
                fputc(char_ascii, fpt);
            }

            for (int i = 0; i < temp_size; i++)
            {
                int char_ascii = input[i];
                fputc(char_ascii, fpt);
             
            }
            

            //ENTERING AGE 

            printf("Enter your age (max 3 integers) > ");
            fgets(input, 3, stdin);

            //counter determining the size of the string
            counter = 0;   //for some reason counter here needs to be 0 to work
            for (int i = 0; i < MAX_SIZE; i++)
            {
                if (input[i] == '\n' || input[i] == '\0')  //weird interaction, must investigate further
                {
                    break;
                }
                else
                {
                    counter++;
                }
            }
            temp_size = counter;


            for (int i = 0; i < 4; i++)  // 4 is size of "age:"
            {
                int char_ascii = age_setup[i];
                fputc(char_ascii, fpt);
            }

            for (int i = 0; i < temp_size; i++)
            {
                int char_ascii = input[i];
                fputc(char_ascii, fpt);
             
            }
            break;
        }
        else
        {
            printf("Invalid input, try again!\n");
        }
        

        
    }
    
    // while (1)
    // {
    //     char *str_input = fgets(content, 64, fpt);
    //     if (str_input == NULL)
    //     {
            
    //     }
    // }

    fclose(fpt);
    return 0;
}