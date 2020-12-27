#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 32
#define pass_setup_size 9  
#define name_setup_size 5  
#define surname_setup_size 8  
#define age_setup_size 4  
            
char pass_setup[9] = "password:";
char name_setup[5] = "name:";
char surname_setup[8] = "surname:";
char age_setup[4] = "age:";
FILE *fpt;
int temp_size;

int counterFunc(char inputArray[MAX_SIZE])
{ 
    int counterFunc = 1;
    for (int i = 0; i < MAX_SIZE; i++)
    {
        if (inputArray[i] == '\n')
        {
            break;
        }
        else
        {
            counterFunc++;
        }
    }
    return counterFunc;
}

void categorySetup(int sizeOfArray, char setupArray[MAX_SIZE])
{
    for (int i = 0; i < sizeOfArray; i++)
    {
        int char_ascii = setupArray[i];
        fputc(char_ascii, fpt);
    }
}

void inputPrint(int temp_size, char inputArray[MAX_SIZE])
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
    char input[MAX_SIZE];
    char useless[4];

    //seb im sorry lol i think this is an okay way of doing it :joy:
    //char disgusting_setup_sequence[30] = "password:\nname:\nsurname:\nage:\n";
    
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
            printf("you chose 1");
            break;
            //this will come later
        }
        else if (choice == 2)          //account creation
        {


            // ENTERING PASSWORD


            printf("Enter the password you want to use (max 32 characters) > ");
            fgets(input, MAX_SIZE, stdin);
            
            temp_size = counterFunc(input);    //counter determining the size of the string                           

            categorySetup(pass_setup_size, pass_setup);  //safe approach of storing shit into file
    
            inputPrint(temp_size, input); //printing the user input value


            //ENTERING NAME 


            printf("Enter your name (max 32 characters) > ");
            fgets(input, MAX_SIZE, stdin);

            temp_size = counterFunc(input);

            categorySetup(name_setup_size, name_setup);

            inputPrint(temp_size, input);


            //ENTERING SURNAME 


            printf("Enter your surname (max 32 characters) > ");
            fgets(input, MAX_SIZE, stdin);

            temp_size = counterFunc(input);

            categorySetup(surname_setup_size, surname_setup);

            inputPrint(temp_size, input);
            

            //ENTERING AGE 

            printf("Enter your age (max 3 integers) > ");
            fgets(input, MAX_SIZE, stdin);

            temp_size = counterFunc(input);

            categorySetup(age_setup_size, age_setup);

            inputPrint(temp_size, input);
            break;
        }
        else
        {
            printf("Invalid input, try again!\n");
        }
        

        
    }

    fclose(fpt);
    return 0;
}