import files
import time
import os
from functions import create,view,delete,cls,category_edit,edit,status,get_date,category_select,owner_select,owner_edit

def app_menu():
    while True:
        menu=input("""
Welcome!
Please choose an option:

(A)dd a new task
(E)dit a task
(R)emove a task
(V)iew tasks by owner name
(S)et a task status
(C)ategories options
(O)wner options

(Q)uit\n""")

        if menu.lower().strip()=="a":
            cls()
            name=input("Choose a title for the task:\n")
            start_date=input("""
Start date:
1) To choose the current date
2) To insert a different date\n""")
            if start_date=='1':
                start_date=get_date()
            elif start_date=='2':
                start_date=input("Please insert the date with the following format dd/mm/yyyy:\n")
            else: print("Wrong choice"),create()
    
            finish_date=input("""
Finish date:
1) To choose the current date
2) To insert a different date\n""")
            if finish_date=='1':
                finish_date=get_date()
            elif finish_date=='2':
                finish_date=input("Please insert the date with the following format dd/mm/yyyy:\n")
            else: print("Wrong choice"),create()

            owner=owner_select()
            description=input("Please write the description of the task:\n")
            category=category_select()
            create(name=name,start_date=start_date,finish_date=finish_date,owner=owner,description=description,category=category)
            cls()
        if menu.lower().strip()=="e":
            cls()
            edit()
            cls()
        if menu.lower().strip()=="v":
            cls()
            owner=input("Please enter the task owner name:\n")
            print(view(owner))
            cls()
        if menu.lower().strip()=="r":
            cls()
            owner=input("Enter a task owner name:\n").capitalize()
            if not view(owner):
                app_menu()
            else: pass
            id=int(input("Enter a task ID to remove:\n"))
            delete(id=id,owner=owner)
            cls()
        if menu.lower().strip()=="q":
            print("Bye bye..")
            break
        if menu.lower().strip()=="c":
            cls()
            category_edit()
            time.sleep(3)
            cls()
        if menu.lower().strip()=="o":
            cls()
            owner_edit()
            time.sleep(3)
            cls()
        if menu.lower().strip()=="s":
            cls()
            owner=input("Please enter the task owner name:\n").capitalize()
            status(owner)
            

            

        
app_menu()
