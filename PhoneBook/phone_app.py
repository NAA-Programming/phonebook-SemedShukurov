from json import * #!I used JSON to store the data in a file called db.json, 
import os #? do not import all in os , otherwise it will give you error
import time #?Time is used to add a delay 



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#* When Updating the code, I will use this function to clear the screen before printing the banner again.
#* This will help to keep the screen clean and make it easier to read the output.


#! Default JSON data When running the code for the first time.
default__json=[
    {
        "name": "Samed",
        "surname": "Hackerov",
        "phone": "+8819281572"
    },
    {
        "name": "Nezrin",
        "surname": "Mehtiyeva",
        "phone": "+216-649-1499"
    },
    {
        "name": "Hamida",
        "surname": "Bananova",
        "phone": "+7 889 099 19 29"
    },
    {
        "name": "Leman",
        "surname": "Ciyeleyova",
        "phone": "+994 50 777 77 77"
    },
    {
        "name": "Cimnaz",
        "surname": "Cimnazova",
        "phone": "+994 50 891 18 47"
    }
]


banner = """
    Welcome to the 

        *******  **                                          **     *******  ******* 
        /**////**/**                                         ****   /**////**/**////**
        /**   /**/**       ******  *******   *****          **//**  /**   /**/**   /**
        /******* /******  **////**//**///** **///**        **  //** /******* /******* 
        /**////  /**///**/**   /** /**  /**/*******       **********/**////  /**////  
        /**      /**  /**/**   /** /**  /**/**////       /**//////**/**      /**      
        /**      /**  /**//******  ***  /**//******      /**     /**/**      /**      
        //       //   //  //////  ///   //  //////       //      // //       //       
    """ 
print(banner)
def laucher():
    choices_banner="""
    Choise an option:
    1. Add a new user
    2. View all users
    3. Search for a user
    4. Delete a user
    5. Update a user
    6. Change the data to default
    7. Exit

    Tip: You should use the number of the option to select it!


    """
    try:
        choice=int(input(choices_banner+": "))
    except ValueError:
        clear_screen()
        print("Invalid input! Please enter a number.")
        choice = 0
    return choice
def change_to_default():
    with open("db.json", "w") as f:
        dump(default__json, f, indent=4)
    print("Data changed to default successfully!")

def add_user():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    phone = input("Enter your phone number: ")
    user = {
        "name": name,
        "surname": surname,
        "phone": phone
    }
    with open("db.json", "r") as f:
        data = load(f)
    data.append(user)
    with open("db.json", "w") as f:
        dump(data, f, indent=4)
    print("User added successfully!")

def view_all_users():
    with open("db.json", "r") as f:
        data = load(f)
    if len(data)==0:
        print("No users found!")
    else:
        for user in data:
            print(f"\n Name: {user['name']}, Surname: {user['surname']}, Phone: {user['phone']} \n")

def search_user():
    name = input("Enter the name of the user you want to search for: ")
    with open("db.json", "r") as f:
        data = load(f)
    found = False
    for user in data:
        if user['name'].lower() == name.lower():
            print(f"\n Name: {user['name']}, Surname: {user['surname']}, Phone: {user['phone']} \n")
            found = True
            break
    if not found:
        print("User not found!")

def delete_user():
    view_all_users()
    name = input("Enter the name of the user you want to delete: ")
    with open("db.json", "r") as f:
        data = load(f)
    found = False
    for user in data:
        if user['name'].lower() == name.lower():
            data.remove(user)
            found = True
            break
    if found:
        with open("db.json", "w") as f:
            dump(data, f, indent=4)
        print("User deleted successfully!")
    else:
        print("User not found!")

def update_user():
    view_all_users()
    name = input("Enter the name of the user you want to update: ")
    with open("db.json", "r") as f:
        data = load(f)
    found = False
    for user in data:
        if user['name'].lower() == name.lower():
            new_name = input("Enter the new name: ")
            new_surname = input("Enter the new surname: ")
            new_phone = input("Enter the new phone number: ")
            user['name'] = new_name
            user['surname'] = new_surname
            user['phone'] = new_phone
            found = True
            break
    if found:
        with open("db.json", "w") as f:
            dump(data, f, indent=4)
        print("User updated successfully!")
    else:
        print("User not found!")

def choice_runner(c):
    clear_screen()
    if c==1:
        print("Adding a new user...") 
        add_user()
    elif c==2:
        print("Viewing all users...") 
        view_all_users()
    elif c==3:
        print("Searching for a user...") 
        search_user()
    elif c==4:
        print("Deleting a user...")
        delete_user()  
    elif c==5:
        print("Updating a user...")
        update_user()
    elif c==6:
        print("Changing the data to default...") 
        change_to_default()
    elif c==7:
        print("Exiting...")
    else:
        print("Invalid choice!")

while True:
    choice = laucher()
    if choice==0:
        time.sleep(1)
        clear_screen()
        continue
    choice_runner(choice)
    if choice==2:
        print("Press any key to continue...")
        input()
        clear_screen()
    elif choice==7:
        time.sleep(0.5)
        clear_screen()
        print("Byeee! See you next time!")
        break
    else:
        time.sleep(1.3)
        clear_screen()




