#include <stdio.h>
#define name_size 10
#define sur_size 20
#define pass_size 10

int main()
{
    FILE *fp;
    int shortterm_i;
    char password[pass_size];
    char name_temp[name_size];
    char surname_temp[sur_size];
    char age_temp[3];
    fp = fopen("C:\\Users\\jbock\\OneDrive\\Desktop\\Programming Projects\\C\\Read Write\\textfile1.txt", "w+");

    //initialisation
    while (1)
    {
        printf("Do you want to open a new account, or login? (1/2) > ");
        scanf("%d", &shortterm_i);

        if (shortterm_i == 1)
        {
            printf("Enter the password you want to use for future logins > ");
            fgets(password, pass_size, stdin);

            printf("Please enter your name > ");
            fgets(name_temp, name_size, stdin);

            printf("Please enter your surname > ");
            fgets(surname_temp, sur_size, stdin);

            printf("And lastly, enter your age > ");
            fgets(age_temp, 3, stdin);
            break;
        }
        else if (shortterm_i == 2)
        {
            printf("Enter your password > ");
            fgets(password, pass_size, stdin);
            break;
        }
    }

for (int i = 0; i < 10; i++)
{
    printf("%c", password[i]);
}
printf("\n");
for (int i = 0; i < 10; i++)
{
    printf("%c", name_temp[i]);
}
printf("\n");
for (int i = 0; i < 20; i++)
{
    printf("%c", surname_temp[i]);
}


    
    
    
    

    



    fclose(fp);

    
    return 0;
}