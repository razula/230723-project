#####################################################################################
####################Imports##########################################################
from classes import Task
import random
from functions import create,view,delete,add
from files import load_list,owner_list,load_file

#####################################################################################
####################Testing functions################################################
def create_tasks(num:int=0):
    for i in range(num):
        owner=random.choice(load_list(filename="owners.pickle",list_name=owner_list))
        name=random.choice(['Clean', 'Vacation', 'Home work', 'Dishes', 'Laundry', 'Meeting', 'Shopping'])
        description=random.choice(["description_test1","description_test2","description_test3"])
        start_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2022,2023)}"
        finish_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2024,2025)}"
        id=i
        category=random.choice(load_list())
        add(Task(owner=owner, name=name, finished="no", description=description, category=category,id=id, start_date=start_date, finish_date=finish_date))

#create_tasks(40)

def test_view(owner):
    if view(owner)==True:
        return True
    else: return False

def test_delete(id):
    if delete(id)==True:
        return True
    else: return False

def show_all_tasks():
    local_list=load_file()
    for row in local_list:
        print(row)
    return ""


print(show_all_tasks())