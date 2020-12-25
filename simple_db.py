from tinydb import TinyDB, Query
db = TinyDB('db.json')
# db.truncate()

initial_sequence = 1


while(initial_sequence != 0):
    initial_choice = int(input("Do you want to create an account, or log in? 1/2\n"))
    if ((initial_choice != 1) & (initial_choice != 2)):
        print("Invalid input, try again.\n")

    elif initial_choice == 1:
        password = input("Enter your login password > ")
        name = input("Enter your name > ")
        surname = input("Enter your surname > ")
        age = input("Enter your age > ")

        db.insert({'password': password, 'name': name, 'surname': surname, 'age': age})
        break

    elif initial_choice == 2:
        incorrect_pass = 1

        while(incorrect_pass == 1):
            pass_input = input("Enter your login password > ")
            pass_checker = Query()
            pass_bool = db.contains('password' == pass_input)
            if pass_bool == 'True':
                incorrect_pass = 0
                print(db.search('password' == pass_input))









