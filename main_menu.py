
from my_users import *

def mainmenu():
    while True:
        print("--------------(Pro Menu)------------------")
        print("1. insert Data")
        print("2. update data")
        print("3. Delete data")
        print("4. View data")
        print("5. Exit")
        choice = input("Enter Your Choice:) ")
        if choice == "1":
            insertdata()

        elif choice == "2":
            updatedata()

        elif choice == "3":
            deletedata()
        elif choice == "4":
            viewdata()
        elif choice == "5":
            exit()
        else:
            print("Invalid choice please try again :)")


mainmenu()

# ----------------------------------------------------------------
