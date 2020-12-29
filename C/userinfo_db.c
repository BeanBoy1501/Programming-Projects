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

char fileContents[65536];

int inputCheck;

FILE *fpt;
int temp_size;
int flag = 0;

int sizeOfFILE = 0;  //the important one for password checking

int counterFunc(char inputArray[max_size], int inputCheck)
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
        if (inputCheck == 1)
        {
            if (!((inputArray[i] >= 65 && inputArray[i] <= 90) || (inputArray[i] >= 97 && inputArray[i] <= 122)))
            {
                flag = 1;
                printf("You have entered an invalid input! Try again.\n");
                break;
            }
            else
            {
                flag = 0;
            }
        }
        else if (inputCheck == 2)
        {
            if (!(inputArray[i] >= 48 && inputArray[i] <= 57))
            {
                flag = 1;
                printf("You have entered an invalid input! Try again.\n");
                break;
            }
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
    char input[max_size];
    char useless[4];
    char temp_passInput[max_size];
    int passIncorrect = 0;

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
                fgets(temp_passInput, max_size, stdin);  //user inputing password which will go through check
                int temp_passSize = counterFunc(temp_passInput, 0);  //getting the size of the password

                //creating the right sized array for the user inputted password
                char pass_for_check[temp_passSize];
                for (int i = 0; i < temp_passSize - 1; i++)
                {
                    pass_for_check[i] = temp_passInput[i];
                    printf("Pass for check -> %c\n", pass_for_check[i]);
                }

                rewind(fpt);
                int counter = 0;
                int ignore = 0;
                int correctPassCounter = 0;
                int c;
                int pass_is_correct = 0;
                char correctPass[temp_passSize];
                while (1)
                {
                    if (feof(fpt))
                    {
                        printf("No account with this password found.");
                        break;
                    }
                    else
                    {
                        if (counter == 9)
                        {
                            c = fgetc(fpt);
                            ignore = 1;
                            if (correctPassCounter < temp_passSize - 1)
                            {
                                correctPass[correctPassCounter] = c;
                                printf("Correct pass -> %c\n", correctPass[correctPassCounter]);
                                correctPassCounter++; 
                            }
                            else
                            {
                                for (int i = 0; i < temp_passSize - 1; i++)
                                {
                                    if (!(pass_for_check[i] == correctPass[i]))
                                    {
                                        ignore = 0;
                                        counter = 0;
                                        correctPassCounter = 0;
                                        printf("WRONG");
                                        passIncorrect = 1;
                                        break;
                                    } 
                                } 
                                if (passIncorrect == 0)
                                {
                                    printf("You have entered the correct password!");
                                }
                                    
                            }
                        }   
                        if (ignore == 0)
                        {
                            c = fgetc(fpt);
                            switch (c)
                            {
                            case 112:
                                counter++;
                                break;
                            case 97:
                                counter++;
                                break;
                            case 115:
                                counter++;
                                break;
                            case 119:
                                counter++;
                                break;
                            case 111:
                                counter++;
                                break;
                            case 114:
                                counter++;
                                break;
                            case 100:
                                counter++;
                                break;
                            case 58:
                                counter++;
                                break;
                            default:
                                counter = 0;
                                break;
                            } 
                        } 
                    }
                    if (pass_is_correct == 1)
                    {
                        break;
                    }
                }
                if (pass_is_correct == 1)
                {
                    int isPrinted = 0;
                    counter = 0;
                    while (1)
                    {
                        if (feof(fpt))
                        {
                            break;
                        }
                        else
                        {
                            //printing out the name
                            while (isPrinted == 0)
                            {
                                c = fgetc(fpt);
                                switch (c)
                                {
                                case 110:
                                    counter++;
                                    break;
                                case 97:
                                    counter++;
                                    break;
                                case 109:
                                    counter++;
                                    break;
                                case 101:
                                    counter++;
                                    break;
                                case 58:
                                    counter++;
                                    break;
                                default:
                                    counter = 0;
                                    break;
                            }
                            
                            }
                        }
                        
                        
                    }
                    
                }
                
            }

        }
        else if (choice == 2)          //account creation
        {
            characterCreation:

            // ENTERING PASSWORD


            printf("Enter the password you want to use (max 32 characters) > ");
            fgets(input, max_size, stdin);

            temp_size = counterFunc(input, 0);    //counter determining the size of the string

            categorySetup(pass_setup_size, pass_setup);  //safe approach of storing shit into file

            inputPrint(temp_size, input); //printing the user input value



            //ENTERING NAME

            printf("Enter your name (max 32 characters) > ");
            do
            {
                fgets(input, max_size, stdin);
                temp_size = counterFunc(input, 1);
            } while (flag == 1);


            categorySetup(name_setup_size, name_setup);

            inputPrint(temp_size, input);


            //ENTERING SURNAME


            printf("Enter your surname (max 32 characters) > ");
            do
            {
                fgets(input, max_size, stdin);
                temp_size = counterFunc(input, 1);
            } while (flag == 1);


            categorySetup(surname_setup_size, surname_setup);

            inputPrint(temp_size, input);


            //ENTERING AGE


            printf("Enter your age (max 3 integers) > ");
            do
            {
                fgets(input, max_size, stdin);
                temp_size = counterFunc(input, 2);
            } while (flag == 1);



            categorySetup(age_setup_size, age_setup);

            inputPrint(temp_size, input);

            //listen, i know what this looks like and i am not ashamed
            sizeOfFILE += max_size*4 + pass_setup_size + name_setup_size + surname_setup_size + age_setup_size;
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