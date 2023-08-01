#####################################################################################
####################Imports##########################################################

import datetime
import os
import time
from classes import Task
from files import save_file , load_file,load_list,owner_list



#####################################################################################
####################Helping functions################################################
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def get_date():
    today = datetime.datetime.now()
    fulldate = f"{today.day}/{today.month}/{today.year}"
    return fulldate

def generate_id(owner):
    tasks=load_file()
    max_id=0
    id=0
    for row in tasks:
        id=row.id
        if id>max_id:
            max_id=id
    max_final=max_id+1
    return max_final

def another_change():
        choice=input("Would you like to change anything else?(Yes/No):\n")
        if choice.lower().strip()=="yes":
            edit()
        else:
            print ("Exiting to the main menu..")
            time.sleep(2)
            return ""
#####################################################################################
####################Menu functions###################################################
def create(name,start_date,finish_date,owner,description,category):
    newtask=Task(name=name.capitalize(),start_date=start_date,finish_date=finish_date,owner=owner.capitalize(),description=description,category=category,id=generate_id(owner=owner),finished="no")
    add(newtask)
    print ("Task added successfully...")
    time.sleep(3)
    cls()

   
def edit():
    local_owner_list=load_list(filename="owners.pickle",list_name=owner_list)
    tasks=load_file()
    categories=load_list()
    owner=input("Owner of the task:\n").capitalize().strip()
    owner_count=False
    for row in tasks:
        if owner==row.owner:
            owner_count=True
    if owner_count==False:
        print (f"The owner {owner} does not exist..Please try again")
        edit()

    view(owner=owner)

    task_id=int(input("choose the task ID you would like to change:\n"))
    if find(task_id,owner)!="Task exist":
        print("Please try again")
        time.sleep(3)
        cls()
        edit()

    cls()
    parameter=int(input("""
What detail would you like to change?:
1) Owner name
2) Task name
3) Start date
4) Finish date
5) Description
6) Category\n"""))

    if parameter not in [1,2,3,4,5,6]:
        print("you have chosen a wrong number")
        edit()
    
    counter=False
    if parameter==1:
        print (f"Choose a name from the owner list: {local_owner_list}")
        new_val=input(f"Please enter a new value:\n").capitalize()
        for row in tasks:
            if row.owner==owner and row.id==task_id and new_val in local_owner_list:
                row.owner=new_val.capitalize().strip()
                counter=True
                print("Owner name has changed successfully")
                save_file(tasks)
                another_change() 
        if counter==False:
            print("Something went wrong")
            another_change()
    
    if parameter==2:
        for row in tasks:
            new_val=input(f"Please enter a new value:\n")
            if row.owner==owner and row.id==task_id:
                row.name=new_val.capitalize().strip()
                counter=True
                print("Task name has changed successfully")
                save_file(tasks)
                another_change()
        if counter==False:
            print("Something went wrong")
            another_change()

    if parameter==3:
        for row in tasks:
            new_val=input(f"Please enter a new value:\n")
            if row.owner==owner and row.id==task_id:
                row.start_date=new_val
                counter=True
                print("Start date has changed successfully")
                save_file(tasks)
                another_change()
        if counter==False:
         print("Something went wrong")
         another_change()

    if parameter==4:
        new_val=input(f"Please enter a new value:\n")
        for row in tasks:
            if row.owner==owner and row.id==task_id:
                row.finish_date=new_val
                counter=True
                print("finish date has changed successfully")
                another_change()
                save_file(tasks)
        if counter==False:
            print("Something went wrong")
            another_change()
    
    if parameter==5:
        new_val=input(f"Please enter a new value:\n")
        for row in tasks:
            if row.owner==owner and row.id==task_id:
                row.description=new_val
                counter=True
                print("The description has changed successfully")
                save_file(tasks)
                another_change()
        if counter==False:
            print("Something went wrong")
            another_change()
    
    if parameter==6:
        print (show_category())
        new_val=input(f"Please enter a new value:\n")
        for row in tasks:
            if row.owner==owner and row.id==task_id and new_val in categories:
                new_val=row.category
                counter=True
                print("Category has changed successfully")
                save_file(tasks)
                another_change()
        if counter==False:
            print("Something went wrong")
            another_change()

def view(owner):
    loaded=load_file()
    count=False
    for row in loaded:
        if owner.capitalize()==row.owner:
           print(row)
           #dict_vals=[row.name,row.start_date,row.finish_date,row.description,row.category,row.id,row.finished]
           #row_dict=dict(zip(dict_keys,dict_vals))
           #full_list.append(row_dict)
           count=True
    if count:
       # print (f"The tasks of {owner} are:", *full_list,sep="\n" )
        time.sleep(5)
        return True
    else:
        print (f"The owner {owner} has no tasks..")
        time.sleep(3)
        return False
    
def delete(id,owner):
    loaded=load_file()
    count=False
    for task in loaded.copy():
        if task.id==id and task.owner==owner:
            count=count+1
            loaded.remove(task)
            save_file(loaded)
            print (f"{task.name} removed succuessfully.")
            time.sleep(2)
            return True
            
    if not count:
        print("No task were found")
        time.sleep(2)
        return False

def status(owner):
    tasks=load_file()
    while True:
        if not view(owner):
            owner = input("Please enter the task owner name:\n").capitalize().strip()
        else:
            id=int(input("Choose the task ID that you want to set as finished\n"))
            for row in tasks:
                if row.owner==owner and row.id==id and row.finished=="no":
                    row.finished="yes"
                    print(f"WooHooo! you have finished the task {row.name}")
                    save_file(tasks)
                    time.sleep(2)
                    return ""

#####################################################################################
####################Categories functions#############################################
def show_category():
    local_list=load_list()
    return f"The categories are: {local_list}"

def category_select():
    local_list=load_list()
    category=input(f"Please choose a category from the list: {local_list}\n")
    if category in local_list:
        return category
    else: return category_select()

def category_edit():
    local_list=load_list()
    tasks=load_file()
    category_option=int(input("""
1) To show the categories
2) To add a new category
3) To remove a category
4) To return to the main menu\n"""))

    if category_option==1:
        print(show_category())
        time.sleep(2)
        cls()
        category_edit()
    
    if category_option==2:
        print(show_category())
        #count=0
        category_to_add=input("New category name:\n")
        #count=count+1
        if category_to_add.lower().strip() in local_list:
            print(f"The category '{category_to_add}' already exist")
            category_edit()
        else:
            local_list.append(category_to_add)
            print (f"The category '{category_to_add}' added successfully.")
            save_file(list_to_save=local_list,filename="category.pickle")



    if category_option==3:
        count=0
        category_in_use=False
        print(show_category())
        category_to_remove=input("Category name to remove:\n")
        for row in tasks:
            if row.category==category_to_remove:
                category_in_use==True
                print (f"Cant remove the Category {category_to_remove}, its in use by a task.")
                return ""
        for row in local_list:
            if category_to_remove.lower().strip() in local_list:
                local_list.remove(category_to_remove)
                save_file(list_to_save=local_list,filename="category.pickle")
                count=1
                print (f"The category '{category_to_remove}' removed successfully")
        if count==0:
            print(f"The category '{category_to_remove}' does not exist..")

    if category_option==4:
        print ("exiting to the main menu..")
#####################################################################################
####################Owner functions##################################################

def owner_select():
    local_list=load_list(filename="owners.pickle",list_name=owner_list)
    owner=input(f"Please choose an owner from the list: {local_list}\n").capitalize().strip()
    if owner in local_list:
        return owner
    else: return owner_select()

def owner_edit():
    local_list=load_list(filename="owners.pickle",list_name=owner_list)
    tasks=load_file()
    owner_menu=int(input("""
1) To show the owners list
2) To add a new owner
3) To remove an owner
4) To return to the main menu\n"""))

    if owner_menu==1:
        cls()
        print(f"The owners are:{local_list}")
        time.sleep(3)
        cls()
        owner_edit()
    
    if owner_menu==2:
        cls()
        count=0
        owner_to_add=input("New owner name:\n").capitalize().strip()
        count=count+1
        if owner_to_add in local_list:
            print("Owner already exist")
            time.sleep(2)
            cls()
            owner_edit()
        else:
            local_list.append(owner_to_add)
            save_file(list_to_save=local_list,filename="owners.pickle")
            print(f"{owner_to_add} added successfully.")
            time.sleep(2)
            cls()
            owner_edit()



    if owner_menu==3:
        cls()
        count=False
        owner_in_use=False
        print(local_list)
        owner_to_remove=input("Owner name to remove:\n").capitalize().strip()
        for row in tasks:
            if row.owner==owner_to_remove:
                owner_in_use==True
                print (f"Cant remove the Owner: {owner_to_remove}, its in use by a task.")
                time.sleep(2)
                cls()
                owner_edit()
        for row in local_list:
            if owner_to_remove.capitalize().strip() in local_list:
                local_list.remove(owner_to_remove)
                save_file(list_to_save=local_list,filename="owners.pickle")
                count=True
                print (f"the owner name: '{owner_to_remove}' removed successfully")
                time.sleep(1)
                cls()
                owner_edit()
        if not count:
            print(f"{owner_to_remove} does not exist..")
            time.sleep(1)
            cls()
            owner_edit()

    if owner_menu==4:
        print ("exiting to the main menu..")
        time.sleep(1)
#####################################################################################
####################Files functions##################################################
def add(newtask):
    loaded=load_file()
    loaded.append(newtask)
    save_file(loaded)

#####################################################################################
####################test functions###################################################

def find(id,owner):
    tasks=load_file()
    counter=False
    for row in tasks:
        if id == row.id and row.owner==owner:
            counter=True
        if counter==True:
            return ("Task exist")
    else:return ("Task does not exist")

