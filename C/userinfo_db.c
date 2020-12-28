#include <stdio.h>
#include <stdlib.h>

#define max_size 32
#define pass_setup_size 9  
#define name_setup_size 5  
#define surname_setup_size 8  
#define age_setup_size 4  
            
const char pass_setup[9] = "password:";
const char name_setup[5] = "name:";
const char surname_setup[8] = "surname:";
const char age_setup[4] = "age:";
FILE *fpt;
int temp_size;
int flag = 0;

int sizeOfFILE = 0;  //the important one for password checking

int counterFunc(char inputArray[max_size])
{ 
    int counterFunc = 1;
    for (int i = 0; i < max_size; i++)
    {
        if (inputArray[i] == '\n')
        {
            break;
        }
        else
        {
            counterFunc++;
        }
        if (!((inputArray[i] >= 65 && inputArray[i] <= 90) || (inputArray[i] >= 97 && inputArray[i] <= 122)))
        {
            flag = 1;
        }
        

    }
    return counterFunc;
}

void categorySetup(int sizeOfArray, const char setupArray[max_size])
{
    for (int i = 0; i < sizeOfArray; i++)
    {
        int char_ascii = setupArray[i];
        fputc(char_ascii, fpt);
    }
}

void inputPrint(int temp_size, char inputArray[max_size])
{
    for (int i = 0; i < temp_size; i++)
    {
        int char_ascii = inputArray[i];
        fputc(char_ascii, fpt); 
    }
}


int main()
{
    int choice;
    char *ifEmpty;
    char input[max_size];
    char useless[4];
    char temp_passInput[max_size];

    //seb im sorry lol i think this is an okay way of doing it :joy:
    
    fpt = fopen("user_info.txt", "a+");

        printf("Do you want to login, or create an account? 1/2\n");
    while (1)
    {
        scanf("%d", &choice);

        //fgets to consume the \n ????
        fgets(useless, 4, stdin);
        //

        if (choice == 1)               //account login
        {
            char *s = fgets(useless, 4, fpt);
            if (s == NULL)
            {
                printf("There are no accounts registered, creating a new account now.\n");
                goto characterCreation;  //you'll like this one seb
            }
            else
            {
                printf("Enter your password > ");
                fgets(temp_passInput, max_size, fpt);  //user inputing password which will go through check
                int temp_passSize = counterFunc(temp_passInput);  //getting the size of the password
                
                //creating the right sized array for the user inputted password
                char pass_for_check[temp_passSize];
                for (int i = 0; i < temp_passSize; i++)
                {
                    pass_for_check[i] = temp_passInput[i];
                }

                for (int i = 0; i < sizeOfFILE; i++)
                {

                    if (feof(fpt))
                    {
                        break;
                    }

                    
                }

            }
                
            break;
        }
        else if (choice == 2)          //account creation
        {
            characterCreation:

            // ENTERING PASSWORD


            printf("Enter the password you want to use (max 32 characters) > ");
            fgets(input, max_size, stdin);
            
            temp_size = counterFunc(input);    //counter determining the size of the string                           

            categorySetup(pass_setup_size, pass_setup);  //safe approach of storing shit into file
    
            inputPrint(temp_size, input); //printing the user input value


            //ENTERING NAME 

            printf("Enter your name (max 32 characters) > ");
            while (flag == 0)
            {
                fgets(input, max_size, stdin);
                temp_size = counterFunc(input);
            }

            categorySetup(name_setup_size, name_setup);

            inputPrint(temp_size, input);


            //ENTERING SURNAME 


            printf("Enter your surname (max 32 characters) > ");
            fgets(input, max_size, stdin);

            temp_size = counterFunc(input);

            categorySetup(surname_setup_size, surname_setup);

            inputPrint(temp_size, input);
            

            //ENTERING AGE 


            printf("Enter your age (max 3 integers) > ");
            fgets(input, max_size, stdin);

            temp_size = counterFunc(input);

            categorySetup(age_setup_size, age_setup);

            inputPrint(temp_size, input);
            
            //listen, i know what this looks like and i am not ashamed
            sizeOfFILE += max_size*4 + pass_setup_size + name_setup_size + surname_setup_size + age_setup_size;
        }
        else
        {
            printf("Invalid input, try again!\n");
        }
        

        
    }

    fclose(fpt);
    return 0;
}